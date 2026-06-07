const { test } = require('@playwright/test');
const { assertUserRemainsLoggedIn } = require('./helpers/auth-assertions');
const {
  assertApiRetryLimits,
  assertHasStatus,
  assertNoUnexpected401,
  createResponseMonitor,
  waitForMonitoredResponse
} = require('./helpers/network-monitor');
const { createNavigationGuard, waitForPageToSettle } = require('./helpers/session-guards');
const { ACCESS_TOKEN_EXPIRY_MS, waitForTokenExpiryWindow } = require('./helpers/token-timing');

test.use({ storageState: 'auth.json' });

test('05 - access token expired: reload refreshes session and keeps user logged in', async ({ page }) => {
  const monitor = createResponseMonitor(page);
  const navigationGuard = createNavigationGuard(page);

  try {
    // Start with the authenticated session created by 01-save-session.spec.js.
    await page.goto('/');
    await waitForPageToSettle(page);
    await assertUserRemainsLoggedIn(page);

    // Access token expires before the refresh token, so reload should trigger automatic token refresh.
    await waitForTokenExpiryWindow(page, 'access token', ACCESS_TOKEN_EXPIRY_MS);

    const getMeOkResponse = waitForMonitoredResponse(page, {
      endpointName: 'getMe',
      status: 200,
      timeout: 45 * 1000
    });

    await page.reload({ waitUntil: 'domcontentloaded' });
    await getMeOkResponse;
    await waitForPageToSettle(page);

    assertHasStatus(monitor, 'getMe', 200);
    assertNoUnexpected401(monitor);
    await assertUserRemainsLoggedIn(page);
    navigationGuard.assertNoInfiniteReloadLoop();
    navigationGuard.assertNoRepeatedRedirects({ maxAuthRedirects: 0 });
    assertApiRetryLimits(monitor);
  } finally {
    monitor.stop();
    navigationGuard.stop();
  }
});
