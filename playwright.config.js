const { defineConfig, devices } = require('@playwright/test');

module.exports = defineConfig({
  testDir: './tests',
  fullyParallel: false,
  timeout: 7 * 60 * 1000,
  expect: {
    timeout: 15 * 1000
  },
  reporter: [['list']],
  use: {
    baseURL: process.env.PWA_BASE_URL || 'https://pwa.foodstg.com',
    screenshot: 'only-on-failure',
    trace: 'retain-on-failure',
    video: 'retain-on-failure'
  },
  projects: [
    {
      name: 'chromium',
      use: {
        ...devices['Desktop Chrome']
      }
    }
  ]
});
