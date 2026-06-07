# Playwright session persistence tests

This repository contains Playwright JavaScript tests for token refresh and session persistence checks against the staging PWA.

## Running

1. Generate an authenticated `auth.json` session with the existing login flow.
2. Run the regression suite:

```bash
npm test
```

Useful environment overrides:

- `PWA_BASE_URL` - defaults to `https://pwa.foodstg.com`
- `ACCESS_TOKEN_EXPIRY_MS` - defaults to `125000`
- `REFRESH_TOKEN_EXPIRY_MS` - defaults to `305000`

`auth.json` is intentionally gitignored because it contains session state.
