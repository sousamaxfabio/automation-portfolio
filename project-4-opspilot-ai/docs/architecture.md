# OpsPilot AI Architecture

```mermaid
flowchart LR
    U[Webhook Client] -->|POST request| N[n8n Workflow]
    N -->|POST /triage| A[FastAPI AI Service]
    A -->|Responses API| O[OpenAI API]
    O -->|Structured result| A
    A -->|JSON response| N
    N -->|Triage result| U

    N --- V[(Persistent n8n Volume)]

    E[Private .env file] -. OpenAI API key .-> A
    E -. n8n encryption key .-> N

    subgraph D[Docker Compose Environment]
        N
        A
        V
    end
```

## Components

- **n8n:** Receives requests, maps input fields, calls the AI service, and returns results.
- **FastAPI service:** Validates requests and produces structured AI triage results.
- **OpenAI API:** Analyses each operational request.
- **Persistent volume:** Preserves the Project 4 n8n configuration.
- **Private Docker network:** Allows n8n to reach the API as `http://ai-api:8000`.
- **Environment file:** Supplies runtime secrets without storing them in the image or repository.