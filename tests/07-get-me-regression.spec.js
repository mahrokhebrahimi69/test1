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

test('07 - get-me regression: expired access token does not log out valid session', async ({ page }) => {
  const monitor = createResponseMonitor(page);
  const navigationGuard = createNavigationGuard(page);

  try {
    // A profile route should exercise /Profile/get-me through the app's auth layer.
    await page.goto('/profile/edit');
    await waitForPageToSettle(page);
    await assertUserRemainsLoggedIn(page);

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
