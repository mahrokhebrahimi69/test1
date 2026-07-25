// ============================================================
// Postman Tests Script — Classification QA Report
// Data file: data/political_comment_dataset.flat.json
// (باید expected_label و expected_reason داشته باشد؛ comments.json کافی نیست)
// ============================================================

const json = pm.response.json();

// ---------- Expected (از Data File رانر) ----------
const expectedLabel = String(pm.iterationData.get("expected_label") || "").trim();
const rawExpectedReason = pm.iterationData.get("expected_reason");
const expectedReason =
    rawExpectedReason === null ||
    rawExpectedReason === undefined ||
    rawExpectedReason === "null"
        ? ""
        : String(rawExpectedReason).trim();

// ---------- Actual (از API) ----------
const actualLabel = String(json.label || "").trim();
const actualReason =
    json.reason === null || json.reason === undefined
        ? ""
        : String(json.reason).trim();
const confidence =
    json.confidence === null || json.confidence === undefined
        ? null
        : Number(json.confidence);

// ---------- تعیین وضعیت ----------
// FALSE_ACCEPT  = نباید می‌پذیرفت (expected disapproval → actual approval)
// FALSE_REJECT  = نباید رد می‌کرد   (expected approval    → actual disapproval)
// LABEL_MISMATCH / REASON_MISMATCH / PASS
let status = "PASS";
let mismatch_type = null;

if (expectedLabel && actualLabel && expectedLabel !== actualLabel) {
    if (expectedLabel === "disapproval" && actualLabel === "approval") {
        status = "FALSE_ACCEPT"; // false positive از دید پذیرش
        mismatch_type = "should_reject_but_approved";
    } else if (expectedLabel === "approval" && actualLabel === "disapproval") {
        status = "FALSE_REJECT"; // false negative از دید پذیرش
        mismatch_type = "should_approve_but_rejected";
    } else {
        status = "LABEL_MISMATCH";
        mismatch_type = `${expectedLabel}_to_${actualLabel}`;
    }
} else if (expectedLabel === actualLabel && expectedReason !== actualReason) {
    status = "REASON_MISMATCH";
    mismatch_type = "reason_only";
}

const reportItem = {
    id: pm.iterationData.get("id"),
    comment: pm.iterationData.get("comment"),
    category: pm.iterationData.get("category") || null,
    subcategory: pm.iterationData.get("subcategory") || null,

    expected_label: expectedLabel,
    actual_label: actualLabel,

    expected_reason: expectedReason || null,
    actual_reason: actualReason || null,

    confidence: confidence,
    status: status,
    mismatch_type: mismatch_type,
    http_status: pm.response.code,
    timestamp: new Date().toISOString()
};

// ---------- ذخیره تجمعی در Collection Variable ----------
let report = [];
const existing = pm.collectionVariables.get("classification_report");
if (existing) {
    try {
        report = JSON.parse(existing);
    } catch (e) {
        report = [];
    }
}
report.push(reportItem);
pm.collectionVariables.set("classification_report", JSON.stringify(report));

// خلاصه سبک برای کپی سریع
const failed = report.filter((x) => x.status !== "PASS");
const summary = {
    TOTAL_CASES: report.length,
    PASS: report.filter((x) => x.status === "PASS").length,
    FALSE_ACCEPT: report.filter((x) => x.status === "FALSE_ACCEPT").length,
    FALSE_REJECT: report.filter((x) => x.status === "FALSE_REJECT").length,
    LABEL_MISMATCH: report.filter((x) => x.status === "LABEL_MISMATCH").length,
    REASON_MISMATCH: report.filter((x) => x.status === "REASON_MISMATCH").length,
    ACCURACY_STRICT_PCT: (
        (report.filter((x) => x.status === "PASS").length / report.length) *
        100
    ).toFixed(2),
    // دقت فقط روی label (reason را نادیده می‌گیرد)
    ACCURACY_LABEL_ONLY_PCT: (
        (report.filter(
            (x) =>
                x.status === "PASS" || x.status === "REASON_MISMATCH"
        ).length /
            report.length) *
        100
    ).toFixed(2)
};
pm.collectionVariables.set("classification_summary", JSON.stringify(summary));
pm.collectionVariables.set(
    "classification_failures",
    JSON.stringify(failed)
);

// ---------- Assertions ----------
pm.test("HTTP 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Label matches expected", function () {
    pm.expect(actualLabel).to.eql(expectedLabel);
});

pm.test("Reason matches expected", function () {
    pm.expect(actualReason).to.eql(expectedReason);
});

pm.test("Confidence is a number between 0 and 1", function () {
    pm.expect(confidence).to.be.a("number");
    pm.expect(confidence).to.be.within(0, 1);
});

// ---------- لاگ ----------
console.log(reportItem);
console.log({
    ...summary,
    // فقط خطاها + confidence برای بررسی سریع
    FAILURES_WITH_CONFIDENCE: failed.map((x) => ({
        id: x.id,
        status: x.status,
        mismatch_type: x.mismatch_type,
        confidence: x.confidence,
        expected_label: x.expected_label,
        actual_label: x.actual_label,
        expected_reason: x.expected_reason,
        actual_reason: x.actual_reason,
        comment: x.comment
    }))
});
