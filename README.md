# Authentication QA Regression Postman Collection

This repository contains a copyable Postman collection for **Master Authentication Truth Matrix v2**.

## Files

- `postman/auth-business-scenarios.postman_collection.json`
- `postman/auth-business-scenarios.postman_environment.json`

Import both files into Postman. Set `baseUrl`, `phone`, and any real OTP/legacy/SSO values before running against a real API.

## Folder / Scenario List

- `TC-01_Guest_Token_Creation` - Guest token is issued
- `TC-02_OTP_Request` - OTP is returned or request is accepted
- `TC-03_Login_Success` - Access and refresh tokens are issued
- `TC-04_Save_Session` - Tokens and expiry variables are saved
- `TC-05_Check_Session_Get_Me` - 200 with user data
- `TC-06_Session_Persist_API_Level` - Session remains valid across repeated API calls
- `TC-07_Smart_Address_Load` - 200 with smart-address data
- `TC-08_Access_Token_Expired_Refresh_Trigger` - 401 triggers refresh and retry succeeds
- `TC-09_Smart_Address_After_Expiry` - SmartAddress recovers after refresh
- `TC-10_Multiple_Access_Expiry_Handling` - Session survives multiple expiry checks
- `TC-11_Long_Session_Stability` - Unexpected logout does not occur
- `TC-12_Refresh_During_API_Call` - No false logout while refresh happens during API call
- `TC-13_Refresh_Token_Expired` - Refresh returns 401
- `TC-14_Refresh_API_Failure` - Refresh failure is handled gracefully
- `TC-15_Re_Login_Flow` - Re-login succeeds after auth failure
- `TC-16_Login_Modal_Trigger` - Frontend login modal should be shown
- `TC-17_Session_Recovery_After_Login` - Session is fully recovered after login
- `TC-18_API_401_Handling` - Refresh is attempted before logout
- `TC-19_Get_Me_401_Regression` - False logout does not occur for GetMe 401
- `TC-20_Smart_Address_401_Regression` - False logout does not occur for SmartAddress 401
- `TC-21_Multiple_401_Responses` - Cascade logout does not occur
- `TC-22_Single_Refresh_Lock` - Only one refresh should be in flight
- `TC-23_Refresh_Retry_Logic` - Refresh retry is controlled
- `TC-24_Guest_After_Logout` - Guest token is recreated after logout
- `TC-25_Guest_To_Customer_Migration` - Guest session upgrades to customer session
- `TC-26_Logout_Cleanup` - Tokens are cleaned after logout
- `TC-27_Multi_Tab_Session` - Session sync across browser tabs
- `TC-28_Multi_Device_Login` - Device sessions remain isolated
- `TC-29_Missing_Access_Token` - GetMe returns 401
- `TC-30_Missing_Refresh_Token` - Refresh fails without refresh token
- `TC-31_Corrupted_Access_Token` - GetMe returns 401
- `TC-32_Corrupted_Refresh_Token` - Refresh fails with corrupted token
- `TC-33_Browser_Restart` - Session remains after restart if variables persist
- `TC-34_Parallel_Requests_Race` - Double logout does not occur
- `TC-35_Refresh_Storm` - Refresh storm collapses to single refresh lock
- `TC-36_Legacy_Session` - Legacy token remains valid
- `TC-37_Token_Format_Migration` - Token format remains backward compatible
- `TC-38_SSO_Login` - SSO login succeeds when APIs exist
- `TC-39_SSO_Sync_Logout` - SSO logout sync behaves correctly
- `TC-40_Release_Regression_Full` - No unexpected logout in full regression flow
- `TC-41_Incident_Replay` - Custom incident path can be replayed
- `TC-42_Idle_Session_Expiry` - Idle session expires and request logs out
- `TC-43_Long_Session_Stability_TTL` - Session stays stable through TTL refreshes
- `TC-44_Smart_Address_Recovery` - SmartAddress retry succeeds after refresh
- `TC-45_Get_Me_Recovery` - GetMe retry succeeds after refresh
- `TC-46_Invalid_OTP` - Login fails with invalid OTP
- `TC-47_Invalid_Login_Payload` - Login validation returns 400 or 422
- `TC-48_Invalid_Refresh_Token` - Refresh returns 401
- `TC-49_API_Latency_Spike` - Latency does not cause false logout
- `TC-50_Full_Auth_Lifecycle` - Login refresh and logout lifecycle works
- `TC-51_Access_Expire_Before_Idle` - Access refresh succeeds before idle timeout
- `TC-52_Refresh_Token_Expire` - Refresh returns 401 after refresh TTL
- `TC-53_Access_And_Refresh_Expire_Together` - Refresh fails and logout is expected
- `TC-54_Idle_Timeout_Enforcement` - Idle rule ends session
- `TC-55_Refresh_At_Expiration_Boundary` - Refresh succeeds near expiration boundary
- `TC-56_Refresh_After_Expiration_Boundary` - Refresh returns 401 after boundary
- `TC-57_GetMe_Immediately_After_Access_Expiry` - GetMe refreshes or returns 401 without looping
- `TC-58_SmartAddress_Immediately_After_Access_Expiry` - SmartAddress refreshes or returns 401 without looping
- `TC-59_Idle_Timeout_After_Successful_Refresh` - Idle timeout is preserved after refresh
- `TC-60_Refresh_Loop_Detection` - Refresh loop does not occur

## Required Environment Variables

- `baseUrl` = `https://api.example.com`
- `phone` = `+989120000000`
- `otpCode` = ``
- `guestToken` = ``
- `accessToken` = ``
- `refreshToken` = ``
- `tokenExpireTime` = `0`
- `refreshExpireTime` = `0`
- `idleExpireTime` = `0`
- `logChain` = ``
- `accessTTL` = `300000`
- `refreshTTL` = `300000`
- `idleTTL` = `600000`
- `legacyAccessToken` = ``
- `invalidAccessToken` = `invalid-access-token-for-negative-tests`
- `invalidRefreshToken` = `invalid-refresh-token-for-negative-tests`
- `ssoCode` = ``
- `refreshLock` = `false`
- `refreshAttemptCount` = `0`
- `retryAttemptCount` = `0`
- `forceAccessExpired` = `false`
- `forceRefreshExpired` = `false`
- `forceIdleExpired` = `false`
- `lastAuthScenario` = ``

## Default TTLs

- Access token TTL: `accessTTL=300000` ms = 5 minutes
- Refresh token TTL: `refreshTTL=300000` ms = 5 minutes
- Idle session TTL: `idleTTL=600000` ms = 10 minutes

The scripts also accept suffixes such as `5m`, `300s`, or `300000ms` for TTL variables.

## Request Sequence Notes

- Login requests save `accessToken`, `refreshToken`, `tokenExpireTime`, `refreshExpireTime`, and `idleExpireTime`.
- Simulated wait requests update expiry variables instead of requiring a real wall-clock wait.
- Protected requests set the `Authorization` header from the environment and use expiry variables to simulate expired access or idle state.
- When a protected request receives `401` or `403` and refresh is allowed for that scenario, Tests scripts call `/auth/refresh` with `pm.sendRequest`, update tokens, and retry the protected API.
- `refreshLock`, `refreshAttemptCount`, and `retryAttemptCount` are used by TC-22, TC-34, TC-35, and refresh/retry flows to prevent duplicate refresh attempts.
- `logChain` accumulates pass/fail/warn events for QA debugging.

## Special Handling

- TC-16, TC-27, TC-28, TC-38, and TC-39 include manual or placeholder requests because UI, multi-tab/device, or missing SSO APIs cannot be fully verified by a normal Postman request alone.
- TC-34 and TC-35 use `pm.sendRequest` to simulate parallel requests and refresh storms inside Postman.
- Endpoint paths are conventional placeholders (`/auth/login`, `/auth/me`, `/auth/refresh`, `/smart-address`). Adjust paths and payload shapes if the target API contract differs.

## Auth Debug Framework v3 Collection

Additional collection generated from the provided **Auth Debug Framework v2 (Auto Refresh + Race + Logger)** plus the prior TC-01 to TC-60 truth matrix.

### Files

- `postman/auth-debug-framework-v3-truth-matrix.postman_collection.json`
- `postman/auth-debug-framework-v3.postman_environment.json`

### Endpoint conventions

- OTP: `{baseUrl}/v1/api/Authentication/otp`
- Login/token: `{baseUrl}/v1/api/Authentication/token`
- Refresh: `{cookieBaseUrl}/v1/api/Authentication/refresh`
- GetMe: `{baseUrl}/v1/api/Profile/get-me`
- SmartAddress: `{baseUrl}/v1/api/Address/smart-addresses?latitude={latitude}&longitude={longitude}`

### Variables from Debug Framework + Truth Matrix

- `baseUrl` = `https://api.foodstg.com`
- `cookieBaseUrl` = `https://cookie.foodstg.com`
- `cellPhone` = `09015649636`
- `phone` = `09015649636`
- `latitude` = `35.75`
- `longitude` = `51.41`
- `otpCode` = ``
- `guestToken` = ``
- `accessToken` = ``
- `refreshToken` = ``
- `tokenExpireTime` = `0`
- `refreshExpireTime` = `0`
- `idleExpireTime` = `0`
- `logChain` = ``
- `accessTTL` = `300000`
- `refreshTTL` = `300000`
- `idleTTL` = `600000`
- `legacyAccessToken` = ``
- `invalidAccessToken` = `invalid-access-token-for-negative-tests`
- `invalidRefreshToken` = `invalid-refresh-token-for-negative-tests`
- `ssoCode` = ``
- `refreshLock` = `false`
- `refreshAttemptCount` = `0`
- `retryAttemptCount` = `0`
- `raceRequestCount` = `0`
- `stormRequestCount` = `0`
- `forceAccessExpired` = `false`
- `forceRefreshExpired` = `false`
- `forceIdleExpired` = `false`
- `lastAuthScenario` = ``
- `lastFailureReason` = ``

### Scenario folders

- `TC-01_Guest_Token_Creation` - Guest token is issued
- `TC-02_OTP_Request` - OTP is returned and stored in otpCode
- `TC-03_Login_Success` - token and refreshToken are issued
- `TC-04_Save_Session` - token, refreshToken, and expiry variables are saved
- `TC-05_Check_Session_Get_Me` - GetMe returns 200 with user data
- `TC-06_Session_Persist_API_Level` - Session remains valid across repeated GetMe calls
- `TC-07_Smart_Address_Load` - SmartAddress returns 200 with data
- `TC-08_Access_Token_Expired_Refresh_Trigger` - GetMe 401 triggers refresh and retry
- `TC-09_Smart_Address_After_Expiry` - SmartAddress 401 triggers refresh and retry
- `TC-10_Multiple_Access_Expiry_Handling` - Repeated expired-access calls do not lose session
- `TC-11_Long_Session_Stability` - Unexpected logout does not occur
- `TC-12_Refresh_During_API_Call` - No false logout during refresh
- `TC-13_Refresh_Token_Expired` - Refresh returns 401 after refresh expiry
- `TC-14_Refresh_API_Failure` - Refresh failure is logged gracefully
- `TC-15_Re_Login_Flow` - Re-login succeeds after auth failure
- `TC-16_Login_Modal_Trigger` - Auth-required response is available for frontend modal
- `TC-17_Session_Recovery_After_Login` - Session is recovered after login
- `TC-18_API_401_Handling` - Refresh is attempted before logout
- `TC-19_Get_Me_401_Regression` - False logout does not occur for GetMe 401
- `TC-20_Smart_Address_401_Regression` - False logout does not occur for SmartAddress 401
- `TC-21_Multiple_401_Responses` - Cascade logout does not occur
- `TC-22_Single_Refresh_Lock` - Only one refresh is in flight
- `TC-23_Refresh_Retry_Logic` - Refresh retry count is controlled
- `TC-24_Guest_After_Logout` - Guest token is recreated after logout
- `TC-25_Guest_To_Customer_Migration` - Guest upgrades to customer session
- `TC-26_Logout_Cleanup` - Tokens are cleaned after logout
- `TC-27_Multi_Tab_Session` - Session sync across tabs is documented
- `TC-28_Multi_Device_Login` - Device sessions remain isolated
- `TC-29_Missing_Access_Token` - GetMe returns 401 without token
- `TC-30_Missing_Refresh_Token` - Refresh fails without refreshToken
- `TC-31_Corrupted_Access_Token` - GetMe returns 401 for corrupted token
- `TC-32_Corrupted_Refresh_Token` - Refresh fails with corrupted refreshToken
- `TC-33_Browser_Restart` - Session remains if environment variables persist
- `TC-34_Parallel_Requests_Race` - Double logout does not occur
- `TC-35_Refresh_Storm` - Refresh storm is controlled by refreshLock
- `TC-36_Legacy_Session` - Legacy token remains valid
- `TC-37_Token_Format_Migration` - token/refreshToken format remains compatible
- `TC-38_SSO_Login` - SSO succeeds when API contract exists
- `TC-39_SSO_Sync_Logout` - SSO logout sync is documented
- `TC-40_Release_Regression_Full` - No unexpected logout in full regression flow
- `TC-41_Incident_Replay` - Incident sequence is replayable
- `TC-42_Idle_Session_Expiry` - Idle session expires and request logs out
- `TC-43_Long_Session_Stability_TTL` - Session stays stable through TTL refreshes
- `TC-44_Smart_Address_Recovery` - SmartAddress retry succeeds after refresh
- `TC-45_Get_Me_Recovery` - GetMe retry succeeds after refresh
- `TC-46_Invalid_OTP` - Login fails with invalid OTP
- `TC-47_Invalid_Login_Payload` - Login validation returns 400 or 422
- `TC-48_Invalid_Refresh_Token` - Refresh returns 401
- `TC-49_API_Latency_Spike` - Latency does not cause false logout
- `TC-50_Full_Auth_Lifecycle` - Login refresh logout lifecycle works
- `TC-51_Access_Expire_Before_Idle` - Access refresh succeeds before idle timeout
- `TC-52_Refresh_Token_Expire` - Refresh returns 401 after refresh TTL
- `TC-53_Access_And_Refresh_Expire_Together` - Refresh fails and logout is expected
- `TC-54_Idle_Timeout_Enforcement` - Idle rule ends session
- `TC-55_Refresh_At_Expiration_Boundary` - Refresh succeeds near expiration boundary
- `TC-56_Refresh_After_Expiration_Boundary` - Refresh returns 401 after boundary
- `TC-57_GetMe_Immediately_After_Access_Expiry` - GetMe refreshes or returns 401 without loop
- `TC-58_SmartAddress_Immediately_After_Access_Expiry` - SmartAddress refreshes or returns 401 without loop
- `TC-59_Idle_Timeout_After_Successful_Refresh` - Idle timeout is preserved after refresh
- `TC-60_Refresh_Loop_Detection` - Refresh loop does not occur

### Debug behavior

- Every scenario starts with `00 - LOGGER INIT` and ends with `99 - FINAL REPORT`.
- Every request has Pre-request and Tests scripts.
- Tests log `[PASS]`, `[FAIL]`, `[WARN]`, `[LOCK]`, or `[REPORT]` messages to the Postman console.
- `logChain` records a chronological auth trace for each scenario.
- Login saves `token` into `accessToken` and `refreshToken` into `refreshToken`.
- Refresh uses the provided cookie service payload shape: `{ token, refreshToken }`.
- TTL simulation uses `tokenExpireTime`, `refreshExpireTime`, `idleExpireTime`, `accessTTL`, `refreshTTL`, and `idleTTL`.
- TC-22, TC-34, and TC-35 use `pm.sendRequest`, `refreshLock`, and request counters to simulate race and refresh storm behavior.
