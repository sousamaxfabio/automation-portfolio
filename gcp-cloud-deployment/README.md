# Stage 5 — Google Cloud and Deployment

This project documents the secure deployment of the existing Stage 2 FastAPI service to Google Cloud Run. It demonstrates project and cost controls, IAM, service accounts, Secret Manager, Cloud Storage, Pub/Sub, Cloud Logging, Cloud Monitoring, and a temporary Cloud SQL integration.

No employer or customer information is used. All names and records are fictional.

## Deployment status

- **Google Cloud project:** `stage5-fastapi-cloud-run`
- **Primary region:** `europe-west1`
- **Cloud Run service:** `stage5-fastapi-api`
- **Runtime service account:** `stage5-fastapi-runtime`
- **Access:** private; callers require Google Cloud Run Invoker permission
- **Scaling:** zero minimum instances and one maximum instance
- **Container resources:** 1 CPU and 512 MiB memory
- **API secret:** supplied from Secret Manager, never committed to Git
- **Cloud SQL:** connected and tested successfully, then deleted to stop ongoing charges

The live deployment returned:

- Anonymous `/health` request: HTTP `403`
- Authenticated `/health` request: HTTP `200`
- Authenticated `/readiness` with Cloud SQL connected: HTTP `200`
- Authenticated and API-key-protected `POST /requests`: HTTP `201`
- Authenticated and API-key-protected `GET /requests`: HTTP `200`

The database test returned this fictional record:

```json
[
  {
    "id": 1,
    "customer": "Stage 5 Demo Customer",
    "category": "cloud-deployment",
    "priority": "high"
  }
]
```

## Architecture

See [architecture.md](architecture.md) for the system diagram and request flow.

## Evidence

- [Deployment and recovery guide](deployment-and-recovery.md)
- [IAM and service-account explanation](iam-and-service-accounts.md)
- [Troubleshooting record](troubleshooting.md)
- [Cost controls and cleanup](cost-controls-and-cleanup.md)
- [FastAPI service](../stage2-api-service/README.md)
- [Cloud Run-compatible Dockerfile](../stage2-api-service/Dockerfile)

## Services practised

| Service | Practical evidence |
|---|---|
| Cloud Run | Built and deployed the container as a private, scale-to-zero service |
| IAM | Used separate human and workload identities with least privilege |
| Service Accounts | Attached a dedicated runtime identity to Cloud Run |
| Secret Manager | Injected API and database credentials without storing values in source control |
| Cloud Storage | Created a private regional bucket and uploaded/downloaded a test object |
| Pub/Sub | Created a topic and subscription, published a message, pulled and acknowledged it |
| Cloud SQL | Connected PostgreSQL to Cloud Run, tested persistence, then deleted the instance |
| Cloud Logging | Inspected startup and HTTP request logs |
| Cloud Monitoring | Reviewed request count, latency, instance count, and billable instance time |
| Cloud Functions | Studied event-triggered functions and their relationship to Pub/Sub and Cloud Storage |

## Current limitations

The Cloud SQL instance was intentionally deleted after the test. The deployed service therefore keeps `/health` available, while `/readiness` correctly returns HTTP `503` until a database is provisioned and connected again.

The deployment is private. It is working evidence, not a public production service.

## Learning status

The official Google Cloud Engineer learning path and relevant free learning material remain in progress. No Google Cloud certification or verified skill badge is claimed here.
