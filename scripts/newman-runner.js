#!/usr/bin/env node
'use strict';

/**
 * Newman runner for Comment Moderation QA
 *
 * Features:
 * - Append each result immediately to results/results.jsonl (low memory)
 * - Checkpoint after every request (resume after crash/stop)
 * - New runs do NOT clear previous results (append only)
 * - Graceful shutdown on SIGINT/SIGTERM
 *
 * Usage:
 *   node scripts/newman-runner.js
 *   node scripts/newman-runner.js --data data/dataset.json
 *   node scripts/newman-runner.js --delay 300
 *   node scripts/newman-runner.js --fresh              # restart from index 0, keep results file
 *   node scripts/newman-runner.js --fresh --clear-results
 */

const fs = require('fs');
const path = require('path');
const newman = require('newman');

const ROOT = path.resolve(__dirname, '..');
const DEFAULTS = {
  collection: path.join(ROOT, 'collections', 'Comment_Moderation_QA.postman_collection.json'),
  data: path.join(ROOT, 'data', 'dataset.json'),
  results: path.join(ROOT, 'results', 'results.jsonl'),
  checkpoint: path.join(ROOT, 'results', 'checkpoint.json'),
  lock: path.join(ROOT, 'results', '.runner.lock'),
  folder: 'Moderate Runner',
  delay: 200,
  timeout: 30000,
};

function parseArgs(argv) {
  const args = {
    fresh: false,
    clearResults: false,
    collection: DEFAULTS.collection,
    data: DEFAULTS.data,
    results: DEFAULTS.results,
    checkpoint: DEFAULTS.checkpoint,
    folder: DEFAULTS.folder,
    delay: DEFAULTS.delay,
    timeout: DEFAULTS.timeout,
  };

  for (let i = 0; i < argv.length; i++) {
    const arg = argv[i];
    switch (arg) {
      case '--fresh':
        args.fresh = true;
        break;
      case '--clear-results':
        args.clearResults = true;
        break;
      case '--data':
        args.data = path.resolve(argv[++i]);
        break;
      case '--collection':
        args.collection = path.resolve(argv[++i]);
        break;
      case '--results':
        args.results = path.resolve(argv[++i]);
        break;
      case '--checkpoint':
        args.checkpoint = path.resolve(argv[++i]);
        break;
      case '--folder':
        args.folder = argv[++i];
        break;
      case '--delay':
        args.delay = Number(argv[++i]);
        break;
      case '--timeout':
        args.timeout = Number(argv[++i]);
        break;
      case '--help':
      case '-h':
        printHelp();
        process.exit(0);
        break;
      default:
        console.error(`Unknown argument: ${arg}`);
        printHelp();
        process.exit(1);
    }
  }

  return args;
}

function printHelp() {
  console.log(`
Comment Moderation QA - Newman Runner

Options:
  --data <file>         JSON or CSV data file (default: data/dataset.json)
  --collection <file>   Postman collection (default: collections/...)
  --results <file>      Output JSONL file (default: results/results.jsonl)
  --checkpoint <file>   Checkpoint file (default: results/checkpoint.json)
  --folder <name>       Folder/request name in collection (default: Moderate Runner)
  --delay <ms>          Delay between requests (default: 200)
  --timeout <ms>        Request timeout (default: 30000)
  --fresh               Restart from first record (does NOT clear results unless --clear-results)
  --clear-results       Truncate results file before run
  -h, --help            Show this help
`);
}

function ensureDir(filePath) {
  fs.mkdirSync(path.dirname(filePath), { recursive: true });
}

function readJson(filePath, fallback) {
  if (!fs.existsSync(filePath)) return fallback;
  return JSON.parse(fs.readFileSync(filePath, 'utf8'));
}

function writeJson(filePath, data) {
  ensureDir(filePath);
  fs.writeFileSync(filePath, JSON.stringify(data, null, 2), 'utf8');
}

function loadDataset(filePath) {
  if (!fs.existsSync(filePath)) {
    throw new Error(`Data file not found: ${filePath}`);
  }

  if (filePath.endsWith('.csv')) {
    const text = fs.readFileSync(filePath, 'utf8');
    const lines = text.split(/\r?\n/).filter((line) => line.trim() !== '');
    const header = lines[0].split(',').map((h) => h.trim().replace(/^"|"$/g, ''));
    const commentIndex = header.indexOf('comment');
    if (commentIndex === -1) {
      throw new Error('CSV must have a "comment" column header');
    }
    return lines.slice(1).map((line) => {
      const value = line.trim().replace(/^"|"$/g, '');
      return { comment: value };
    });
  }

  const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));
  if (!Array.isArray(data)) {
    throw new Error('JSON data file must be an array of objects');
  }
  return data;
}

function acquireLock(lockPath) {
  ensureDir(lockPath);
  if (fs.existsSync(lockPath)) {
    const existing = readJson(lockPath, null);
    throw new Error(
      `Another runner appears active (lock: ${lockPath}, pid: ${existing?.pid ?? 'unknown'}). ` +
        'Remove the lock file only if no runner is running.'
    );
  }
  const lock = { pid: process.pid, startedAt: new Date().toISOString() };
  fs.writeFileSync(lockPath, JSON.stringify(lock, null, 2), 'utf8');
  return lockPath;
}

function releaseLock(lockPath) {
  if (fs.existsSync(lockPath)) {
    fs.unlinkSync(lockPath);
  }
}

function appendResult(filePath, record) {
  ensureDir(filePath);
  fs.appendFileSync(filePath, `${JSON.stringify(record)}\n`, 'utf8');
}

function parseResponseBody(response) {
  if (!response) return null;

  try {
    if (typeof response.json === 'function') {
      return response.json();
    }
  } catch (_) {
    // fall through to text
  }

  try {
    if (typeof response.text === 'function') {
      return response.text();
    }
  } catch (_) {
    // fall through
  }

  if (response.stream) {
    const text = response.stream.toString('utf8');
    try {
      return JSON.parse(text);
    } catch (_) {
      return text;
    }
  }

  return null;
}

function buildRunId() {
  return new Date().toISOString().replace(/[:.]/g, '-');
}

function main() {
  const args = parseArgs(process.argv.slice(2));
  const lockPath = DEFAULTS.lock;

  ensureDir(args.results);
  ensureDir(args.checkpoint);

  if (args.clearResults && fs.existsSync(args.results)) {
    fs.unlinkSync(args.results);
    console.log(`Cleared results file: ${args.results}`);
  }

  const dataset = loadDataset(args.data);
  if (dataset.length === 0) {
    console.log('Dataset is empty. Nothing to run.');
    process.exit(0);
  }

  let checkpoint = {
    dataFile: path.resolve(args.data),
    lastCompletedIndex: -1,
    totalProcessed: 0,
    totalInDataset: dataset.length,
    lastUpdated: null,
    lastRunId: null,
  };

  if (!args.fresh && fs.existsSync(args.checkpoint)) {
    const saved = readJson(args.checkpoint, checkpoint);
    if (path.resolve(saved.dataFile || '') === path.resolve(args.data)) {
      checkpoint = { ...checkpoint, ...saved };
    } else {
      console.log('Checkpoint data file differs; starting from index 0.');
      checkpoint.lastCompletedIndex = -1;
    }
  } else if (args.fresh) {
    checkpoint.lastCompletedIndex = -1;
    checkpoint.totalProcessed = 0;
    console.log('Fresh run: checkpoint reset to index 0 (results file preserved unless --clear-results).');
  }

  const startIndex = checkpoint.lastCompletedIndex + 1;
  if (startIndex >= dataset.length) {
    console.log(`All ${dataset.length} records already processed.`);
    console.log(`Results: ${args.results}`);
    console.log('Use --fresh to rerun from the beginning (append mode) or --fresh --clear-results to reset.');
    process.exit(0);
  }

  const remaining = dataset.slice(startIndex);
  const tempDataFile = path.join(path.dirname(args.checkpoint), '.temp-data.json');
  fs.writeFileSync(tempDataFile, JSON.stringify(remaining), 'utf8');

  const runId = buildRunId();
  let shuttingDown = false;
  let lastSavedIndex = checkpoint.lastCompletedIndex;

  acquireLock(lockPath);

  const saveCheckpoint = (index) => {
    const cp = {
      dataFile: path.resolve(args.data),
      lastCompletedIndex: index,
      totalProcessed: index + 1,
      totalInDataset: dataset.length,
      lastUpdated: new Date().toISOString(),
      lastRunId: runId,
    };
    writeJson(args.checkpoint, cp);
    lastSavedIndex = index;
  };

  const onSignal = (signal) => {
    if (shuttingDown) return;
    shuttingDown = true;
    console.log(`\nReceived ${signal}. Checkpoint is at index ${lastSavedIndex}. Exiting safely...`);
    releaseLock(lockPath);
    try {
      if (fs.existsSync(tempDataFile)) fs.unlinkSync(tempDataFile);
    } catch (_) {}
    process.exit(130);
  };

  process.on('SIGINT', onSignal);
  process.on('SIGTERM', onSignal);

  console.log('Comment Moderation QA - Newman Runner');
  console.log(`Run ID:        ${runId}`);
  console.log(`Collection:    ${args.collection}`);
  console.log(`Data file:     ${args.data}`);
  console.log(`Results file:  ${args.results}`);
  console.log(`Checkpoint:    ${args.checkpoint}`);
  console.log(`Range:         ${startIndex + 1}-${dataset.length} of ${dataset.length}`);
  console.log(`Delay:         ${args.delay}ms`);
  console.log('');

  const collection = JSON.parse(fs.readFileSync(args.collection, 'utf8'));

  const runner = newman.run(
    {
      collection,
      iterationData: tempDataFile,
      folder: args.folder,
      delayRequest: args.delay,
      timeoutRequest: args.timeout,
      reporters: ['cli'],
      insecure: false,
      bail: false,
    },
    (err, summary) => {
      releaseLock(lockPath);
      try {
        if (fs.existsSync(tempDataFile)) fs.unlinkSync(tempDataFile);
      } catch (_) {}

      if (err) {
        console.error('Newman run failed:', err.message);
        process.exit(1);
      }

      const failed = summary?.run?.failures?.length || 0;
      console.log('');
      console.log(`Done. Processed in this session: ${remaining.length}`);
      console.log(`Failures: ${failed}`);
      console.log(`Results appended to: ${args.results}`);
      console.log(`Checkpoint: index ${lastSavedIndex} (${lastSavedIndex + 1}/${dataset.length})`);

      process.exit(failed > 0 ? 1 : 0);
    }
  );

  runner.on('request', (_err, data) => {
    const localIteration = data?.cursor?.iteration ?? 0;
    const globalIndex = startIndex + localIteration;
    const row = dataset[globalIndex] || {};
    const comment = row.comment || '';

    const response = data?.response;
    const status = response?.code ?? 0;
    const responseBody = parseResponseBody(response);
    const requestError = _err ? String(_err.message || _err) : null;

    const record = {
      runId,
      index: globalIndex,
      comment,
      status,
      response: requestError ? null : responseBody,
      error: requestError,
      durationMs: response?.responseTime ?? null,
      timestamp: new Date().toISOString(),
    };

    appendResult(args.results, record);
    saveCheckpoint(globalIndex);

    const preview = comment.length > 50 ? `${comment.slice(0, 50)}...` : comment;
    console.log(`[saved ${globalIndex + 1}/${dataset.length}] status=${status} comment="${preview}"`);
  });
}

try {
  main();
} catch (error) {
  console.error(error.message);
  process.exit(1);
}
