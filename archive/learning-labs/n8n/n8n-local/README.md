# Local n8n with Docker Compose

A reproducible local n8n environment managed with Docker Compose. The setup uses persistent storage and keeps credentials outside the repository.

## Start n8n

From this folder, run:

```powershell
docker compose up -d
```

Open n8n at:

```text
http://localhost:5678
```

## Stop n8n

```powershell
docker compose down
```

Stopping or replacing the container does not delete the saved workflows and credentials.

## Persistent Storage

The named Docker volume `n8n-local_n8n_data` is mounted at:

```text
/home/node/.n8n
```

Do not use `docker compose down -v` unless you intentionally want to delete the local n8n data.

## Secure Credentials

- No API keys, passwords, or tokens are stored in `compose.yaml`.
- Credentials are configured through the n8n interface and kept in persistent storage.
- Exported portfolio workflows contain credential references or placeholders, not secret values.

## Skills Demonstrated

- Docker Compose
- Running n8n locally
- Persistent Docker volumes
- Workflow import and recovery
- Secure credential handling

## Troubleshooting Commands

List running containers:

```powershell
docker ps
```

List local images:

```powershell
docker images
```

Inspect recent n8n logs:

```powershell
docker logs --tail 20 n8n-local-n8n-1
```

Stop and restart the container:

```powershell
docker stop n8n-local-n8n-1
docker start n8n-local-n8n-1
```

Check whether the local port is reachable:

```powershell
Test-NetConnection localhost -Port 5678
```

## Failure and Recovery Test

The Compose application was deliberately taken down to confirm that port `5678` became unavailable. Running `docker compose up -d` recreated the container and reattached the existing `n8n-local_n8n_data` volume. The saved workflows remained available after recovery.