# Access-Denied Troubleshooting Scenario

## Scenario classification

- Type: Authorization failure
- Environment: Fictional Microsoft Entra ID and SaaS application
- Organisation: Northstar Services
- User: Fictional Finance Analyst
- Application: Finance Reporting Portal
- Data classification: Fictional training data only

Northstar Services is a fictional organisation. All users, systems, identifiers and events in this document are fictional and contain no employer or customer information.

## Incident summary

A newly onboarded Finance Analyst could sign in successfully through Microsoft Entra ID and complete multifactor authentication. When the user opened the Finance Reporting Portal, the application displayed:

```text
Access denied. Your account does not have permission to view this resource.
```

The user required read-only access to monthly financial reports.

## User impact

The user could:

- Sign in to Microsoft 365
- Complete MFA
- Access email
- Access standard collaboration tools
- Open the Finance Reporting Portal sign-in page

The user could not:

- View monthly reports
- Access the reporting dashboard
- Complete assigned reporting work

No other Finance Analysts reported the problem.

## Initial classification

Authentication had succeeded because:

- The username was accepted.
- The user completed MFA.
- Microsoft Entra sign-in was successful.
- The application received the authenticated identity.

The visible failure occurred after sign-in. The incident was therefore investigated primarily as an authorization problem rather than a password problem.

## Security requirements

The investigation followed these controls:

- Do not request the user’s password.
- Do not request an MFA code.
- Do not disable MFA.
- Do not bypass Conditional Access.
- Do not assign a global administrator role.
- Do not grant broader access than required.
- Confirm approval before changing group or role membership.
- Record only necessary fictional diagnostic information.
- Do not include tokens, session cookies or secrets in the ticket.

## Troubleshooting process

### 1. Confirmed the affected identity

The administrator confirmed:

- Correct fictional user account
- Correct username
- Correct department
- Correct manager
- Active account status
- Confirmed employment start date
- No duplicate identity

Result: the correct identity was being used.

### 2. Confirmed authentication status

The administrator reviewed the fictional Microsoft Entra sign-in record.

The record showed:

- Sign-in status: Successful
- MFA requirement: Satisfied
- Conditional Access: Successful
- Account risk: No active risk
- Device requirement: Satisfied
- Application: Finance Reporting Portal
- Fictional correlation reference: NS-DEMO-2026-0042

Result: authentication and Conditional Access were not the cause.

### 3. Confirmed licence assignment

The administrator checked the user’s assigned services.

The required productivity and reporting licences were active.

Result: a missing licence was not the cause.

### 4. Confirmed application assignment

The Finance Reporting Portal used group-based assignment.

Approved access path:

```text
User
→ Finance Analysts group
→ Finance Viewer role
→ Read monthly reports
→ Finance Reporting Portal
```

The affected user was not a member of the `Finance Analysts` group.

Result: the application had received a valid authenticated identity, but that identity had no approved application role.

### 5. Compared with a working user

The administrator compared role structure—not confidential data—with another fictional Finance Analyst.

The working access pattern included:

- Active account
- Successful MFA
- Compliant device
- Required licence
- Finance Analysts group
- Finance Viewer application role

The affected account had every required element except the Finance Analysts group membership.

Result: missing group membership was confirmed as the likely cause.

### 6. Reviewed the onboarding request

The onboarding ticket requested:

- Finance Analyst job title
- Standard productivity licence
- Reporting application licence

The ticket did not explicitly request or approve membership in the Finance Analysts access group.

The administrator did not add the group without approval.

Result: the onboarding request was incomplete.

## Root cause

The user was not a member of the `Finance Analysts` group.

The Finance Reporting Portal assigned the read-only `Finance Viewer` role through that group. Because the group membership was missing, the authenticated user had no authorization to view reports.

This was an RBAC provisioning failure, not an authentication, password, MFA, device-compliance or application-availability failure.

## Resolution

The administrator:

1. Requested approval from the fictional Finance data owner.
2. Confirmed that read-only access was sufficient.
3. Added the user to the `Finance Analysts` group.
4. Recorded the group change and approval reference.
5. Allowed time for directory and application propagation.
6. Asked the user to start a new application session.
7. Verified that monthly reports opened successfully.
8. Verified that edit and administration actions remained unavailable.

The user received the `Finance Viewer` role only. No elevated role was assigned.

## Verification

After the approved group assignment:

- Microsoft Entra sign-in succeeded.
- MFA succeeded.
- Conditional Access succeeded.
- The application recognised the Finance Viewer role.
- Monthly reports opened successfully.
- Report editing remained blocked.
- Permission management remained blocked.
- No unrelated resources became available.

The result met the user’s business requirement while preserving least privilege.

## Safe change record

| Field | Fictional value |
|---|---|
| Incident reference | NS-INC-2026-0042 |
| User | Fictional Finance Analyst |
| Application | Finance Reporting Portal |
| Failure type | Authorization |
| Authentication result | Successful |
| MFA result | Successful |
| Conditional Access result | Successful |
| Required group | Finance Analysts |
| Required role | Finance Viewer |
| Approval | Fictional data-owner approval confirmed |
| Change | Added approved group membership |
| Verification | Read access successful; edit access denied |
| Secrets recorded | None |

## Information excluded from the record

The administrator did not record:

- Passwords
- MFA codes
- Access tokens
- Refresh tokens
- Session cookies
- Personal customer data
- Real employer information
- Unnecessary personal information
- Full sensitive sign-in details

## Preventive actions

Northstar Services should:

- Add approved role templates to onboarding forms.
- Map job roles to standard groups.
- Require system-owner approval for sensitive groups.
- Validate required group membership before closing onboarding.
- Perform a first-week access review.
- Use automated group-based provisioning where appropriate.
- Generate alerts for failed application assignment.
- Review direct permission assignments.
- Maintain separate read, edit and administrator roles.
- Document expected propagation time.
- Train support teams to distinguish authentication from authorization.

## Troubleshooting decision summary

```text
Can the user sign in?
├── No
│   └── Investigate identity, password, MFA, risk and authentication policies
└── Yes
    └── Did Conditional Access succeed?
        ├── No
        │   └── Investigate device, location, risk and policy requirements
        └── Yes
            └── Does the user have the required licence?
                ├── No
                │   └── Obtain approval and assign the required licence
                └── Yes
                    └── Does the user or group have the required role?
                        ├── No
                        │   └── Obtain approval and assign least-privilege access
                        └── Yes
                            └── Investigate application configuration and propagation
```

## Lessons learned

- Successful authentication does not guarantee authorization.
- Access-denied errors should not automatically trigger password resets.
- Group-based RBAC makes missing access easier to diagnose.
- Licences, groups, roles and resource permissions are separate controls.
- Conditional Access results should be checked before changing permissions.
- Missing approval must be resolved before access is granted.
- Read-only access should be preferred when modification is unnecessary.
- Resolution must be verified by confirming both allowed and denied actions.
- Tickets must not contain passwords, tokens or unnecessary sensitive data.