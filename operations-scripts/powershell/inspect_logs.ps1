param(
    [Parameter(Mandatory = $true)]
    [string]$LogFile
)

if (-not (Test-Path -LiteralPath $LogFile -PathType Leaf)) {
    Write-Host "FAIL: Log file not found: $LogFile" -ForegroundColor Red
    exit 2
}

$ErrorMatches = @(
    Select-String -LiteralPath $LogFile -Pattern "ERROR"
)

$WarningMatches = @(
    Select-String -LiteralPath $LogFile -Pattern "WARNING"
)

Write-Host "Log inspection report"
Write-Host "File: $LogFile"
Write-Host "Warnings found: $($WarningMatches.Count)"
Write-Host "Errors found:   $($ErrorMatches.Count)"

if ($ErrorMatches.Count -gt 0) {
    Write-Host ""
    Write-Host "Most recent errors:" -ForegroundColor Red

    $ErrorMatches |
        Select-Object -Last 5 |
        ForEach-Object {
            Write-Host "$($_.LineNumber):$($_.Line)"
        }

    exit 1
}

Write-Host "PASS: No errors found" -ForegroundColor Green
exit 0