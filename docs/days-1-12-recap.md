# Days 1–12 Recap

## Overview

During Days 1–12, I built a foundation in Git, GitHub, APIs, security practices, PowerShell, Python, and n8n workflow automation.

This recap included practical verification of the main concepts and completion of previously identified learning gaps.

## Git and GitHub

Skills practised:

- Creating and cloning repositories
- Checking repository status
- Staging and committing changes
- Pushing and pulling changes
- Creating and switching branches
- Merging changes through pull requests
- Writing clear commit messages
- Creating and closing GitHub Issues
- Organising project files and documentation
- Protecting sensitive and generated files with `.gitignore`

Practical evidence:

- Created GitHub Issue #4 for a reusable project README template
- Created the `feature/4-readme-template` branch
- Added `docs/project-readme-template.md`
- Committed and pushed the branch
- Created and merged Pull Request #5
- Automatically closed Issue #4 through the pull request
- Deleted the completed local branch
- Confirmed that the local `main` branch matched `origin/main`
- Confirmed at least ten meaningful Git commits

## API Fundamentals

API concepts practised:

- `GET` — retrieve data
- `POST` — create data
- `PATCH` — update selected fields
- `DELETE` — remove data
- JSON request and response bodies
- HTTP headers
- Query parameters
- HTTP status codes
- API authentication patterns
- Environment variables
- Webhooks

JSONPlaceholder was used as a safe practice API. Its create, update, and delete operations are simulated and do not permanently change its data.

## Verified API Exercises

### PATCH request

Updated only the `title` field of a test resource.

Result:

- The request succeeded
- The selected field changed
- Existing fields remained in the response

### DELETE request

Sent a DELETE request to a test resource.

Result:

```text
StatusCode: 200
StatusDescription: OK
```

### Query parameter

Used:

```text
?userId=1
```

This filtered the returned posts to records belonging to user 1.

### HTTP header

Sent:

```text
Accept: application/json
```

The response confirmed:

```text
application/json; charset=utf-8
```

### Authentication pattern

Stored a harmless practice key in an environment variable and supplied it through an `X-API-Key` header.

No real API key was used or exposed.

### Python request

Used Python and the `requests` package to retrieve an API resource.

Verified:

- HTTP status code `200`
- JSON content type
- Successful JSON parsing
- Access to an individual response field

## Environment Variables and Security

Security practices verified:

- `.env` is excluded by `.gitignore`
- `.env.local` is excluded by `.gitignore`
- Real API keys should never be committed
- Credentials should not be included in screenshots
- Environment variables can provide configuration and secrets at runtime
- Exported n8n workflows should not contain credentials
- Dummy values should be used in public documentation

Additional ignored files include:

```text
__pycache__/
*.pyc
*.log
node_modules/
n8n-workflows/
```

A `.gitignore` rule protects untracked files. It does not automatically remove a file that was already committed, so tracked files must also be checked.

## n8n Skills

Skills practised:

- Creating workflows
- Connecting and configuring nodes
- Using manual and scheduled triggers
- Receiving webhook data
- Mapping JSON fields
- Writing n8n expressions
- Calling APIs
- Sending data to Google Sheets
- Adding conditional routes
- Testing successful and alternative routes
- Exporting workflow JSON
- Documenting workflows with screenshots

## Completed Workflow Projects

### Day 11 — Service Request API

Built and documented an API-based service-request workflow.

Skills demonstrated:

- Webhook input
- Input validation
- Expressions
- Conditional routing
- API responses
- Testing and troubleshooting
- Project documentation

### Day 12 — Scheduled Weather Check

Built and documented a scheduled weather workflow.

Skills demonstrated:

- Scheduled execution
- Weather API integration
- Data transformation
- Google Sheets integration
- Workflow export verification
- Secure credential handling

## Documentation

Portfolio documentation now includes:

- Project-specific README files
- Workflow screenshots
- Exported workflow JSON files
- A reusable project README template
- Clear setup, testing, security, and limitations sections

## Recap Result

The focused Days 1–12 review is complete.

Previously identified gaps were reviewed and verified:

- Git branches
- Pull requests and merging
- GitHub Issues
- PATCH requests
- DELETE requests
- Query parameters
- HTTP headers
- Authentication patterns
- Environment variables
- HTTP status codes
- Python API requests

The next learning stage begins with the completed Day 13 human-approval workflow.