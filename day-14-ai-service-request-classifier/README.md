# AI Service Request Classifier

An n8n automation that receives service requests through a webhook, uses OpenAI to classify them, validates the AI output, stores valid requests in Google Sheets, and notifies the service team through Slack.

## What It Solves

Manually reviewing and routing incoming service requests is repetitive and can slow down response times.

This workflow automates the intake and classification process while validating AI output before it is accepted.

## Key Features

- HTTP POST webhook intake
- Structured JSON processing
- OpenAI-powered request classification
- Category, urgency, language, department, and summary extraction
- AI output validation
- Conditional routing
- Google Sheets storage
- Slack notifications
- Controlled HTTP success and validation-error responses

## Tech Stack

- n8n
- OpenAI
- Google Sheets
- Slack
- REST / HTTP
- Webhooks
- JSON
- Git and GitHub

## Workflow Architecture

```mermaid
flowchart LR
    A[Webhook receives request] --> B[Prepare request data]
    B --> C[OpenAI classification]
    C --> D[Build structured result]
    D --> E[Validate classification]
    E --> F{Classification valid?}

    F -->|Yes| G[Append to Google Sheets]
    G --> H[Notify team in Slack]
    H --> I[Return success response]

    F -->|No| J[Return HTTP 422 validation error]