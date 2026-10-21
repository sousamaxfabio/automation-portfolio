# OpenAPI Reference Notes

## API

GitHub REST API

## OpenAPI source

GitHub publishes a machine-readable OpenAPI description for its REST API:

- https://github.com/github/rest-api-description
- https://docs.github.com/en/rest

OpenAPI describes an API’s endpoints, methods, parameters, authentication requirements, request bodies, responses, and schemas in a standard format that can be read by both humans and software tools.

## Endpoint reviewed

**Operation:** List repositories for a user  
**Method:** `GET`  
**Path:** `/users/{username}/repos`

Reference:

https://docs.github.com/en/rest/repos/repos#list-repositories-for-a-user

## Parameters

### Path parameter

- `username` — required GitHub account handle.

### Query parameters

- `type` — limits the repository type.
- `sort` — selects the property used for sorting.
- `direction` — selects ascending or descending order.
- `per_page` — controls the number of results per page, with a maximum of 100.
- `page` — selects the page of results.

## Headers

- `Accept: application/vnd.github+json`
- `Authorization: Bearer <token>` when authenticated access is required.
- `X-GitHub-Api-Version` selects a GitHub REST API version.

Secrets must never be written directly into source code, documentation, logs, or committed configuration files.

## Responses

- `200 OK` — repositories returned successfully.
- `401 Unauthorized` — authentication is invalid or missing for a protected operation.
- `403 Forbidden` — permissions are insufficient or a rate limit has been reached.
- `404 Not Found` — the requested user or endpoint does not exist.

## Project implementation

The GitHub Repository Monitor:

- Constructs the endpoint using the configured username.
- Sends headers and query parameters.
- Supports optional bearer-token authentication.
- Handles pagination.
- Configures a request timeout.
- Retries temporary network and server failures using exponential backoff.
- Monitors rate-limit headers.
- Validates the response format.
- Transforms raw API objects into a smaller internal model.
- Saves cleaned results as JSON.
- Produces structured diagnostic logs.