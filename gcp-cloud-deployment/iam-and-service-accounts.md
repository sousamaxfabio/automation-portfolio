# IAM, Service Accounts and Secrets

## Human identity and workload identity

The deployment separates two identity types:

- **Human identity:** used interactively to configure the project and deploy resources.
- **Workload identity:** `stage5-fastapi-runtime`, attached to the Cloud Run service.

The application does not use a downloaded service-account JSON key. Cloud Run supplies short-lived credentials to the attached service account automatically.

## Least-privilege permissions

The runtime identity received only the permissions needed for each task:

- `roles/secretmanager.secretAccessor` on `stage5-api-key`
- `roles/secretmanager.secretAccessor` on the temporary database-password secret
- `roles/cloudsql.client` during the temporary Cloud SQL exercise

The database secret and Cloud SQL Client role were removed when Cloud SQL was deleted. The API-key permission remains because the Cloud Run service still uses that secret.

## Two security layers

The service uses two independent controls:

1. **Cloud Run IAM** — blocks anonymous callers at the platform boundary.
2. **Application API key** — protects FastAPI's `/requests` endpoints after the caller passes Cloud Run IAM.

The observed results were:

- Anonymous `/health`: HTTP `403`
- Authenticated `/health`: HTTP `200`
- Authenticated `/requests` without the correct API key: HTTP `401`
- Authenticated `/requests` with the correct API key: HTTP `200`

## Safe secret handling

- Secret values were generated in Cloud Shell and piped directly into Secret Manager.
- Values were never added to source code, Docker images, documentation, or Git.
- Cloud Run configurations reference secret names and versions, not values.
- Secret lengths were checked with `wc -c`, which revealed an invisible trailing newline without exposing either secret.
- Corrected versions were created with `printf`, and Cloud Run was pinned to explicit version `2`.

## Database authorization

The temporary database used a restricted PostgreSQL user named `stage5_app`. It received:

- `USAGE` on the `public` schema
- `SELECT` and `INSERT` on `customers` and `requests`
- `USAGE` and `SELECT` on sequences

It did not receive database-administrator, table-deletion, or schema-creation permissions.
