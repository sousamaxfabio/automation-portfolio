# Failed Service Investigation

## Incident date

18 September 2026

## Environment

- Windows 11
- PowerShell
- Docker Desktop
- Linux container image: `python:3.14-slim`

## Summary

A training container named `stage3-failed-service` did not appear in the normal running-container list. The investigation determined that the container had started successfully but its application process exited with code `1` after reporting a missing `APP_MODE` environment variable.

An initial remediation attempt also failed because PowerShell split an inline Linux shell command into multiple Docker command arguments. The corrected solution avoided nested shell quoting and passed the required environment variable directly to a Python process.

## Symptoms

The following command returned no running container:

```powershell
docker ps --filter "name=stage3-failed-service"
```

Listing all containers showed:

```text
stage3-failed-service   Exited (1)
```

## Investigation

### 1. Checked stopped containers

```powershell
docker ps -a --filter "name=stage3-failed-service"
```

The container had exited with code `1`.

### 2. Inspected application logs

```powershell
docker logs stage3-failed-service
```

The log contained:

```text
ERROR: required APP_MODE is missing
```

### 3. Inspected container state

```powershell
docker inspect --format "ExitCode={{.State.ExitCode}} Error={{.State.Error}} FinishedAt={{.State.FinishedAt}}" stage3-failed-service
```

The result showed an application exit code of `1` and no Docker Engine error. This confirmed that Docker created and started the container successfully, but the process inside the container failed.

### 4. Investigated the unsuccessful first remediation

The first corrected container exited with code `2` and reported:

```text
Syntax error: end of file unexpected (expecting "fi")
```

Inspecting the configured command showed that PowerShell had split the intended Linux shell program into several arguments:

```powershell
docker inspect --format '{{json .Config.Cmd}}' stage3-healthy-service
```

This confirmed a cross-platform command-quoting problem.

## Root cause

The original service failed because its required `APP_MODE` environment variable was not provided.

The first remediation failed separately because nested quotation marks were interpreted differently by PowerShell, Docker and the Linux shell, causing the shell command to be split incorrectly.

## Resolution

A new container was started with:

- `APP_MODE=production`
- A direct Python command instead of a nested inline Linux shell program
- A temporary running period for verification

The corrected container was named `stage3-healthy-service-fixed`.

## Verification

The running-container list showed:

```text
stage3-healthy-service-fixed   Up
```

The container log showed:

```text
INFO: service started in production mode
```

This confirmed that the required configuration was available and the corrected process remained running.

## Lessons learned

- Use `docker ps -a` when a container is missing from `docker ps`.
- Container exit codes identify whether the main process succeeded.
- `docker logs` often provides the fastest route to the application-level cause.
- An empty Docker state error combined with a non-zero exit code usually indicates failure inside the container.
- Inspect the stored container command rather than guessing when quoting behaves unexpectedly.
- Avoid complicated nested quoting across PowerShell, Docker and Linux shells when a simpler command is available.
- Always verify a remediation through container status and application logs.