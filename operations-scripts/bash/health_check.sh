#!/usr/bin/env bash

TARGET_HOST="${1:-api.github.com}"
TARGET_URL="${2:-https://api.github.com}"

echo "Health check started"
echo "Host: $TARGET_HOST"
echo "URL:  $TARGET_URL"
echo

echo "1. Testing network reachability..."

if ping -c 1 -W 3 "$TARGET_HOST" > /dev/null 2>&1; then
    echo "PASS: $TARGET_HOST responded to ping"
else
    echo "WARNING: Ping failed or was blocked"
fi

echo
echo "2. Testing the HTTP endpoint..."

HTTP_STATUS=$(curl -sS -o /dev/null -w "%{http_code}" --max-time 10 "$TARGET_URL")
CURL_EXIT_CODE=$?

if [ "$CURL_EXIT_CODE" -ne 0 ]; then
    echo "FAIL: Could not connect to $TARGET_URL"
    exit 1
fi

echo "HTTP status: $HTTP_STATUS"

if [[ "$HTTP_STATUS" =~ ^2 ]]; then
    echo "PASS: Endpoint is healthy"
    exit 0
else
    echo "FAIL: Endpoint returned HTTP $HTTP_STATUS"
    exit 1
fi