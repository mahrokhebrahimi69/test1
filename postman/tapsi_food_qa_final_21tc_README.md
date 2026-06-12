# Tapsi Food Strict Login / Session / Refresh Regression Pack - 21 TC

This is the final QA regression collection for the login/session/refresh scope. It intentionally excludes the old 70-TC enterprise truth matrix from the download bundle.

## Import this file

- `tapsi_food_qa_final_21tc.postman_collection.json`
- Optional environment: `tapsi_food_auth_session_regression.postman_environment.json`

## Runtime strategy

- URL, token, OTP, coordinates, TTL, and refresh-lock state stay dynamic.
- Fixed browser/device headers stay literal in the Headers tab, matching the provided cURLs.
- Run `00 - Reset Runtime State / Clear Runtime Variables` first if Postman reuses stale Collection, Environment, or Global variables.

## State-transition folders

1. `01 - Authentication Bootstrap`
   - TC-01 Guest Token
   - TC-02 OTP Request (`GET Login Asset` then `POST OTP Request`)
   - TC-03 Login Token
2. `02 - Session Validation`
   - TC-04 Get Me
   - TC-05 Smart Address
3. `03 - Refresh Flow`
   - TC-06 Refresh Token
   - TC-07 Get Me After Refresh
   - TC-08 Smart Address After Refresh
4. `04 - Negative Cases`
   - TC-09 Missing Access Token
   - TC-10 Missing Refresh Token
   - TC-11 Invalid Access Token
5. `05 - Regression Bugs`
   - TC-12 GetMe 401 -> Refresh -> Retry GetMe 200
   - TC-13 SmartAddress 401 -> Refresh -> Retry SmartAddress 200
   - TC-14 Multiple 401 Requests - Simulation Only
   - TC-15 Single Refresh Lock - Simulation Only
   - TC-16 API 401 Handling: 401 -> Refresh Fail -> Guest Token/Login Flow
6. `06 - Session Expiration`
   - TC-17 Refresh Token Expired
   - TC-18 Idle Session Timeout
   - TC-19 Active User Session
7. `07 - Logout Flow`
   - TC-20 Logout API And Guest Token
   - TC-21 Get Me As Guest

## Critical regression flow

TC-12 and TC-13 implement the core bug chain:

```text
Protected API with expired/invalid access token
-> 401/403
-> Refresh API
-> Save new access/refresh token
-> Retry original request
-> 200
```

By default these use `expiredAccessToken` to force the first 401. To validate real token expiry, set:

```text
enableRealAccessExpiryWait = true
accessExpiryWaitMs = 70000
```

## Idle session

TC-18 uses simulated idle expiry by default. To run the real Keycloak idle wait, set:

```text
enableRealIdleWait = true
idleWaitMs = 130000
```

## Simulation-only scenarios

TC-14 and TC-15 are marked `Simulation Only` because Postman cannot generate true browser-level parallel traffic. Use Playwright/k6/JMeter for real concurrency.

## OTP handling

The staging OTP API may return:

```json
{ "status": true, "message": "32638" }
```

The OTP request saves numeric `message` into `otpCode` and `lastOtpCode`. Login also accepts a literal `otpCode` typed directly into the body.
