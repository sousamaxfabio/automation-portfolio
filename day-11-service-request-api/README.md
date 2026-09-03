# Service Request API

An n8n webhook workflow that receives customer service requests, validates the submitted data, normalizes it, and routes the request according to its urgency.

## Features

- Accepts service requests through a POST webhook
- Checks that `name`, `email`, and `message` are present
- Validates the email format
- Validates and normalizes the urgency value
- Adds a request ID and received timestamp
- Routes high-urgency requests for urgent attention
- Routes normal requests to the standard queue
- Calculates a response deadline
- Returns clear validation errors with HTTP status `400`

## Request Body

```json
{
  "name": "Nora",
  "email": "nora@example.com",
  "message": "The customer portal is unavailable",
  "urgency": "high"
}
```

## Successful Urgent Response

```json
{
  "requesterName": "Nora",
  "requesterEmail": "nora@example.com",
  "requestMessage": "The customer portal is unavailable",
  "urgency": "high",
  "receivedAt": "2026-09-03T09:42:11.752+01:00",
  "requestId": "105",
  "routingStatus": "escalated",
  "responseMessage": "Request from Nora has been marked for urgent attention.",
  "responseDueAt": "2026-09-03T10:
  