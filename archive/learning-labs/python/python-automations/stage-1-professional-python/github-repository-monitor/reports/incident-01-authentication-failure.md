# Incident 01 — GitHub API Authentication Failure

**Date:** 2026-09-15  
**Status:** Resolved  
**HTTP status:** 401 Unauthorized

## Summary

The GitHub Repository Monitor could not retrieve repository data because the bearer token supplied to the API was invalid.

## Impact

The API request failed and no repository data was returned. This was a controlled test and caused no production impact.

## Symptoms

- The application confirmed that bearer authentication was enabled.
- GitHub returned HTTP status 401.
- The application displayed: `Authentication failed: check the GitHub token`.
- No secret value was printed.

## Root cause

A temporary `GITHUB_TOKEN` environment variable contained an intentionally invalid token. This temporary value took precedence over the valid token stored in the local `.env` file.

## Resolution

The temporary environment variable was removed. The application then loaded the valid token from `.env`, and the next request returned HTTP status 200.

## Prevention

- Keep tokens outside the source code.
- Exclude `.env` from Git commits.
- Use fine-grained tokens with minimal permissions and an expiration date.
- Return a specific diagnostic message for HTTP 401 responses.
- Never print token values in logs or error messages.