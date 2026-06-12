# Tapsi Food QA Final Auth Session Regression - 21 TC

This is the focused QA Lead collection for the final authentication/session regression pack.

## Final base URLs

- Authentication bootstrap APIs used by latest working cURLs: `{{baseApiUrl}}` = `https://api.foodstg.com`
- Refresh / Logout APIs: `{{baseCookieUrl}}` = `https://cookie.foodstg.com`
- Business APIs: `{{baseApiUrl}}` = `https://api.foodstg.com`

## Collection variables

The collection stores all runtime values as collection variables:

- `baseCookieUrl`
- `baseApiUrl`
- `cellPhone`
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


## Header values

The request Headers tab keeps the same fixed browser/device values from the provided sample cURLs:

- `User-Agent`: Chrome 149 Windows user agent
- `sec-ch-ua`: `"Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"`
- `x-platform`: `desktop`
- `x-app-version`: empty value, matching `x-app-version;` in the sample cURL
- `X-Usw`: `682`
- `X-Usid`: `gtjdcnagu9amqamd2do`
- `x-d-sx94k`: `a9e2269d5b8e836d4962db133aadf7f375f75af147ea03170913694de4a84ff8`

Only `Authorization` keeps token variables such as `Bearer {{guestToken}}` and `Bearer {{accessToken}}`, because those tokens are generated and refreshed during the collection run.

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
2. Set `cellPhone` and `otpCode` before login if OTP is not returned by STG.
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
  --env-var cellPhone=09015649636
```

## APIs used

Authentication bootstrap APIs on API base:

- `POST {{baseApiUrl}}/v1/api/Authentication/guest-token`
- `POST {{baseApiUrl}}/v1/api/Authentication/otp`
- `POST {{baseApiUrl}}/v1/api/Authentication/token`

Refresh / Logout APIs on cookie base:

- `POST {{baseCookieUrl}}/v1/api/Authentication/refresh`
- `POST {{baseCookieUrl}}/v1/api/Authentication/logout`

Business APIs on API base:

- `GET /v1/api/Profile/get-me`
- `GET /v1/api/Address/smart-addresses?latitude={{latitude}}&longitude={{longitude}}`

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
