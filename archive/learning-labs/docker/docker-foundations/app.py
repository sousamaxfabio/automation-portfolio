import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path


APP_MESSAGE = os.getenv("APP_MESSAGE", "Hello from Docker!")
PORT = int(os.getenv("PORT", "8000"))
DATA_FILE = Path("/data/visits.txt")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/":
            self.send_response(404)
            self.end_headers()
            return

        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

        try:
            visits = int(DATA_FILE.read_text())
        except (FileNotFoundError, ValueError):
            visits = 0

        visits += 1
        DATA_FILE.write_text(str(visits))

        message = f"{APP_MESSAGE}\nPersistent visits: {visits}\n".encode()

        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(message)))
        self.end_headers()
        self.wfile.write(message)


print(f"Server listening on port {PORT}", flush=True)
HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
