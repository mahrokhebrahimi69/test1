# SSO / SuperApp Completed Postman Collection

This collection is based on the uploaded `SSO_b273.json` and has been completed with new scenarios marked by `★`.

## New marked sections

- `★ 09 - Keycloak TTL Validation`
  - `★ KC-01 Access Before 70s Must Still Work`
  - `★ KC-02 Access After 70s Must Refresh And Retry`
  - `★ KC-03 Refresh Before 130s Must Work`
  - `★ KC-04 Refresh After 130s Must Fail`
  - `★ KC-05 Idle After 190s Must Require Login`
  - `★ KC-06 Active User Should Not Idle Timeout`
- `★ 10 - SSO / SuperApp Direct No401`
  - Requires a real `superAppAccessToken`.
  - Fails clearly if `superAppAccessToken` is missing.
- `★ 11 - End To End Authentication Validation SuperApp Direct No401`
  - Validates direct SuperApp token path against GetMe and SmartAddress without 401.

## Timing values

The collection variables were aligned with the requested test timing:

- `accessTTL = 70000`
- `refreshTTL = 130000`
- `idleTTL = 190000`
- `accessExpiryWaitMs = 70000`
- `refreshExpiryWaitMs = 130000`
- `idleWaitMs = 190000`

The new Keycloak TTL tests fail with explicit messages when behavior does not match these timings.

## Important run notes

1. Run `00 - Reset Runtime State` first.
2. Run login/bootstrap to get fresh tokens.
3. For SSO/SuperApp direct tests, set:
   - `superAppAccessToken`
   - optionally `expiredSuperAppAccessToken`
   - `superAppSource`
4. `★ KC-04 Refresh After 130s Must Fail` should be run from a fresh login token pair. If another refresh rotates the refresh token before this test, the expected timing may shift.
5. `★ KC-05 Idle After 190s Must Require Login` can be affected by background activity. Run it without intermediate API calls.

## Simulation / limitations

- True browser-level parallel traffic is still not possible in Postman alone.
- Existing simulation-only cases remain marked as such.
- SSO endpoint-level validation requires real SuperApp/SSO token inputs because no dedicated SSO login endpoint was provided in the uploaded collection.
