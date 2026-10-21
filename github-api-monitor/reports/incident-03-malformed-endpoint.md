# Incident 03 — Malformed GitHub API Endpoint

**Date:** 2026-09-17  
**Status:** Resolved  
**HTTP status:** 404 Not Found

## Summary

An API request failed because the GitHub endpoint path was malformed.

## Impact

No repository data was returned. This was a controlled troubleshooting exercise and caused no production impact.

## Symptoms

- The request returned HTTP status 404.
- The request used `/userz/` instead of the valid `/users/` path.
- The failure was reproduced independently of the Python application.

## Investigation

The request was repeated with curl to isolate the problem from the application code. Curl returned the same HTTP 404 response, proving that the endpoint URL—not Python processing—caused the failure.

## Root cause

The API path contained a spelling mistake:

`/userz/sousamaxfabio/repos`

The correct path is:

`/users/sousamaxfabio/repos`

## Resolution

The endpoint path was corrected and the request was repeated. GitHub then returned HTTP status 200.

## Prevention

- Copy endpoints from official API documentation.
- Keep the API base URL in one configuration constant.
- Add automated tests for constructed URLs.
- Reproduce unexpected responses with curl before changing application logic.
- Record the request URL and HTTP status in diagnostic logs without exposing secrets.