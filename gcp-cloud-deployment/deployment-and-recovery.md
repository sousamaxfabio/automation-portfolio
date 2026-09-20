# Deployment and Recovery Guide

## Prerequisites

- A dedicated Google Cloud project
- Billing budget and alerts configured before deployment
- Google account protected with multifactor authentication
- Google Cloud Shell authorized for the project
- Cloud Run, Cloud Build, Artifact Registry, and Secret Manager APIs enabled

## Container requirements

Cloud Run supplies the listening port through the `PORT` environment variable. The Dockerfile therefore starts Uvicorn with:

```dockerfile
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8080}"]
```

The fallback port supports local testing, while Cloud Run can set its required value.

Before deployment, the image was built and tested locally in Cloud Shell:

```bash
docker build -t stage5-fastapi-local .
```

```bash
docker run --rm -d --name stage5-fastapi-test -p 8080:8080 -e PORT=8080 stage5-fastapi-local
```

```bash
curl http://localhost:8080/health
```

## Cloud Run deployment controls

The service was deployed with these controls:

- private access (`--no-allow-unauthenticated`)
- dedicated runtime service account
- zero minimum and one maximum instance
- 1 CPU and 512 MiB memory
- concurrency of 20
- timeout of 60 seconds
- API key injected from Secret Manager

The deployment created an Artifact Registry repository and a Cloud Run revision. Traffic was routed only after the revision became ready.

## Validation

Test platform authentication:

```bash
curl -i SERVICE_URL/health
```

Expected: HTTP `403`.

Test an authenticated health request:

```bash
curl -H "Authorization: Bearer $(gcloud auth print-identity-token)" SERVICE_URL/health
```

Expected: `{"status":"ok"}`.

Test application authentication by adding the `x-api-key` header to an authenticated request. The secret value should be retrieved at execution time rather than copied into documentation or shell history.

## Temporary Cloud SQL validation

A PostgreSQL 15 `db-f1-micro` instance was created in `europe-west1` with:

- zonal availability
- 10 GB HDD storage
- automatic storage growth disabled
- automated backups disabled
- deletion protection disabled

The Stage 2 schema was loaded through the Cloud SQL Auth Proxy. Cloud Run then received the database configuration and a Secret Manager reference for the password.

Successful checks:

- `/readiness`: HTTP `200`, database connected
- `POST /requests`: HTTP `201`
- `GET /requests`: HTTP `200` with the stored fictional record

## Recovery procedure

If a new Cloud Run revision fails:

1. Read the revision and request logs.
2. Compare environment-variable and secret-version references with the previous revision.
3. Confirm the container listens on the supplied `PORT`.
4. Confirm the runtime service account has only the required access.
5. Route traffic back to the last known-good revision in Cloud Run.
6. Retest `/health`, authentication, and any connected dependency.

If Cloud SQL is unavailable:

1. Confirm the instance state and recent operations.
2. Confirm the Cloud SQL connection is attached to the Cloud Run revision.
3. Confirm the runtime account has Cloud SQL Client permission.
4. Confirm the database host uses `/cloudsql/PROJECT:REGION:INSTANCE`.
5. Confirm the database secret version does not contain an invisible newline.
6. Keep `/health` separate from `/readiness` so process health remains observable.

## Current recovery state

Cloud SQL was intentionally removed after evidence collection. To restore full readiness, provision a PostgreSQL instance, recreate the schema and restricted user, grant temporary connection permission, attach the instance, and deploy a new revision with the database settings.
