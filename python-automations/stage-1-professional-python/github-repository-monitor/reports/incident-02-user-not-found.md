# Incident 02 — GitHub User Not Found

**Date:** 2026-09-15  
**Status:** Resolved  
**HTTP status:** 404 Not Found

## Summary

The GitHub Repository Monitor could not retrieve repositories because the configured GitHub username did not exist.

## Impact

No repository data was returned. This was a controlled test and caused no production impact.

## Symptoms

- Bearer-token authentication was loaded successfully.
- GitHub returned HTTP status 404.
- The application displayed a clear message identifying the username that could not be found.
- The application exited without producing a long traceback.

## Root cause

A temporary `GITHUB_USERNAME` environment variable contained an intentionally nonexistent username. This value overrode the username stored in `.env`.

## Resolution

The temporary environment variable was removed. The program then used the valid username from `.env`, and the next request returned HTTP status 200.

## Prevention

- Validate configuration before running API requests.
- Distinguish resource-not-found errors from authentication failures.
- Include the affected username in diagnostic messages, but never include secrets.
- Test configuration changes in a controlled environment.