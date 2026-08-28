from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class WebhookHandler(BaseHTTPRequestHandler):
	def do_POST(self):
		content_length = int(self.headers["Content-Length"])
		body = self.rfile.read(content_length)

		data = json.loads(body)

		transformed_data = {
			"customer_name": data.get("name"),
			"contact_email": data.get("email"),
			"request": data.get("message"),
			"status": "received",
		}

		response = json.dumps(transformed_data).encode()

		self.send_response(200)
		self.send_header("Content-Type", "application/json")
		self.end_headers()

		self.wfile.write(response)


server = HTTPServer(("localhost", 8000), WebhookHandler)

print("Webhook running at http://localhost:8000/")

server.serve_forever()
