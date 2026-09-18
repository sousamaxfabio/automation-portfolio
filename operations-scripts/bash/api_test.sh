#!/usr/bin/env bash

# The first argument is the API URL.
# The second argument is the expected HTTP status, defaulting to 200.
URL="${1:-}"
EXPECTED_STATUS="${2:-200}"

# Exit code 2 means that the script was used incorrectly.
if [ -z "$URL" ]; then
    echo "Usage: $0 <url> [expected-status]"
    exit 2
fi

# Create a temporary file for the response body.
RESPONSE_FILE=$(mktemp)

# Delete the temporary file automatically when the script finishes.
trap 'rm -f "$RESPONSE_FILE"' EXIT

echo "API test started"
echo "URL:             $URL"
echo "Expected status: $EXPECTED_STATUS"

# Send the request, save the body, and capture the HTTP status.
ACTUAL_STATUS=$(curl \
    -sS \
    -o "$RESPONSE_FILE" \
    -w "%{http_code}" \
    --max-time 10 \
    "$URL")

CURL_EXIT_CODE=$?

# A curl failure means that no valid HTTP response was received.
if [ "$CURL_EXIT_CODE" -ne 0 ]; then
    echo "FAIL: The API connection failed"
    exit 1
fi

echo "Actual status:   $ACTUAL_STATUS"
echo
echo "Response preview:"
head -c 500 "$RESPONSE_FILE"
echo

# Compare the actual and expected statuses.
if [ "$ACTUAL_STATUS" = "$EXPECTED_STATUS" ]; then
    echo "PASS: Actual status matched the expected status"
    exit 0
else
    echo "FAIL: Expected HTTP $EXPECTED_STATUS but received HTTP $ACTUAL_STATUS"
    exit 1
fi