const ACCESS_TOKEN_EXPIRY_MS = Number(process.env.ACCESS_TOKEN_EXPIRY_MS || 125 * 1000);
const REFRESH_TOKEN_EXPIRY_MS = Number(process.env.REFRESH_TOKEN_EXPIRY_MS || 305 * 1000);

async function waitForTokenExpiryWindow(page, label, waitMs) {
  console.log(`[token-timing] waiting ${waitMs}ms for ${label} expiry window`);
  await page.waitForTimeout(waitMs);
  console.log(`[token-timing] finished waiting for ${label} expiry window`);
}

module.exports = {
  ACCESS_TOKEN_EXPIRY_MS,
  REFRESH_TOKEN_EXPIRY_MS,
  waitForTokenExpiryWindow
};
