const { expect, test } = require('@playwright/test');
const { assertLoginModalAppears } = require('./helpers/auth-assertions');
const {
  assertApiRetryLimits,
  assertHasStatus,
  createResponseMonitor,
  endpointNameForUrl,
  waitForMonitoredResponse
} = require('./helpers/network-monitor');
const { createNavigationGuard, waitForPageToSettle } = require('./helpers/session-guards');
const { REFRESH_TOKEN_EXPIRY_MS, waitForTokenExpiryWindow } = require('./helpers/token-timing');

test.use({ storageState: 'auth.json' });

test('06 - refresh token expired: reload redirects to login without loops', async ({ page }) => {
  const monitor = createResponseMonitor(page);
  const navigationGuard = createNavigationGuard(page);

  try {
    // Start authenticated, then wait beyond the refresh-token lifetime.
    await page.goto('/');
    await waitForPageToSettle(page);
    await waitForTokenExpiryWindow(page, 'refresh token', REFRESH_TOKEN_EXPIRY_MS);

    const unauthorizedResponse = waitForMonitoredResponse(page, {
      status: 401,
      timeout: 45 * 1000
    }).catch(() => null);

    await page.reload({ waitUntil: 'domcontentloaded' });
    await waitForPageToSettle(page);

    const response = await unauthorizedResponse;

    expect(
      response,
      `Expected get-me or smart-addresses to return 401 after refresh token expiry. Captured responses:\n${monitor.summary().join('\n')}`
    ).not.toBeNull();

    const unauthorizedEndpointName = endpointNameForUrl(response.url());

    assertHasStatus(monitor, unauthorizedEndpointName, 401);
    await assertLoginModalAppears(page);
    navigationGuard.assertNoInfiniteReloadLoop();
    navigationGuard.assertNoRepeatedRedirects({ maxAuthRedirects: 2 });
    assertApiRetryLimits(monitor, {
      maxResponsesPerEndpoint: 6,
      maxResponsesPerUrl: 5
    });
  } finally {
    monitor.stop();
    navigationGuard.stop();
  }
});
