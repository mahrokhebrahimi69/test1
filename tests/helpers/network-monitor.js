const { expect } = require('@playwright/test');

const TARGET_ENDPOINTS = {
  getMe: /\/Profile\/get-me(?:\?|$)/i,
  smartAddresses: /\/Address\/smart-addresses(?:\?|$)/i
};

function endpointNameForUrl(url, endpointMatchers = TARGET_ENDPOINTS) {
  return Object.entries(endpointMatchers).find(([, matcher]) => matcher.test(url))?.[0] || null;
}

function normalizeUrlForRetryCount(rawUrl) {
  try {
    const url = new URL(rawUrl);
    return `${url.origin}${url.pathname}`;
  } catch {
    return rawUrl.split('?')[0];
  }
}

function createResponseMonitor(page, options = {}) {
  const {
    endpointMatchers = TARGET_ENDPOINTS,
    log = console.log
  } = options;

  const responses = [];
  const responsesByEndpoint = Object.fromEntries(
    Object.keys(endpointMatchers).map((endpointName) => [endpointName, []])
  );

  const onResponse = (response) => {
    const url = response.url();
    const endpointName = endpointNameForUrl(url, endpointMatchers);

    if (!endpointName) {
      return;
    }

    const entry = {
      endpointName,
      method: response.request().method(),
      status: response.status(),
      url
    };

    responses.push(entry);
    responsesByEndpoint[endpointName].push(entry);

    log(`[api-monitor] ${entry.method} ${entry.status} ${entry.url}`);

    if (entry.status === 200) {
      log(`[api-monitor] detected 200 OK for ${endpointName}`);
    }

    if (entry.status === 401) {
      log(`[api-monitor] detected 401 Unauthorized for ${endpointName}`);
    }
  };

  page.on('response', onResponse);

  return {
    responses,
    responsesByEndpoint,
    stop: () => page.off('response', onResponse),
    getResponses: (endpointName) => responsesByEndpoint[endpointName] || [],
    getStatusResponses: (status) => responses.filter((response) => response.status === status),
    summary: () => responses.map((response) => `${response.method} ${response.status} ${response.url}`)
  };
}

function waitForMonitoredResponse(page, options = {}) {
  const {
    endpointName,
    endpointMatchers = TARGET_ENDPOINTS,
    status,
    timeout = 30 * 1000
  } = options;

  return page.waitForResponse((response) => {
    const matchedEndpointName = endpointNameForUrl(response.url(), endpointMatchers);

    if (!matchedEndpointName) {
      return false;
    }

    if (endpointName && matchedEndpointName !== endpointName) {
      return false;
    }

    return status === undefined || response.status() === status;
  }, { timeout });
}

function assertNoUnexpected401(monitor, options = {}) {
  const { allowedEndpointNames = [] } = options;
  const unexpected401 = monitor.responses.filter((response) => (
    response.status === 401 && !allowedEndpointNames.includes(response.endpointName)
  ));

  expect(unexpected401, `Unexpected 401 responses:\n${JSON.stringify(unexpected401, null, 2)}`).toEqual([]);
}

function assertHasStatus(monitor, endpointName, status) {
  const matchingResponses = monitor
    .getResponses(endpointName)
    .filter((response) => response.status === status);

  expect(
    matchingResponses.length,
    `Expected ${endpointName} to include status ${status}. Captured responses:\n${monitor.summary().join('\n')}`
  ).toBeGreaterThan(0);
}

function assertApiRetryLimits(monitor, options = {}) {
  const {
    maxResponsesPerEndpoint = 5,
    maxResponsesPerUrl = 4
  } = options;

  for (const [endpointName, responses] of Object.entries(monitor.responsesByEndpoint)) {
    expect(
      responses.length,
      `Excessive API retries for ${endpointName}:\n${responses.map((response) => `${response.method} ${response.status} ${response.url}`).join('\n')}`
    ).toBeLessThanOrEqual(maxResponsesPerEndpoint);
  }

  const responsesByMethodAndUrl = new Map();

  for (const response of monitor.responses) {
    const retryKey = `${response.method} ${normalizeUrlForRetryCount(response.url)}`;
    responsesByMethodAndUrl.set(retryKey, (responsesByMethodAndUrl.get(retryKey) || 0) + 1);
  }

  for (const [retryKey, count] of responsesByMethodAndUrl) {
    expect(count, `Excessive API retries for ${retryKey}`).toBeLessThanOrEqual(maxResponsesPerUrl);
  }
}

module.exports = {
  TARGET_ENDPOINTS,
  assertApiRetryLimits,
  assertHasStatus,
  assertNoUnexpected401,
  createResponseMonitor,
  endpointNameForUrl,
  waitForMonitoredResponse
};
