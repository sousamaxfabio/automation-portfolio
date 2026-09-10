# Intelligent Invoice Processing Automation

An n8n-based invoice processing workflow that extracts invoice data, validates required fields, supports human approval, prevents duplicate records, logs outcomes in Airtable, and sends success or failure notifications.

## What It Solves

Manual invoice handling is repetitive and error-prone.

This workflow automates the invoice-processing path while keeping validation, duplicate checking, human approval, audit logging, and failure handling under control.

## Key Features

- PDF invoice data extraction
- Required-field validation
- Human approval step
- Duplicate invoice detection
- Airtable record creation and audit logging
- Retry handling for temporary service failures
- Gmail success notifications
- Dedicated failure notification workflow
- Tests for invalid, incomplete, duplicate, and successful invoices

## Tech Stack

- n8n
- OpenAI
- Airtable
- Gmail
- PDF data extraction
- Webhooks
- Conditional routing
- Error workflows
- Retry handling

## Workflow Architecture

### Main Invoice Workflow

```mermaid
flowchart LR
    A[Upload an invoice] --> B[Extract from File]
    B --> C[Information Extractor]
    C --> D[Validate Invoice]
    D --> E{Validation Passed?}

    E -->|No| F[Log Validation Failure]
    F --> G[Validation Failed]

    E -->|Yes| H[Review Invoice]
    H --> I{Invoice Approved?}

    I -->|No| J[Log Approval Rejection]
    J --> K[Invoice Rejected]

    I -->|Yes| L[Find Existing Invoice]
    L --> M{Duplicate Found?}

    M -->|Yes| N[Log Duplicate Invoice]
    N --> O[Duplicate Invoice]

    M -->|No| P[Create a record]
    P --> Q[Log Successful Execution]
    Q --> R[Send Success Notification]
    R --> S[Invoice Saved]