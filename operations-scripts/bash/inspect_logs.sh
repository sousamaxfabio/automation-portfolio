#!/usr/bin/env bash

LOG_FILE="${1:-}"

if [ -z "$LOG_FILE" ]; then
    echo "Usage: $0 <log-file>"
    exit 2
fi

if [ ! -f "$LOG_FILE" ]; then
    echo "FAIL: Log file not found: $LOG_FILE"
    exit 2
fi

ERROR_COUNT=$(grep -ic "ERROR" "$LOG_FILE")
WARNING_COUNT=$(grep -ic "WARNING" "$LOG_FILE")

echo "Log inspection report"
echo "File: $LOG_FILE"
echo "Warnings found: $WARNING_COUNT"
echo "Errors found:   $ERROR_COUNT"

if [ "$ERROR_COUNT" -gt 0 ]; then
    echo
    echo "Most recent errors:"
    grep -in "ERROR" "$LOG_FILE" | tail -n 5
    exit 1
fi

echo "PASS: No errors found"
exit 0