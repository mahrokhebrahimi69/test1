# Tapsi Food QA Final Auth Session Regression - 21 TC

This is the focused QA Lead collection for the final authentication/session regression pack.

## Final base URLs

- Authentication APIs: `{{baseCookieUrl}}` = `https://cookie.foodstg.com`
- Business APIs: `{{baseApiUrl}}` = `https://api.foodstg.com`

## Collection variables

The collection stores all runtime values as collection variables:

- `baseCookieUrl`
- `baseApiUrl`
- `mobile`
- `latitude`
- `longitude`
- `guestToken`
- `accessToken`
- `refreshToken`
- `otpCode`
- `invalidAccessToken`
- `invalidRefreshToken`
- `expiredAccessToken`
- `expiredRefreshToken`
- `refreshInProgress`
- `refreshCount`
- `enableRealAccessExpiryWait`
- `enableRealIdleWait`

## Folders and test cases

1. `01 - Guest Session`
   - TC-01 Guest Token
2. `02 - Authentication`
   - TC-02 OTP Request
   - TC-03 Login Success
3. `03 - Authenticated APIs`
   - TC-04 Get Me
   - TC-05 Smart Address
4. `04 - Refresh Flow`
   - TC-06 Refresh Token
   - TC-07 Get Me After Refresh
   - TC-08 Smart Address After Refresh
5. `05 - Negative Authentication`
   - TC-09 Missing Access Token
   - TC-10 Missing Refresh Token
   - TC-11 Invalid Access Token
   - TC-12 Invalid Refresh Token
6. `06 - Session Expiration`
   - TC-13 Access Token Expired
   - TC-14 Refresh Token Expired
   - TC-15 Idle Session Expired
7. `07 - Regression`
   - TC-16 GetMe 401 -> Refresh -> GetMe 200
   - TC-17 SmartAddress 401 -> Refresh -> SmartAddress 200
   - TC-18 Multiple 401 Requests
   - TC-19 Single Refresh Lock
   - TC-20 No Refresh Loop
8. `08 - Logout`
   - TC-21 Logout Flow

## Execution notes

1. Import `tapsi_food_qa_final_21tc.postman_collection.json` into Postman.
2. Set `mobile` and `otpCode` before login if OTP is not returned by STG.
3. Run folders in order for the full lifecycle.
4. For real expiry validation:
   - Set access token TTL in STG to 60 seconds.
   - Set `enableRealAccessExpiryWait=true` to wait `accessExpiryWaitMs=70000` before expiry-dependent requests.
   - Set `enableRealIdleWait=true` to wait `idleWaitMs=150000` for idle timeout checks.
5. Keep these wait flags `false` for faster CI smoke runs.

## Main regression target

The critical bug flow is covered by TC-16 and TC-17:

```text
Logged-in user
-> Access token expires
-> GetMe or SmartAddress returns 401
-> Refresh API returns new token
-> Original request retries
-> Original request returns 200
```

If refresh fails, the expected product behavior is:

```text
Refresh fails
-> Logout/session cleanup
-> Guest token
-> Login modal
```

## Newman example

```bash
newman run postman/tapsi_food_qa_final_21tc.postman_collection.json \
  --env-var otpCode=12345 \
  --env-var mobile=09015649636
```

## APIs used

Authentication APIs on cookie base:

- `POST /v1/api/Authentication/guest-token`
- `POST /v1/api/Authentication/otp`
- `POST /v1/api/Authentication/token`
- `POST /v1/api/Authentication/refresh`
- `POST /v1/api/Authentication/logout`

Business APIs on API base:

- `GET /v1/api/Profile/get-me`
- `GET /v1/api/Address/smart-addresses?latitude={{latitude}}&longitude={{longitude}}`
