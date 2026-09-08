# Day 24 — Python + APIs

Learning to work with external APIs using Python `requests`.

## Checklist
- [x] requests
- [x] GET requests
- [x] POST requests
- [x] Authentication (Bearer token from.env)
- [x] Environment variables
- [x].env +.env.example
- [x] Parse JSON responses
- [x] Timeouts (5s)
- [x] Failed requests (404 handling)

## How it works
1. Loads `API_KEY` and `API_URL` from `.env`
2. **GET** `https://jsonplaceholder.typicode.com/posts/1` with Bearer auth and `timeout=5`
3. **FAILED** `GET /invalid-endpoint-xyz` → catches `HTTPError 404`
4. **POST** `https://jsonplaceholder.typicode.com/posts` with JSON payload

## Run
```powershell
pip install requests python-dotenv
python main.py
```

## Screenshots
- `screenshots/terminal-success.png` — GET, 404 handling, and POST all passing