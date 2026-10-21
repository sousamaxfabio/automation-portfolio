# Day 6 Mini Integration

A simple Python webhook integration that receives JSON data through a POST request, transforms the data, and returns a JSON response.

## Flow

POST Request → Python Webhook → Read JSON → Transform Data → Return Response

## Technologies Used

- Python
- HTTP
- JSON
- PowerShell
- Git
- GitHub

## Sample Input

```json
{
	"name": "Fabio",
	"email": "fabio@example.com",
	"message": "Hello from the webhook"
}
```

## Sample Output

```json
{
	"success": true,
	"data": {
		"name": "FABIO",
		"email": "FABIO@EXAMPLE.COM",
		"message": "HELLO FROM THE WEBHOOK"
	}
}
```

## Run the Webhook

Start the Python server:

```powershell
python webhook.py
```

Send a POST request from PowerShell:

```powershell
$body = @{
	name = "Fabio"
	email = "fabio@example.com"
	message = "Hello from the webhook"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/webhook" -Method Post -ContentType "application/json" -Body $body
```

## Expected Behavior

The webhook reads the incoming JSON object, transforms the field names, adds a status value, and returns the transformed data as JSON.


