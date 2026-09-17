# Stage 2 API Service

A small FastAPI service demonstrating SQL, PostgreSQL, API validation, authentication, automated testing, and Docker packaging.

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- psycopg
- Pydantic
- pytest
- Docker

## Features

- GET and POST API endpoints
- PostgreSQL database integration
- Pydantic request validation
- API-key authentication
- Health and readiness endpoints
- Application-level error handling
- Parameterised SQL queries
- Automated endpoint tests
- Mocked external API test
- Test coverage reporting
- Docker packaging

## Database Structure

### customers

- id
- name

### requests

- id
- customer_id
- category
- priority

`requests.customer_id` references `customers.id`.

## API Endpoints

### Health

GET `/health`

Example response:

```json
{
  "status": "ok"
}