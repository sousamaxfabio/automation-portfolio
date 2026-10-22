# OpsPilot AI

[![OpsPilot AI CI](https://github.com/sousamaxfabio/automation-portfolio/actions/workflows/opspilot-ci.yml/badge.svg)](https://github.com/sousamaxfabio/automation-portfolio/actions/workflows/opspilot-ci.yml)

A containerised AI operations-triage environment combining n8n, Python, the OpenAI API, and a Python FastAPI service.

OpsPilot receives operational requests, validates their input, classifies their category and urgency, recommends an action, and returns a structured response.

The advanced Stage 6 workflow adds duplicate-event protection, persistent audit records, fallback handling, and authenticated human approval for both `high` and `critical` requests.

## Demonstration

![Successful OpsPilot AI triage request](screenshots/api-triage-success.png)

## What It Does

1. Receives an operations request through an n8n webhook.
2. Validates and normalises the expected input fields in a reusable subworkflow.
3. Rejects previously processed `event_id` values to prevent duplicate work.
4. Sends new requests to a Python API over a private Docker network.
5. Uses the OpenAI Responses API to produce structured triage results.
6. Routes `high` and `critical` requests through an authenticated approval form.
7. Records pending and completed approval decisions in an n8n Data Table.
8. Records processed events for auditability and duplicate detection.
9. Returns a controlled fallback response when the AI service is unavailable.
10. Uses a dedicated error workflow to persist workflow failures.

## Example Request

```json
{
  "requester": "Maria",
  "title": "Water leak near electrical socket",
  "description": "Water is entering the office beside an electrical socket and staff are still working nearby."
}
```

## Example Response

```json
{
  "category": "maintenance",
  "urgency": "critical",
  "summary": "A water leak is occurring near an electrical socket.",
  "recommended_action": "Isolate the area and contact emergency maintenance.",
  "confidence": 0.95,
  "request_id": "generated-request-id"
}
```

## Architecture

View the [architecture diagram](docs/architecture.md).

The environment contains:

- An n8n workflow exposed locally on port `5679`
- A FastAPI service exposed locally on port `8000`
- A private Docker network connecting the two services
- A persistent n8n data volume
- Runtime secrets supplied through a private `.env` file

Within the Docker network, n8n reaches the API at:

```text
http://ai-api:8000/triage
```

## Technology Stack

- Python 3.12
- FastAPI
- OpenAI Responses API
- n8n
- Docker
- Docker Compose
- GitHub Actions
- Python `unittest`

## Project Structure

```text
opspilot-ai/
├── docs/
│   └── architecture.md
├── n8n-workflow/
│   ├── opspilot-triage-workflow.json
│   ├── opspilot-advanced-triage-stage6.json
│   ├── opspilot-error-handler.json
│   └── opspilot-validate-and-prepare-request.json
├── screenshots/
│   └── api-triage-success.png
├── tests/
│   └── test_app.py
├── .dockerignore
├── .env.example
├── app.py
├── compose.yaml
├── Dockerfile
├── README.md
└── requirements.txt
```

## Setup Instructions

### Prerequisites

- Docker Desktop
- Docker Compose
- An OpenAI API key

### 1. Create the private environment file

From the project folder:

```powershell
Copy-Item .env.example .env
```

Edit `.env` and replace the placeholder values:

```text
OPENAI_API_KEY=your_real_openai_api_key
OPENAI_MODEL=gpt-4o-mini
N8N_ENCRYPTION_KEY=your_long_random_private_value
```

Never commit or share `.env`.

### 2. Build and start the environment

```powershell
docker compose up -d --build
```

### 3. Check the services

FastAPI health check:

```text
http://localhost:8000/health
```

Interactive API documentation:

```text
http://localhost:8000/docs
```

OpsPilot n8n instance:

```text
http://localhost:5679
```

### 4. Import the n8n workflows

In the OpsPilot n8n instance:

1. Import `n8n-workflow/opspilot-validate-and-prepare-request.json`.
2. Import `n8n-workflow/opspilot-error-handler.json`.
3. Import `n8n-workflow/opspilot-advanced-triage-stage6.json`.
4. Open **Validate Request** in the advanced workflow and select the imported validator workflow.
5. In the advanced workflow settings, select the imported error-handler workflow.
6. Keep the workflows unpublished until their nodes and local resources have been reviewed.

The original introductory workflow remains available as `n8n-workflow/opspilot-triage-workflow.json`.

### 5. Create the advanced workflow Data Tables

Create `opspilot_processed_events` with these string columns:

```text
event_id
status
result_request_id
```

Create `opspilot_approvals` with these string columns:

```text
event_id
request_id
status
decision
reviewer
comments
```

Create `opspilot_error_audit` with these columns:

```text
timestamp        date/time
status           string
workflow_name    string
workflow_id      string
failed_node      string
error_message    string
execution_id     string
execution_url    string
```

In the advanced workflow, select `opspilot_processed_events` in **Allow New Event**, **Detect Duplicate Event**, and **Record Processed Event**. Select `opspilot_approvals` in **Save Pending Approval** and **Save Approval Decision**. In the error-handler workflow, select `opspilot_error_audit` in **Save Error Audit Record**.

### 6. Configure approval authentication and publish

1. Create an n8n **Basic Auth** credential for the approval reviewer.
2. Select it in **Wait for Human Approval**.
3. Confirm that **Requires Human Approval** uses `urgency = high OR urgency = critical`.
4. Publish the validator, error-handler, and advanced workflows.

The production webhook is:

```text
POST http://localhost:5679/webhook/opspilot-stage6
```

Every request must include a unique `event_id`.

## Advanced Verification

A critical ransomware-style request was used for final verification. The workflow returned HTTP `202`, created a pending approval record, generated an authenticated approval URL, accepted the reviewer decision, and persisted the processed-event audit record.

Example pending response fields:

```json
{
  "urgency": "critical",
  "status": "pending_approval",
  "event_id": "stage0-critical-20261022-05",
  "approval_url": "http://localhost:5679/form-waiting/...",
  "message": "High-urgency request requires human approval"
}
```

## Run Automated Tests

Create and use a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

The tests validate:

- Health endpoint responses
- Input validation
- Missing API-key handling
- Structured AI response handling using a mocked OpenAI client

No real OpenAI request is made during automated tests.

## Useful Docker Commands

View service status:

```powershell
docker compose ps
```

View recent logs:

```powershell
docker compose logs --tail 30
```

Rebuild after a code change:

```powershell
docker compose up -d --build
```

Stop the environment without deleting its data:

```powershell
docker compose down
```

Do not add `-v` unless you intentionally want to delete the OpsPilot n8n volume.

## Security

- `.env` is ignored by Git.
- `.env` is excluded from the Docker image.
- The OpenAI key is supplied only to the Python API container.
- The n8n encryption key is supplied only to the n8n container.
- Containers communicate through a private Docker network.
- The Python container runs as a non-root user.
- The API filesystem is read-only.
- Automated tests use fake credentials and make no external API calls.

## Troubleshooting

### Compose reports a missing variable

Confirm that `.env` exists beside `compose.yaml` and contains all three required variables.

### The API returns `503 AI service is not configured`

Confirm that `OPENAI_API_KEY` is set in the private `.env`, then recreate the API container:

```powershell
docker compose up -d --build
```

### The API returns `502 AI triage service failed`

Inspect the API logs:

```powershell
docker compose logs --tail 30 ai-api
```

Check the API key, model access, internet connection, and OpenAI API account status.

### n8n cannot connect to the AI service

Inside n8n, use the Docker service address:

```text
http://ai-api:8000/triage
```

Do not use `localhost:8000` from inside the n8n container.

### Port `8000` or `5679` is already in use

Stop the conflicting local service or change the host-side port in `compose.yaml`.

### Workflows disappear after restart

Confirm that the `opspilot_n8n_data` volume still exists:

```powershell
docker volume inspect opspilot_n8n_data
```

Avoid running `docker compose down -v`.

## CI Pipeline

GitHub Actions runs when OpsPilot files change. It:

- Installs Python dependencies
- Checks Python syntax
- Runs four automated tests
- Validates the Compose configuration with fake CI values
- Verifies that the Docker image builds

## Verification Evidence

The repository includes a successful API-response screenshot, an exported n8n workflow, automated tests, and GitHub Actions validation for both Python and Docker.

## Portfolio Context and Limits

This is a personal portfolio project demonstrating an end-to-end n8n-to-Python AI integration, rather than a commercial operations platform. Input constraints, structured output, a request ID and controlled error responses make the integration inspectable.

The automated tests use a mocked AI client. They verify application behaviour, not the accuracy of live AI classifications. The model's confidence value is self-reported and is not a calibrated probability. A human should review recommendations before taking action.

The service does not currently implement caller authentication, rate limiting, durable request storage or an evaluation dataset. Add these controls and verify deployment configuration before exposing it beyond a controlled demonstration environment.

