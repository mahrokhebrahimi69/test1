# Tapsi Food Authentication & Session Regression Pack

This directory contains a Postman regression pack for Tapsi Food authentication, guest sessions, customer sessions, token refresh, logout fallback, legacy-release regressions, SSO placeholders, multi-tab behavior, storage/cookie resilience, concurrency, and end-to-end lifecycle coverage.

## Files

- `tapsi_food_auth_session_regression.postman_collection.json` - Postman Collection v2.1.
- `tapsi_food_auth_session_regression.postman_environment.json` - Staging environment variables.
- `README.md` - Usage notes and scenario map.

## Scope

- **TC-01 to TC-60 are mandatory regression scenarios.**
- **TC-61 to TC-70 are extended regression/load/e2e scenarios.**
- The collection includes all scenarios from **TC-01 to TC-70**.

## Default target

- `baseUrl`: `https://api.foodstg.com`
- `cookieBaseUrl`: `https://cookie.foodstg.com`
- `pwaBaseUrl`: `https://pwa.foodstg.com`

Production cURL examples were used only as reference. No production token, real OTP, or real user token is stored in the collection.

## Required environment variables

### Core

- `baseUrl`
- `cookieBaseUrl`
- `pwaBaseUrl`
- `guestToken`
- `accessToken`
- `refreshToken`
- `tokenExpireTime`
- `refreshExpireTime`
- `idleExpireTime`
- `logChain`

### Dynamic TTL

- `accessTTL` default `300000` ms / 5 minutes
- `refreshTTL` default `300000` ms / 5 minutes
- `idleTTL` default `600000` ms / 10 minutes

Override these values in the Postman environment to simulate shorter or longer token/session windows.

### User/session

- `otpCode`
- `userId`
- `cellPhone`
- `platform`
- `appVersion`
- `usw`
- `usid`
- `deviceHash`
- `latitude`
- `longitude`
- `userAgent`

### Concurrency and refresh-lock

- `refreshLock`
- `refreshInProgress`
- `refreshAttemptCount`
- `lastRefreshAt`
- `parallelRequestCount`
- `refreshStormDetected`

## Token saving behavior

- Guest token responses save `guestToken` when a token-like field exists.
- Login responses save `accessToken`, `refreshToken`, `userId`, `tokenExpireTime`, `refreshExpireTime`, and `idleExpireTime`.
- Refresh responses update `accessToken`, update `refreshToken` when returned, reset expiry times, and clear `refreshLock` / `refreshInProgress`.
- Logout fallback requests clear `accessToken`, `refreshToken`, and `userId`, then related scenarios request a new guest token.

## Refresh and retry logic

Protected `Get Me` and `Smart Address` requests accept either a direct success or a `401` that triggers refresh handling. On `401`, the Tests script uses `pm.sendRequest` to call:

```http
POST {{cookieBaseUrl}}/v1/api/Authentication/refresh
```

If refresh succeeds, the script retries the original protected request and logs the retry status.

## Refresh storm protection

Concurrency scenarios use:

- `refreshInProgress`
- `refreshLock`
- `refreshAttemptCount`
- `parallelRequestCount`
- `refreshStormDetected`

The refresh-storm requests simulate multiple workers and assert that duplicate refresh attempts are locked.

## OTP handling

The staging token endpoint requires a valid OTP. Set these before running login-dependent folders:

- `cellPhone`
- `otpCode`

If the OTP API returns a test OTP/code, the collection attempts to save it automatically. Otherwise, keep `otpCode` manually populated in the environment.

## SSO placeholders

SSO endpoints were not provided. TC-42 to TC-48 are included as visible, non-blocking placeholder requests against the PWA auth page. Replace them with real SSO endpoints when available:

- TC-42 SSO Login
- TC-43 Existing SSO Session
- TC-44 Expired SSO Session
- TC-45 SSO ReAuthentication
- TC-46 SSO Logout Sync
- TC-47 Food Logout Sync
- TC-48 SSO Token Refresh

## Logout fallback behavior

A real logout endpoint was not provided. Logout scenarios use a fallback:

1. Clear `accessToken`, `refreshToken`, and `userId`.
2. Call Guest Token again.
3. Save `guestToken` if returned.

This matches the observed behavior where `guest-token` was called during logout.

## Legacy release regression notes

The pack covers the previous release bug where legacy logged-in users had invalid sessions after deployment, login modal was not shown, a refresh loop occurred, `Get Me` was not called, and the profile appeared empty. TC-36 to TC-41 and TC-69/TC-70 seed invalid legacy tokens and verify that recovery/login-modal paths are visible instead of silently looping.

## Scenario map

### Authentication & Session
- TC-01 Guest Token Creation (Mandatory)
- TC-02 Save Session (Mandatory)
- TC-03 Check Session (Mandatory)
- TC-04 Session Persist (Mandatory)
- TC-05 Profile Recovery (Mandatory)
- TC-06 Smart Address Load (Mandatory)

### Access Token Lifecycle
- TC-07 Access Token Refresh (Mandatory)
- TC-08 Get Me After Access Expire (Mandatory)
- TC-09 Smart Address After Access Expire (Mandatory)
- TC-10 Multiple Access Expirations (Mandatory)
- TC-11 Active User Long Session (Mandatory)
- TC-12 Browser Refresh During Access Expire (Mandatory)

### Refresh Token Lifecycle
- TC-13 Refresh Token Expired (Mandatory)
- TC-14 Refresh API Failure (Mandatory)
- TC-15 Re-Login Flow (Mandatory)
- TC-16 Login Modal Display (Mandatory)
- TC-17 Session Recovery After Login (Mandatory)

### 401 Handling
- TC-18 API 401 Handling (Mandatory)
- TC-19 Get Me 401 Regression (Mandatory)
- TC-20 Smart Address 401 Regression (Mandatory)
- TC-21 Multiple 401 Responses (Mandatory)
- TC-22 Single Refresh Lock (Mandatory)
- TC-23 Refresh Retry Logic (Mandatory)

### Guest User Flow
- TC-24 Guest Token Creation (Mandatory)
- TC-25 Guest To Customer Migration (Mandatory)
- TC-26 Customer To Guest Migration (Mandatory)
- TC-27 Guest Token After Logout (Mandatory)
- TC-28 Guest Token After Session End (Mandatory)
- TC-29 Guest Restricted Get Me (Mandatory)
- TC-30 Guest Restricted Profile APIs (Mandatory)

### Logout Flow
- TC-31 Manual Logout (Mandatory)
- TC-32 Logout Cleanup (Mandatory)
- TC-33 Logout To Guest (Mandatory)
- TC-34 Logout From Multiple Tabs (Mandatory)
- TC-35 Logout During Refresh (Mandatory)

### Legacy Users & Release Regression
- TC-36 Legacy Session User (Mandatory)
- TC-37 Legacy Session Expired (Mandatory)
- TC-38 Legacy Session ReLogin (Mandatory)
- TC-39 Session Recovery After Deploy (Mandatory)
- TC-40 Cookie Migration (Mandatory)
- TC-41 Token Format Migration (Mandatory)

### SSO Integration
- TC-42 SSO Login (Mandatory)
- TC-43 Existing SSO Session (Mandatory)
- TC-44 Expired SSO Session (Mandatory)
- TC-45 SSO ReAuthentication (Mandatory)
- TC-46 SSO Logout Sync (Mandatory)
- TC-47 Food Logout Sync (Mandatory)
- TC-48 SSO Token Refresh (Mandatory)

### Multi Device & Multi Tab
- TC-49 Multi Tab Session (Mandatory)
- TC-50 Multi Tab Refresh (Mandatory)
- TC-51 Multi Device Login (Mandatory)
- TC-52 Logout One Device (Mandatory)
- TC-53 Session Isolation (Mandatory)

### Storage & Cookie Resilience
- TC-54 Missing Access Token (Mandatory)
- TC-55 Missing Refresh Token (Mandatory)
- TC-56 Corrupted Access Token (Mandatory)
- TC-57 Corrupted Refresh Token (Mandatory)
- TC-58 Cleared Local Storage (Mandatory)
- TC-59 Cleared Cookies (Mandatory)
- TC-60 Browser Restart (Mandatory)

### High Load & Concurrency
- TC-61 Parallel Requests During Expiration (Extended)
- TC-62 Refresh Storm Protection (Extended)
- TC-63 Multiple Get Me Calls (Extended)
- TC-64 Multiple Smart Address Calls (Extended)
- TC-65 Session Stability Under Load (Extended)

### End-to-End Business Flows
- TC-66 Complete Authentication Flow (Extended)
- TC-67 Long Running User Journey (Extended)
- TC-68 Idle User Journey (Extended)
- TC-69 Release Day Regression (Extended)
- TC-70 Production Incident Regression (Extended)

## How to run with Postman Collection Runner

1. Import both JSON files into Postman.
2. Select environment `Tapsi Food Auth Session Regression - Staging`.
3. Set `cellPhone` and `otpCode` for login-dependent tests.
4. Run the full collection or an individual parent folder.
5. Review Tests output and Postman Console logs.

## How to run with Newman

```bash
newman run postman/tapsi_food_auth_session_regression.postman_collection.json \
  -e postman/tapsi_food_auth_session_regression.postman_environment.json \
  --env-var cellPhone=09xxxxxxxxx \
  --env-var otpCode=00000
```

## Source cURL references

The following examples were used as source-of-truth references for paths, headers, request bodies, and observed behavior. Sensitive values are represented as variables.

### Guest Token, also observed during logout flow

```bash
curl 'https://api.tapsi.food/v1/api/Authentication/guest-token' \
  -X 'POST' \
  -H 'x-platform: desktop' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'Referer: https://tapsi.food/' \
  -H 'sec-ch-ua: "Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"' \
  -H 'X-Usw: 679' \
  -H 'sec-ch-ua-cellPhone: ?0' \
  -H 'X-Usid: {{usid}}' \
  -H 'x-app-version: {{appVersion}}' \
  -H 'x-d-sx94k: {{deviceHash}}' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'DNT: 1' \
  -H 'User-Agent: {{userAgent}}'
```

### Refresh

```bash
curl -X 'POST' \
  'https://cookie.foodstg.com/v1/api/Authentication/refresh' \
  -H 'accept: text/plain' \
  -H 'Content-Type: application/json' \
  -d '{
  "refreshToken": "{{refreshToken}}",
  "token": "{{accessToken}}"
}'
```

Observed invalid refresh response:

```json
{
  "status": false,
  "message": "Invalid token",
  "token": null,
  "refreshToken": null,
  "newUser": true,
  "userId": ""
}
```

Expected successful refresh schema:

```json
{
  "status": true,
  "message": "string",
  "token": "string",
  "refreshToken": "string",
  "newUser": true,
  "userId": "string"
}
```

### Login page asset

```bash
curl 'https://pwa.foodstg.com/static/assets/lotties/login.json' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'Referer: https://pwa.foodstg.com/auth' \
  -H 'User-Agent: {{userAgent}}' \
  -H 'sec-ch-ua: "Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"' \
  -H 'DNT: 1' \
  -H 'sec-ch-ua-cellPhone: ?0'
```

### Send OTP

```bash
curl 'https://api.foodstg.com/v1/api/Authentication/otp' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'authorization: Bearer {{guestToken}}' \
  -H 'content-type: application/json' \
  -H 'origin: https://pwa.foodstg.com' \
  -H 'referer: https://pwa.foodstg.com/' \
  -H 'user-agent: {{userAgent}}' \
  -H 'x-app-version: {{appVersion}}' \
  -H 'x-d-sx94k: {{deviceHash}}' \
  -H 'x-platform: {{platform}}' \
  -H 'x-usid: {{usid}}' \
  -H 'x-usw: {{usw}}' \
  --data-raw '{"cellPhone":"{{cellPhone}}"}'
```

### Login / Token

```bash
curl 'https://api.foodstg.com/v1/api/Authentication/token' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'authorization: Bearer {{guestToken}}' \
  -H 'content-type: application/json' \
  -H 'origin: https://pwa.foodstg.com' \
  -H 'referer: https://pwa.foodstg.com/' \
  -H 'user-agent: {{userAgent}}' \
  -H 'x-app-version: {{appVersion}}' \
  -H 'x-d-sx94k: {{deviceHash}}' \
  -H 'x-platform: {{platform}}' \
  -H 'x-usid: {{usid}}' \
  -H 'x-usw: {{usw}}' \
  --data-raw '{"cellPhone":"{{cellPhone}}","otpCode":"{{otpCode}}"}'
```

### Get Me

```bash
curl 'https://api.foodstg.com/v1/api/Profile/get-me' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'authorization: Bearer {{accessToken}}' \
  -H 'origin: https://pwa.foodstg.com' \
  -H 'referer: https://pwa.foodstg.com/' \
  -H 'user-agent: {{userAgent}}' \
  -H 'x-app-version: {{appVersion}}' \
  -H 'x-d-sx94k: {{deviceHash}}' \
  -H 'x-platform: {{platform}}' \
  -H 'x-usid: {{usid}}' \
  -H 'x-usw: {{usw}}'
```

### Smart Address

```bash
curl 'https://api.foodstg.com/v1/api/Address/smart-addresses?latitude={{latitude}}&longitude={{longitude}}' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'authorization: Bearer {{accessToken}}' \
  -H 'origin: https://pwa.foodstg.com' \
  -H 'referer: https://pwa.foodstg.com/' \
  -H 'user-agent: {{userAgent}}' \
  -H 'x-app-version: {{appVersion}}' \
  -H 'x-d-sx94k: {{deviceHash}}' \
  -H 'x-platform: {{platform}}' \
  -H 'x-usid: {{usid}}' \
  -H 'x-usw: {{usw}}'
```

## Known assumptions / endpoints needing confirmation

- Real logout endpoint was not provided, so logout is simulated by clearing tokens and requesting guest token.
- SSO endpoints were not provided, so TC-42 to TC-48 are placeholders.
- Some expiry scenarios simulate client-side TTL by setting expiry variables. For backend-enforced expiry, configure staging token TTLs accordingly.
- Login-dependent tests require a valid OTP or a staging test OTP.

## Latest import note

The Enterprise collection now keeps sample browser/device headers as literal values in the Headers tab, matching the provided cURLs. Authentication bootstrap endpoints use literal `https://api.foodstg.com` URLs, while Refresh and Logout use literal `https://cookie.foodstg.com` URLs. Only Authorization token values remain variable because they are generated during the run.

## Variable and header strategy

The collection keeps only runtime/state values as variables: base URLs, `cellPhone`, OTP, generated tokens, coordinates, TTL/expiry values, and refresh-lock state. Fixed browser/device headers stay as literal sample values in the Headers tab to keep requests close to the provided cURLs without adding unnecessary variable noise.

## Login bootstrap order

The observed PWA flow calls the login lottie asset before OTP and token requests:

```text
GET {{pwaBaseUrl}}/static/assets/lotties/login.json
POST {{baseApiUrl}}/v1/api/Authentication/otp
POST {{baseApiUrl}}/v1/api/Authentication/token
```

The login asset request uses the fixed sample `Referer` value `https://pwa.foodstg.com/auth?path:redirect-url=/?smart-address-fallback-modal=true` and is inserted before OTP flows.

## OTP variable requirement

The Login/Token request sends `"otpCode": "{{otpCode}}"`. The backend returns a validation error when `otpCode` is empty. The collection now blocks Login/Token before sending if `otpCode` is not set, with a clear pre-request error. After running OTP, copy the current SMS/STG OTP into the runtime variable `otpCode` and then run Token/Login.

## OTP response mapping

The staging OTP API can return the OTP in `response.message`, for example `{ "status": true, "message": "32638" }`. The OTP request tests now save numeric `message` values into `otpCode` and `lastOtpCode`. Login/Token also accepts a literal `otpCode` typed directly in the body, but keeping `{{otpCode}}` is recommended for collection runs.
