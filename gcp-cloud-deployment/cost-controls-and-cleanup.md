# Cost Controls and Cleanup

## Controls applied before deployment

- Used the Google Cloud free trial without upgrading the account.
- Created a monthly `stage5-all-services-budget` with a €5 target.
- Configured alerts at 10%, 50%, 90%, and 100% of the target.
- Scoped the budget to the Stage 5 project and all services.
- Tracked gross service usage rather than hiding it behind credits.
- Selected one European region for related resources.

A budget is an alerting control, not a guaranteed spending cap.

## Runtime controls

- Cloud Run minimum instances: 0
- Cloud Run maximum instances: 1
- CPU: 1
- Memory: 512 MiB
- Service access: private
- Cloud SQL: smallest shared-core tier and deleted after testing
- Storage auto-increase: disabled for the temporary database
- Backups and high availability: disabled for the temporary exercise

## Cleanup completed

- Stopped the local Docker test container.
- Disconnected Cloud Run from Cloud SQL.
- Removed database environment variables and the database-password mapping.
- Deleted the Cloud SQL instance.
- Removed the Cloud SQL Client role from the runtime service account.
- Deleted the database-password secret.
- Stopped the local Cloud SQL Auth Proxy.
- Confirmed `gcloud sql instances list` returned zero items.

## Resources intentionally retained

- Private Cloud Run service, configured to scale to zero
- Artifact Registry deployment image
- API-key secret used by Cloud Run
- Dedicated runtime service account
- Private Cloud Storage evidence bucket containing a tiny test object
- Pub/Sub topic and empty subscription used for the messaging exercise

These retained resources should be reviewed periodically and deleted when the portfolio evidence is no longer needed.
