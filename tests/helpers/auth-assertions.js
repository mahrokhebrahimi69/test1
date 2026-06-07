const { expect } = require('@playwright/test');

const AUTH_URL_PATTERN = /\/auth(?:\/|$|\?)/i;
const LOGIN_TEXT_PATTERN = /ورود|ثبت(?:‌|\s|-)?نام|شماره(?:‌|\s|-)?(?:موبایل|همراه)|کد(?:‌|\s|-)?تایید|login|sign(?:\s|-)?in|otp|phone/i;

function loginModalLocator(page) {
  return page
    .getByRole('dialog')
    .filter({ hasText: LOGIN_TEXT_PATTERN })
    .first()
    .or(page.locator('form').filter({ hasText: LOGIN_TEXT_PATTERN }).first())
    .or(page.getByText(LOGIN_TEXT_PATTERN).first());
}

async function assertUserRemainsLoggedIn(page) {
  await expect(page, 'User should not be redirected to auth while refresh token is still valid')
    .not.toHaveURL(AUTH_URL_PATTERN);
  await expect(loginModalLocator(page), 'Login modal should stay hidden while refresh token is valid')
    .toBeHidden();
}

async function assertLoginModalAppears(page) {
  await expect(async () => {
    const currentUrl = page.url();
    const authUrlVisible = AUTH_URL_PATTERN.test(currentUrl);
    const loginUiVisible = await loginModalLocator(page).isVisible().catch(() => false);

    expect(
      authUrlVisible || loginUiVisible,
      `Expected auth URL or login modal. Current URL: ${currentUrl}`
    ).toBeTruthy();
  }).toPass({ timeout: 30 * 1000 });

  await expect(loginModalLocator(page), 'Login modal should be visible after refresh token expires')
    .toBeVisible();
}

module.exports = {
  AUTH_URL_PATTERN,
  LOGIN_TEXT_PATTERN,
  assertLoginModalAppears,
  assertUserRemainsLoggedIn,
  loginModalLocator
};
