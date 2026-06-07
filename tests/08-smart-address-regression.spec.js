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

test.use({
  storageState: 'auth.json',
  permissions: ['geolocation'],
  geolocation: {
    latitude: 35.7547,
    longitude: 51.4116
  }
});

test('08 - smart-address regression: expired access token does not log out valid session', async ({ page }) => {
  const monitor = createResponseMonitor(page);
  const navigationGuard = createNavigationGuard(page);

  try {
    // Home page loading with geolocation should exercise /Address/smart-addresses.
    await page.goto('/');
    await waitForPageToSettle(page);
    await assertUserRemainsLoggedIn(page);

    await waitForTokenExpiryWindow(page, 'access token', ACCESS_TOKEN_EXPIRY_MS);

    const smartAddressOkResponse = waitForMonitoredResponse(page, {
      endpointName: 'smartAddresses',
      status: 200,
      timeout: 45 * 1000
    });

    await page.reload({ waitUntil: 'domcontentloaded' });
    await smartAddressOkResponse;
    await waitForPageToSettle(page);

    assertHasStatus(monitor, 'smartAddresses', 200);
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
