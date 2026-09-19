# User Offboarding Procedure

## Document purpose

This procedure describes how Northstar Services removes user access safely, consistently and with an auditable record while preserving required business data.

Northstar Services is a fictional organisation. All names, systems and examples in this document are fictional and contain no employer or customer information.

## Scope

This procedure applies to:

- Employees leaving the organisation
- Contractors reaching the end of an engagement
- Temporary workers reaching an expiry date
- External collaborators who no longer require access
- Users whose access must be suspended
- Users changing to a role that no longer requires their current access

It covers:

- Sign-in blocking
- Session revocation
- Password and authentication reset
- Group and role removal
- Application-access removal
- Licence recovery
- Data preservation and transfer
- Device and MDM actions
- Token and credential revocation
- Documentation and verification

## Security principles

The offboarding process follows these principles:

- Block access promptly.
- Verify the request before making changes.
- Preserve business data before deleting an identity.
- Revoke active sessions and authentication methods.
- Remove access according to least privilege.
- Follow legal-hold and retention requirements.
- Never record passwords, MFA codes or access tokens.
- Document every administrative change.
- Verify that access has actually been removed.
- Escalate suspicious activity to the security team.

## Roles and responsibilities

### Human Resources

Human Resources:

- Confirms the worker’s final date and time.
- Confirms whether the departure is standard or urgent.
- Provides the manager and worker type.
- Identifies any legal or retention requirement.
- Does not request or receive the user’s password.

### Manager

The manager:

- Confirms required data ownership transfers.
- Identifies shared files, mailboxes and application records.
- Confirms whether delegated access is required.
- Approves removal of business access.
- Confirms return of physical assets.

### IT or SaaS administrator

The administrator:

- Validates the request and approvals.
- Blocks access at the approved time.
- Revokes sessions and authentication methods.
- Removes group, role and application access.
- Preserves or transfers data according to policy.
- Recovers licences.
- Updates device-management records.
- Documents and verifies all changes.

### Security or compliance team

The security or compliance team:

- Directs urgent or security-related suspensions.
- Reviews suspicious sign-in activity.
- Confirms legal-hold or investigation requirements.
- Approves exceptions to the normal process.

### Application or data owner

The owner:

- Confirms how application data should be retained.
- Reassigns records, workflows and automation ownership.
- Confirms that specialised access has been removed.

## Required offboarding request

The request must contain:

- User’s full name
- Organisational username or approved identifier
- Department
- Manager
- Worker type
- Final working date
- Exact access-removal time
- Standard or urgent departure classification
- Required data-transfer recipient
- Required mailbox handling
- Required file-ownership transfer
- Device and physical-asset details
- Legal-hold or retention instructions
- Application-owner approvals
- Ticket or request reference

The request must not contain:

- Passwords
- MFA codes
- Recovery codes
- Personal access tokens
- API keys
- Unnecessary personal information
- Customer data

## Departure types

### Standard departure

A standard departure has a known final date and follows the planned offboarding schedule.

Access should normally remain available until the authorised removal time.

### Urgent or security-related departure

An urgent departure requires immediate action authorised by Human Resources, Security or another approved authority.

The administrator should:

- Block sign-in immediately.
- Revoke active sessions.
- Disable privileged access.
- Preserve logs and evidence.
- Avoid alerting the user when instructed by the authorised investigation owner.
- Follow legal and incident-response requirements.

## Procedure

### 1. Validate the request

Before changing access, confirm:

- The request came from an authorised source.
- The user’s identity is unambiguous.
- The final date and access-removal time are clear.
- The departure classification is clear.
- Data-retention instructions are available.
- The manager or data owner is identified.
- Any legal hold or investigation requirement is documented.
- The request does not ask the administrator to obtain the user’s password.

If the identity, timing or approval is unclear, pause and escalate.

### 2. Identify the user’s access

Review the identity and record:

- Primary account
- Secondary or administrative accounts
- Email account
- Group memberships
- Directory roles
- Application roles
- SSO assignments
- Shared mailboxes
- Shared drives and sites
- File and folder ownership
- Calendar ownership
- Automation ownership
- API tokens and personal access tokens
- Registered MFA methods
- Active sessions
- Managed devices
- Mobile-device enrolments
- Licences
- Physical assets

Do not assume that disabling the primary account automatically removes every external or local account.

### 3. Preserve required information

Before deletion:

- Confirm retention requirements.
- Check for legal hold.
- Preserve required mailbox data.
- Transfer ownership of business files.
- Transfer calendars when required.
- Reassign shared mailboxes.
- Reassign application records.
- Reassign automation workflows.
- Reassign service accounts or integrations incorrectly owned by the departing user.
- Preserve relevant audit and sign-in logs.
- Record who received transferred data.

Do not transfer personal or irrelevant information unnecessarily.

### 4. Block sign-in

At the authorised time:

- Disable or suspend the primary identity.
- Block interactive sign-in.
- Disable secondary administrative accounts.
- Disable local application accounts that are not controlled through SSO.
- Confirm that the account status changed successfully.

Blocking sign-in should occur before account deletion.

### 5. Revoke active sessions

Revoke:

- Browser sessions
- Desktop application sessions
- Mobile application sessions
- Refresh tokens
- Remembered sign-ins
- Application sessions where supported
- VPN sessions
- Remote-access sessions

Disabling an account alone may not immediately terminate every existing session.

### 6. Reset authentication controls

According to policy:

- Reset the account password to an unknown random value.
- Remove registered MFA methods.
- Revoke passwordless credentials.
- Revoke recovery codes.
- Revoke app passwords.
- Disable authentication devices.
- Remove trusted-device registrations where required.

Do not place replacement passwords or recovery information in the ticket.

### 7. Remove privileged access

Immediately remove:

- Global or super administrator roles
- Security roles
- Billing roles
- Application-owner roles
- Group-owner roles
- Privileged Identity Management eligibility
- Emergency or temporary elevated access
- Local administrator access
- Cloud-subscription roles
- Database administrator roles

Privileged access must be checked separately from ordinary group membership.

### 8. Remove groups and application assignments

Remove the user from:

- Department groups
- Security groups
- Collaboration groups
- Distribution groups
- Shared drives
- Teams or channels
- Application-assignment groups
- SSO applications
- Project workspaces
- Customer-support systems
- Source-code platforms
- Documentation systems

Record any access that cannot be removed and escalate it to the appropriate owner.

### 9. Revoke tokens and keys

Identify and revoke user-owned:

- Personal access tokens
- OAuth grants
- API tokens
- SSH keys
- Application passwords
- CLI sessions
- Git credentials
- Cloud-access keys
- Automation credentials

If a business process depends on a personal credential, replace it with an approved service identity rather than transferring the departing user’s secret.

### 10. Handle email and collaboration data

According to policy:

- Convert the mailbox to a shared mailbox when approved.
- Configure an approved automatic reply when required.
- Configure mail forwarding only with documented approval.
- Delegate mailbox access only to authorised recipients.
- Transfer calendar ownership when needed.
- Remove the user from collaboration groups.
- Preserve messages according to retention policy.

Do not configure indefinite forwarding without review and expiry.

### 11. Handle files and ownership

Transfer required business content from:

- Personal cloud storage
- Shared drives
- Team sites
- Document libraries
- Project folders
- Reporting workspaces
- Automation platforms

Record:

- Source owner
- New owner
- Data location
- Approval
- Transfer date
- Retention period

Verify that transferred content is accessible to the new owner before deleting the original account.

### 12. Recover licences

After required data handling is complete:

- Remove product licences.
- Remove premium security licences when appropriate.
- Recover specialist application licences.
- Record licences returned to the available pool.
- Confirm that licence removal will not delete required data unexpectedly.

Licence removal should follow, not replace, identity disabling.

### 13. Secure managed devices

For organisational devices:

- Mark the asset as returned or outstanding.
- Disable remote access.
- Remove the user’s local access.
- Preserve required evidence.
- Back up approved business data.
- Perform an approved corporate wipe or full wipe.
- Rebuild or reassign the device.
- Update the asset-management system.

For personal or BYOD devices:

- Remove organisational profiles.
- Retire the device from MDM.
- Remove organisational applications and data.
- Do not erase personal data unless policy, ownership and authorisation explicitly permit it.

### 14. Recover physical assets

Confirm return of:

- Laptop
- Mobile phone
- Security key
- Smart card
- Access badge
- Hardware token
- Storage devices
- Company documents
- Other assigned equipment

Outstanding assets should be escalated through the approved process.

### 15. Check forwarding, delegation and automation

Review:

- Email forwarding
- Mailbox delegation
- Calendar delegation
- Shared-drive ownership
- Workflow ownership
- Scheduled jobs
- Application integrations
- Notification destinations
- Approval chains
- Service accounts
- Webhooks

Remove or reassign dependencies so that business processes continue securely.

### 16. Verify access removal

Confirm:

- Sign-in is blocked.
- Active sessions are revoked.
- Administrative roles are removed.
- Group memberships are removed.
- SSO applications are inaccessible.
- Local application accounts are disabled.
- Tokens and keys are revoked.
- Managed devices are retired or secured.
- Required data has a new owner.
- Licences are recovered.
- No unauthorised forwarding remains.

Verification should use administrative status and audit records, not the former user’s password.

### 17. Monitor after offboarding

For an appropriate period:

- Review sign-in attempts.
- Review security alerts.
- Review unexpected application activity.
- Review attempts to use revoked tokens.
- Confirm that forwarding and delegation remain appropriate.
- Escalate suspicious activity.

### 18. Delete the account according to policy

Delete the identity only when:

- The retention period permits deletion.
- Required business data has been preserved.
- Legal-hold requirements are satisfied.
- Ownership transfers are complete.
- Security or investigation requirements are complete.
- The manager and relevant owners have confirmed completion.

Permanent deletion must not be used as the first offboarding action.

## Offboarding record

The administrative record should include:

| Field | Example |
|---|---|
| Request reference | NS-OFF-2026-001 |
| User | Fictional User |
| Department | Support |
| Departure type | Standard |
| Approved removal time | Fictional date and time |
| Sign-in blocked | Confirmed |
| Sessions revoked | Confirmed |
| MFA methods removed | Confirmed |
| Privileged roles removed | None assigned |
| Groups removed | Confirmed |
| Applications removed | Confirmed |
| Tokens revoked | Confirmed |
| Data owner | Fictional Manager |
| Mailbox action | Retained according to policy |
| Device action | Returned and retired |
| Licences recovered | Confirmed |
| Monitoring review | Scheduled |
| Completed by | Administrator role |
| Completion date | Fictional date |

Do not record passwords, tokens, recovery codes or unnecessary personal information.

## Failure and escalation procedure

If access cannot be removed:

1. Record the exact failed action.
2. Record the error message without secrets.
3. Confirm that the correct identity was selected.
4. Confirm administrator permissions.
5. Check whether the account is synchronised from another directory.
6. Check whether access is inherited through a group.
7. Check whether the application is controlled outside SSO.
8. Check for active tokens or local accounts.
9. Escalate to the identity, security or application owner.
10. Apply an approved temporary containment control.
11. Verify the final resolution.
12. Update the incident or offboarding record.

## Completion criteria

Offboarding is complete only when:

- Sign-in is blocked.
- Sessions and tokens are revoked.
- Privileged access is removed.
- Group and application access is removed.
- Required data is preserved or transferred.
- Devices and physical assets are handled.
- Licences are recovered.
- Audit records are preserved.
- Post-offboarding monitoring is scheduled.
- All actions and approvals are documented.
- Account deletion follows the approved retention policy.