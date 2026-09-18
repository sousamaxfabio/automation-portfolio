param(
    [string]$TargetHost = "api.github.com",
    [string]$TargetUrl = "https://api.github.com"
)

Write-Host "Health check started"
Write-Host "Host: $TargetHost"
Write-Host "URL:  $TargetUrl"
Write-Host ""

Write-Host "1. Testing network reachability..."

$PingSucceeded = Test-Connection `
    -ComputerName $TargetHost `
    -Count 1 `
    -Quiet

if ($PingSucceeded) {
    Write-Host "PASS: $TargetHost responded to ping" -ForegroundColor Green
}
else {
    Write-Host "WARNING: Ping failed or was blocked" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "2. Testing the HTTP endpoint..."

try {
    $Response = Invoke-WebRequest `
        -Uri $TargetUrl `
        -Method Head `
        -TimeoutSec 10 `
        -UseBasicParsing

    $StatusCode = [int]$Response.StatusCode
}
catch {
    if ($null -ne $_.Exception.Response) {
        $StatusCode = [int]$_.Exception.Response.StatusCode
    }
    else {
        Write-Host "FAIL: Could not connect to $TargetUrl" -ForegroundColor Red
        exit 1
    }
}

Write-Host "HTTP status: $StatusCode"

if ($StatusCode -ge 200 -and $StatusCode -lt 300) {
    Write-Host "PASS: Endpoint is healthy" -ForegroundColor Green
    exit 0
}
else {
    Write-Host "FAIL: Endpoint returned HTTP $StatusCode" -ForegroundColor Red
    exit 1
}