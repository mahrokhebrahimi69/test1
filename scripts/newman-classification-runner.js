#!/usr/bin/env node
/**
 * Preferred history store for classification QA.
 *
 * Why not Postman Collection Variables?
 * - size limit (~few MB)
 * - wiped easily / not durable across machines
 * - hard to diff, query, resume
 *
 * This runner:
 * - appends one JSON line per case to results/runs/<runId>.jsonl
 * - writes summary JSON next to it
 * - keeps a small index of all runs in results/runs/index.json
 * - supports resume via checkpoint
 *
 * Usage:
 *   node scripts/newman-classification-runner.js
 *   node scripts/newman-classification-runner.js --fresh
 *   node scripts/newman-classification-runner.js --data data/political_comment_dataset.flat.json
 */

const fs = require("fs");
const path = require("path");
const { spawnSync } = require("child_process");

const ROOT = path.resolve(__dirname, "..");
const DEFAULT_COLLECTION = path.join(
    ROOT,
    "postman",
    "preferred",
    "Classification_QA.postman_collection.json"
);
const DEFAULT_DATA = path.join(
    ROOT,
    "data",
    "political_comment_dataset.flat.json"
);
const RESULTS_DIR = path.join(ROOT, "results", "runs");

function parseArgs(argv) {
    const args = {
        collection: DEFAULT_COLLECTION,
        data: DEFAULT_DATA,
        delay: 200,
        timeout: 30000,
        fresh: false,
        baseUrl: process.env.BASE_URL || "https://comment.foodstg.com"
    };
    for (let i = 2; i < argv.length; i++) {
        const a = argv[i];
        if (a === "--fresh") args.fresh = true;
        else if (a === "--data") args.data = path.resolve(argv[++i]);
        else if (a === "--collection") args.collection = path.resolve(argv[++i]);
        else if (a === "--delay") args.delay = Number(argv[++i]);
        else if (a === "--timeout") args.timeout = Number(argv[++i]);
        else if (a === "--base-url") args.baseUrl = argv[++i];
        else if (a === "--help" || a === "-h") {
            console.log(`Usage:
  node scripts/newman-classification-runner.js [--fresh]
      [--data PATH] [--collection PATH]
      [--delay MS] [--timeout MS] [--base-url URL]
`);
            process.exit(0);
        }
    }
    return args;
}

function ensureDir(dir) {
    fs.mkdirSync(dir, { recursive: true });
}

function loadJson(file, fallback) {
    if (!fs.existsSync(file)) return fallback;
    return JSON.parse(fs.readFileSync(file, "utf8"));
}

function classifyStatus(expectedLabel, actualLabel, expectedReason, actualReason) {
    const eLabel = String(expectedLabel || "").trim();
    const aLabel = String(actualLabel || "").trim();
    const eReason =
        expectedReason == null || expectedReason === "null"
            ? ""
            : String(expectedReason).trim();
    const aReason =
        actualReason == null || actualReason === "null"
            ? ""
            : String(actualReason).trim();

    if (eLabel !== aLabel) {
        if (eLabel === "disapproval" && aLabel === "approval") {
            return {
                status: "FALSE_ACCEPT",
                mismatch_type: "should_reject_but_approved"
            };
        }
        if (eLabel === "approval" && aLabel === "disapproval") {
            return {
                status: "FALSE_REJECT",
                mismatch_type: "should_approve_but_rejected"
            };
        }
        return {
            status: "LABEL_MISMATCH",
            mismatch_type: `${eLabel || "empty"}_to_${aLabel || "empty"}`
        };
    }
    if (eReason !== aReason) {
        return { status: "REASON_MISMATCH", mismatch_type: "reason_only" };
    }
    return { status: "PASS", mismatch_type: null };
}

function summarize(rows) {
    const counts = {
        PASS: 0,
        FALSE_ACCEPT: 0,
        FALSE_REJECT: 0,
        LABEL_MISMATCH: 0,
        REASON_MISMATCH: 0,
        ERROR: 0
    };
    for (const r of rows) {
        counts[r.status] = (counts[r.status] || 0) + 1;
    }
    const total = rows.length;
    const pass = counts.PASS || 0;
    return {
        total,
        ...counts,
        accuracy_strict_pct: total
            ? Number(((pass / total) * 100).toFixed(2))
            : 0,
        accuracy_label_only_pct: total
            ? Number(
                  (
                      ((pass + (counts.REASON_MISMATCH || 0)) / total) *
                      100
                  ).toFixed(2)
              )
            : 0,
        false_accept_ids: rows
            .filter((r) => r.status === "FALSE_ACCEPT")
            .map((r) => r.id),
        false_reject_ids: rows
            .filter((r) => r.status === "FALSE_REJECT")
            .map((r) => r.id)
    };
}

function readJsonl(file) {
    if (!fs.existsSync(file)) return [];
    return fs
        .readFileSync(file, "utf8")
        .split("\n")
        .filter(Boolean)
        .map((line) => JSON.parse(line));
}

function main() {
    const args = parseArgs(process.argv);
    ensureDir(RESULTS_DIR);

    if (!fs.existsSync(args.collection)) {
        console.error("Collection not found:", args.collection);
        process.exit(1);
    }
    if (!fs.existsSync(args.data)) {
        console.error("Data file not found:", args.data);
        process.exit(1);
    }

    const dataset = JSON.parse(fs.readFileSync(args.data, "utf8"));
    if (!Array.isArray(dataset) || dataset.length === 0) {
        console.error("Data file must be a non-empty JSON array");
        process.exit(1);
    }

    const runId = new Date().toISOString().replace(/[:.]/g, "-");
    const runDir = path.join(RESULTS_DIR, runId);
    ensureDir(runDir);

    const jsonlPath = path.join(runDir, "results.jsonl");
    const summaryPath = path.join(runDir, "summary.json");
    const metaPath = path.join(runDir, "meta.json");
    const checkpointPath = path.join(RESULTS_DIR, "checkpoint.json");
    const indexPath = path.join(RESULTS_DIR, "index.json");

    let startIndex = 0;
    let activeJsonl = jsonlPath;

    if (!args.fresh && fs.existsSync(checkpointPath)) {
        const checkpoint = loadJson(checkpointPath, null);
        if (
            checkpoint &&
            checkpoint.data === args.data &&
            checkpoint.collection === args.collection &&
            fs.existsSync(checkpoint.jsonlPath)
        ) {
            startIndex = checkpoint.nextIndex || 0;
            activeJsonl = checkpoint.jsonlPath;
            console.log(
                `Resuming from index ${startIndex} -> ${activeJsonl}`
            );
        }
    }

    if (startIndex >= dataset.length) {
        console.log("Nothing to run; dataset already completed.");
        return;
    }

    const slice = dataset.slice(startIndex);
    const slicePath = path.join(runDir, "slice.json");
    fs.writeFileSync(slicePath, JSON.stringify(slice, null, 2), "utf8");

    const meta = {
        runId,
        startedAt: new Date().toISOString(),
        baseUrl: args.baseUrl,
        collection: args.collection,
        data: args.data,
        startIndex,
        totalInDataset: dataset.length,
        scheduled: slice.length
    };
    fs.writeFileSync(metaPath, JSON.stringify(meta, null, 2), "utf8");

    // Prefer local newman binary if present; otherwise npx.
    const newmanBin = fs.existsSync(
        path.join(ROOT, "node_modules", ".bin", "newman")
    )
        ? path.join(ROOT, "node_modules", ".bin", "newman")
        : "npx";

    const newmanArgs =
        newmanBin === "npx"
            ? [
                  "--yes",
                  "newman",
                  "run",
                  args.collection,
                  "-d",
                  slicePath,
                  "--delay-request",
                  String(args.delay),
                  "--timeout-request",
                  String(args.timeout),
                  "--env-var",
                  `baseUrl=${args.baseUrl}`,
                  "--reporters",
                  "cli,json",
                  "--reporter-json-export",
                  path.join(runDir, "newman-raw.json")
              ]
            : [
                  "run",
                  args.collection,
                  "-d",
                  slicePath,
                  "--delay-request",
                  String(args.delay),
                  "--timeout-request",
                  String(args.timeout),
                  "--env-var",
                  `baseUrl=${args.baseUrl}`,
                  "--reporters",
                  "cli,json",
                  "--reporter-json-export",
                  path.join(runDir, "newman-raw.json")
              ];

    console.log("Running Newman...");
    const proc = spawnSync(newmanBin, newmanArgs, {
        cwd: ROOT,
        encoding: "utf8",
        maxBuffer: 64 * 1024 * 1024
    });

    if (proc.stdout) process.stdout.write(proc.stdout);
    if (proc.stderr) process.stderr.write(proc.stderr);

    const rawPath = path.join(runDir, "newman-raw.json");
    if (!fs.existsSync(rawPath)) {
        console.error("Newman did not produce newman-raw.json");
        process.exit(proc.status || 1);
    }

    const raw = JSON.parse(fs.readFileSync(rawPath, "utf8"));
    const executions = (((raw || {}).run || {}).executions) || [];

    const out = fs.createWriteStream(activeJsonl, { flags: "a" });
    let wrote = 0;

    for (let i = 0; i < executions.length; i++) {
        const ex = executions[i];
        const data = slice[i] || {};
        const bodyText =
            ex && ex.response && ex.response.stream
                ? Buffer.from(ex.response.stream).toString("utf8")
                : ex && ex.response && ex.response.body
                  ? String(ex.response.body)
                  : "";

        let parsed = null;
        let error = null;
        try {
            parsed = bodyText ? JSON.parse(bodyText) : null;
        } catch (e) {
            error = `invalid_json: ${e.message}`;
        }

        const actualLabel = parsed ? parsed.label : null;
        const actualReason = parsed ? parsed.reason : null;
        const confidence = parsed ? parsed.confidence : null;

        let status = "ERROR";
        let mismatch_type = error || "request_or_parse_error";
        if (parsed) {
            ({ status, mismatch_type } = classifyStatus(
                data.expected_label,
                actualLabel,
                data.expected_reason,
                actualReason
            ));
        }

        const row = {
            runId: path.basename(path.dirname(activeJsonl)) || runId,
            index: startIndex + i,
            id: data.id,
            comment: data.comment,
            category: data.category || null,
            subcategory: data.subcategory || null,
            expected_label: data.expected_label,
            actual_label: actualLabel,
            expected_reason: data.expected_reason ?? null,
            actual_reason: actualReason ?? null,
            confidence,
            status,
            mismatch_type,
            http_status: ex && ex.response ? ex.response.code : null,
            duration_ms: ex && ex.response ? ex.response.responseTime : null,
            timestamp: new Date().toISOString(),
            error
        };

        out.write(JSON.stringify(row) + "\n");
        wrote += 1;
    }
    out.end();

    const allRows = readJsonl(activeJsonl);
    const summary = {
        runFile: activeJsonl,
        updatedAt: new Date().toISOString(),
        ...summarize(allRows),
        // keep failures compact for quick review
        failures: allRows
            .filter((r) => r.status !== "PASS")
            .map((r) => ({
                id: r.id,
                status: r.status,
                mismatch_type: r.mismatch_type,
                confidence: r.confidence,
                expected_label: r.expected_label,
                actual_label: r.actual_label,
                expected_reason: r.expected_reason,
                actual_reason: r.actual_reason,
                comment: r.comment
            }))
    };

    // Write summary beside the active jsonl
    const activeSummary = path.join(
        path.dirname(activeJsonl),
        "summary.json"
    );
    fs.writeFileSync(activeSummary, JSON.stringify(summary, null, 2), "utf8");
    fs.writeFileSync(summaryPath, JSON.stringify(summary, null, 2), "utf8");

    const nextIndex = startIndex + wrote;
    const checkpoint = {
        data: args.data,
        collection: args.collection,
        jsonlPath: activeJsonl,
        nextIndex,
        updatedAt: new Date().toISOString(),
        done: nextIndex >= dataset.length
    };
    fs.writeFileSync(checkpointPath, JSON.stringify(checkpoint, null, 2), "utf8");

    const index = loadJson(indexPath, []);
    index.push({
        runId,
        at: new Date().toISOString(),
        jsonl: activeJsonl,
        summary: activeSummary,
        wrote,
        startIndex,
        nextIndex,
        accuracy_strict_pct: summary.accuracy_strict_pct,
        false_accept: summary.FALSE_ACCEPT,
        false_reject: summary.FALSE_REJECT
    });
    fs.writeFileSync(indexPath, JSON.stringify(index, null, 2), "utf8");

    console.log("\nSaved:");
    console.log("  jsonl   :", activeJsonl);
    console.log("  summary :", activeSummary);
    console.log("  index   :", indexPath);
    console.log("Summary:", {
        total: summary.total,
        PASS: summary.PASS,
        FALSE_ACCEPT: summary.FALSE_ACCEPT,
        FALSE_REJECT: summary.FALSE_REJECT,
        REASON_MISMATCH: summary.REASON_MISMATCH,
        ACCURACY_STRICT_PCT: summary.accuracy_strict_pct
    });

    const hasCritical =
        (summary.FALSE_ACCEPT || 0) +
            (summary.FALSE_REJECT || 0) +
            (summary.ERROR || 0) >
        0;
    process.exit(hasCritical ? 2 : 0);
}

main();
