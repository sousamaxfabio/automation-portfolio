# Operations Scripts

Cross-platform operations and troubleshooting scripts created during Stage 3 of the automation engineering roadmap.

This folder demonstrates practical Linux, Bash, PowerShell, networking, API troubleshooting, log inspection, scheduling and Docker investigation skills.

## Folder structure

```text
operations-scripts/
├── bash/
│   ├── api_test.sh
│   ├── health_check.sh
│   └── inspect_logs.sh
├── powershell/
│   ├── health_check.ps1
│   └── inspect_logs.ps1
├── scheduling/
│   └── cron.example
├── docs/
│   └── failed-service-investigation.md
└── README.md
```

## Requirements

### Linux and Bash

- Ubuntu through WSL 2 or another Linux environment
- Bash
- `curl`
- `ping`

### Windows and PowerShell

- Windows PowerShell or PowerShell 7
- Network access for remote health checks

### Docker investigation

- Docker Desktop
- Docker Engine running

## Exit codes

The scripts use standard operational exit codes:

- `0` — the check completed successfully.
- `1` — the check completed but detected an unhealthy condition.
- `2` — the script was used incorrectly or an input file was missing.

Exit codes allow schedulers, monitoring systems and CI pipelines to determine whether a check passed or failed.

## Bash health check

File:

```text
bash/health_check.sh
```

The script:

1. Tests whether a host responds to `ping`.
2. Sends an HTTP request to an endpoint.
3. Reports the HTTP status.
4. Returns exit code `0` for a 2xx response.
5. Returns exit code `1` for a connection failure or non-2xx response.

### Default GitHub API check

```bash
./bash/health_check.sh
```

### Custom target

```bash
./bash/health_check.sh api.github.com "https://api.github.com/users/sousamaxfabio"
```

### Expected failure example

```bash
./bash/health_check.sh api.github.com "https://api.github.com/users/definitely-not-a-real-user-948271/repos"
```

A successful ping combined with HTTP `404` indicates that the network and API are reachable but the requested resource does not exist.

## Bash log inspector

File:

```text
bash/inspect_logs.sh
```

The script:

1. Confirms that the supplied log file exists.
2. Counts warning entries.
3. Counts error entries.
4. Displays the five most recent errors with line numbers.
5. Returns exit code `1` when errors are found.

### Usage

```bash
./bash/inspect_logs.sh /path/to/application.log
```

## Bash API test

File:

```text
bash/api_test.sh
```

The script compares an API’s actual HTTP status with an expected status. A test can pass for either a successful or unsuccessful HTTP response when the returned status matches the expected behaviour.

### Test a successful request

```bash
./bash/api_test.sh "https://api.github.com/users/sousamaxfabio" 200
```

### Test an expected 404 response

```bash
./bash/api_test.sh "https://api.github.com/users/definitely-not-a-real-user-948271" 404
```

The script also displays a limited preview of the response body and deletes its temporary response file automatically.

## PowerShell health check

File:

```text
powershell/health_check.ps1
```

The script performs the same network and HTTP checks as the Bash health check using native PowerShell commands.

### Default GitHub API check

```powershell
& ".\powershell\health_check.ps1"
```

### Custom target

```powershell
& ".\powershell\health_check.ps1" `
    -TargetHost "api.github.com" `
    -TargetUrl "https://api.github.com/users/sousamaxfabio"
```

### Expected failure example

```powershell
& ".\powershell\health_check.ps1" `
    -TargetHost "api.github.com" `
    -TargetUrl "https://api.github.com/users/definitely-not-a-real-user-948271/repos"
```

## PowerShell log inspector

File:

```text
powershell/inspect_logs.ps1
```

The script uses structured PowerShell objects to count warnings and errors and display recent matching lines.

### Usage

```powershell
& ".\powershell\inspect_logs.ps1" -LogFile ".\app.log"
```

## Linux scheduling

File:

```text
scheduling/cron.example
```

The example file contains:

- A health check scheduled every 15 minutes.
- A log inspection scheduled every day at 09:00.
- Explicit executable paths and output redirection suitable for cron’s limited environment.

The example is intentionally not installed automatically. Review paths and frequency before adding entries to a real user crontab.

To inspect existing schedules:

```bash
crontab -l
```

To edit the current user’s schedule:

```bash
crontab -e
```

## Failed Docker service investigation

Documentation:

```text
docs/failed-service-investigation.md
```

The investigation demonstrates:

1. Finding a stopped container with `docker ps -a`.
2. Reading the application output with `docker logs`.
3. Checking exit codes and Docker state with `docker inspect`.
4. Distinguishing a Docker Engine problem from an application problem.
5. Diagnosing a PowerShell-to-Linux quoting failure.
6. Supplying a required environment variable.
7. Verifying the corrected container through status and logs.

## Useful operational commands

### Linux services and logs

```bash
systemctl is-system-running
systemctl --failed --no-pager
systemctl status systemd-journald --no-pager
journalctl -p err -b --no-pager
```

### Linux resources

```bash
df -h
free -h
uptime
ps aux --sort=-%mem
```

### Network and API checks

```bash
ping -c 4 api.github.com
curl -I "https://api.github.com"
```

### Docker checks

```powershell
docker ps
docker ps -a
docker logs CONTAINER_NAME
docker inspect CONTAINER_NAME
```

## Security notes

- No API tokens, passwords or secrets are stored in these scripts.
- Use environment variables for sensitive configuration.
- Do not commit `.env` files containing real credentials.
- Validate target URLs and file paths before using scripts in production.
- Review scheduled commands before installing them.