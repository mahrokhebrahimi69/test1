# Authentication QA Regression Postman Collection

This repository contains a copyable Postman collection for **Master Authentication Truth Matrix v2**.

## Collection

- `postman/auth-business-scenarios.postman_collection.json`

The collection is organized by **business scenario** instead of endpoint. Each `TC-xx` folder is self-contained and intentionally repeats requests such as OTP, Login, Get Me, Refresh, and Smart Address where needed for QA and regression runs.

## Configure before running

Set these collection variables in Postman:

- `baseUrl`
- `phone`
- `otpCode` when the OTP is not returned by the API
- `legacyAccessToken` for legacy-session regression
- `ssoCode` if SSO endpoints become available

Every request includes a Tests script with an assertion and a console message showing which scenario checkpoint passed.
