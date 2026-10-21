import os


app_environment = os.getenv("APP_ENV", "development")
service_api_key = os.getenv("SERVICE_API_KEY")

print(f"Application environment: {app_environment}")

if service_api_key:
    print("Service API key was loaded")
else:
    print("Service API key is missing")