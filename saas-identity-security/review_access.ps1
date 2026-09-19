param(
    [string]$CsvPath = (Join-Path $PSScriptRoot "access-review.csv")
)

if (-not (Test-Path -LiteralPath $CsvPath)) {
    Write-Error "Access review file not found: $CsvPath"
    exit 2
}

$Today = Get-Date
$Records = Import-Csv -LiteralPath $CsvPath

$Results = foreach ($Record in $Records) {
    $Recommendation = "Keep"
    $Reasons = [System.Collections.Generic.List[string]]::new()

    if ($Record.account_status -ne "Active") {
        $Recommendation = "Remove"
        $Reasons.Add("Account is not active")
    }

    if ($Record.approved -ne "Yes") {
        $Recommendation = "Remove"
        $Reasons.Add("Access is not approved")
    }

    $ExpectedDepartment = switch ($Record.group_name) {
        "Support Team" { "Support" }
        "Finance Analysts" { "Finance" }
        "Identity Operations" { "IT" }
        "External Collaborators" { "External" }
        default { $null }
    }

    if (
        $ExpectedDepartment -and
        $Record.department -ne $ExpectedDepartment
    ) {
        $Recommendation = "Remove"
        $Reasons.Add(
            "Department does not match the assigned group"
        )
    }

    if ($Record.expiry_date) {
        $ExpiryDate = [datetime]::ParseExact(
            $Record.expiry_date,
            "yyyy-MM-dd",
            [System.Globalization.CultureInfo]::InvariantCulture
        )

        if ($ExpiryDate -lt $Today.Date) {
            $Recommendation = "Remove"
            $Reasons.Add("Access has expired")
        }
        elseif (
            $Record.privileged -eq "Yes" -and
            $Recommendation -eq "Keep"
        ) {
            $Recommendation = "Review"
            $Reasons.Add(
                "Privileged access expires on $($Record.expiry_date)"
            )
        }
    }
    elseif (
        $Record.privileged -eq "Yes" -and
        $Recommendation -eq "Keep"
    ) {
        $Recommendation = "Review"
        $Reasons.Add("Privileged access has no expiry date")
    }

    if ($Reasons.Count -eq 0) {
        $Reasons.Add("Access is active, approved and role-aligned")
    }

    [pscustomobject]@{
        UserId        = $Record.user_id
        User          = $Record.display_name
        Department    = $Record.department
        Group         = $Record.group_name
        Role          = $Record.role_name
        Privileged    = $Record.privileged
        Recommendation = $Recommendation
        Reason        = $Reasons -join "; "
    }
}

$OutputPath = Join-Path $PSScriptRoot "access-review-results.csv"

$Results |
    Export-Csv -LiteralPath $OutputPath -NoTypeInformation -Encoding UTF8

Write-Host ""
Write-Host "Access review results"
Write-Host "---------------------"

$Results |
    Select-Object User, Role, Recommendation |
    Format-Table -AutoSize

$KeepCount = @($Results | Where-Object Recommendation -eq "Keep").Count
$ReviewCount = @($Results | Where-Object Recommendation -eq "Review").Count
$RemoveCount = @($Results | Where-Object Recommendation -eq "Remove").Count

Write-Host "Summary"
Write-Host "Keep:   $KeepCount"
Write-Host "Review: $ReviewCount"
Write-Host "Remove: $RemoveCount"
Write-Host ""
Write-Host "Detailed report: $OutputPath"

if (($ReviewCount + $RemoveCount) -gt 0) {
    exit 1
}

exit 0