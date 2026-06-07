const { expect } = require('@playwright/test');

function createNavigationGuard(page) {
  const mainFrameNavigations = [];
  const authRedirects = [];

  const onFrameNavigated = (frame) => {
    if (frame !== page.mainFrame()) {
      return;
    }

    const url = frame.url();
    mainFrameNavigations.push(url);
    console.log(`[navigation-guard] ${url}`);

    try {
      const parsedUrl = new URL(url);

      if (/\/auth(?:\/|$)/i.test(parsedUrl.pathname)) {
        authRedirects.push(url);
        console.log(`[navigation-guard] auth redirect detected: ${url}`);
      }
    } catch {
      // Ignore browser-internal URLs such as about:blank.
    }
  };

  page.on('framenavigated', onFrameNavigated);

  return {
    mainFrameNavigations,
    authRedirects,
    stop: () => page.off('framenavigated', onFrameNavigated),
    assertNoInfiniteReloadLoop: (options = {}) => {
      const { maxMainFrameNavigations = 6 } = options;

      expect(
        mainFrameNavigations.length,
        `Possible infinite reload loop. Main-frame navigations:\n${mainFrameNavigations.join('\n')}`
      ).toBeLessThanOrEqual(maxMainFrameNavigations);
    },
    assertNoRepeatedRedirects: (options = {}) => {
      const { maxAuthRedirects = 2 } = options;

      expect(
        authRedirects.length,
        `Repeated auth redirects detected:\n${authRedirects.join('\n')}`
      ).toBeLessThanOrEqual(maxAuthRedirects);
    }
  };
}

async function waitForPageToSettle(page, options = {}) {
  const { networkIdleTimeout = 10 * 1000 } = options;

  await page.waitForLoadState('domcontentloaded');

  try {
    await page.waitForLoadState('networkidle', { timeout: networkIdleTimeout });
  } catch {
    console.log('[navigation-guard] networkidle was not reached; continuing after domcontentloaded');
  }
}

module.exports = {
  createNavigationGuard,
  waitForPageToSettle
};
