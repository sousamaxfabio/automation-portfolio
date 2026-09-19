# User Onboarding Procedure

## Document purpose

This procedure describes how Northstar Services creates and configures user access safely, consistently and with an auditable approval record.

Northstar Services is a fictional organisation. All names, systems and examples in this document are fictional and contain no employer or customer information.

## Scope

This procedure applies to:

- Employees
- Contractors
- Temporary workers
- Interns
- External collaborators who require an organisational account

It covers:

- Identity creation
- Licence assignment
- Group and role membership
- Multifactor authentication
- Application access
- Device enrolment
- Verification
- Documentation
- Post-onboarding access review

## Security principles

The onboarding process follows these principles:

- Least privilege
- Role-based access control
- No shared user accounts
- Multifactor authentication
- Separation of standard and administrative access
- Manager and system-owner approval
- Secure delivery of initial credentials
- Documented and reviewable access changes
- No passwords or authentication secrets in support tickets

## Roles and responsibilities

### Hiring manager

The hiring manager:

- Confirms the user’s identity and start date.
- Provides the correct job title and department.
- Identifies the access required for the role.
- Approves standard business access.
- Confirms whether the worker is permanent, temporary or external.

### Human Resources

Human Resources:

- Confirms that the worker is authorised to start.
- Supplies the official name, worker type and employment dates.
- Provides the manager and department information.
- Does not send passwords or sensitive authentication data.

### IT or SaaS administrator

The administrator:

- Validates the onboarding request and approvals.
- Creates the user identity.
- Assigns approved licences, groups and roles.
- Configures security controls.
- Records each access change.
- Verifies that the account works as intended.

### Application or data owner

The owner:

- Approves access to sensitive or specialised resources.
- Confirms the appropriate access level.
- Reviews privileged or exceptional access.

### New user

The user:

- Completes initial sign-in.
- Changes any temporary password.
- Registers approved MFA methods.
- Accepts security and acceptable-use requirements.
- Reports access problems without sharing passwords or MFA codes.

## Required onboarding request

The onboarding request must contain:

- Full name
- Personal or employee identifier approved for administrative use
- Job title
- Department
- Manager
- Worker type
- Start date
- End date for temporary access
- Required location
- Required applications
- Required licence type
- Required groups or business roles
- Device requirement
- Access approvals
- Ticket or request reference

The request must not contain:

- Passwords
- MFA codes
- Personal access tokens
- API keys
- Unnecessary personal information
- Customer information

## Procedure

### 1. Validate the request

The administrator must confirm that:

- The request came from an authorised source.
- The hiring manager approved the onboarding.
- The start date is confirmed.
- The worker’s role and department are clear.
- Requested access matches the role.
- Sensitive or privileged access has system-owner approval.
- Temporary access has an expiry date.

If required information or approval is missing, pause the onboarding and request clarification.

### 2. Check for an existing identity

Before creating an account:

- Search for an existing active account.
- Search for a disabled or archived account.
- Check for naming conflicts.
- Confirm that a returning worker is handled according to the account-recovery policy.
- Never create a duplicate identity merely to bypass an access problem.

### 3. Create the primary identity

Create the account in the organisation’s identity platform.

Example platforms include:

- Microsoft Entra ID
- Microsoft 365
- Google Workspace
- Okta

Configure:

- Display name
- Unique username
- Primary email address
- Department
- Job title
- Manager
- Worker type
- Usage location
- Start date
- End date when applicable

The account must be created for one named person. Shared credentials are not permitted.

### 4. Configure initial authentication

Apply the organisation’s approved initial sign-in method.

Requirements:

- Use a secure temporary credential or passwordless enrolment process.
- Deliver initial access information through an approved secure channel.
- Require a password change at first sign-in when a temporary password is used.
- Require MFA registration.
- Never place a password or MFA code in the onboarding ticket.
- Do not ask the user to send a password or authentication code back to IT.

### 5. Assign licences

Assign only licences required for the role.

Examples may include:

- Email and calendar
- Office or collaboration applications
- Video conferencing
- Endpoint management
- Security and compliance services
- Specialist business applications

Record the assigned licence type. Avoid assigning premium licences without a documented requirement.

### 6. Assign groups and roles

Use group-based access whenever possible.

Example access path:

User → Department group → Business role → Permission → Resource

For a fictional Support Analyst, approved access might include:

- All Employees group
- Support Department group
- Service Desk application user role
- Internal knowledge-base reader role
- Standard collaboration licence

Do not assign:

- Global administrator
- Security administrator
- Billing administrator
- Application owner
- Data export permission
- Unrestricted shared-drive access

unless the role specifically requires it and the correct owner has approved it.

### 7. Apply least privilege

For every requested permission, confirm:

- Is this access required for the user’s current duties?
- Is a read-only role sufficient?
- Can access be granted through an existing approved group?
- Is an expiry date required?
- Does the access create a conflict of duties?
- Is privileged access being assigned to a separate administrative account?

If a lower level of access meets the business requirement, use the lower level.

### 8. Configure application access

Provision approved applications through:

- Group membership
- SSO assignment
- Role assignment
- Licence assignment
- Automated provisioning where available

Avoid manually creating separate application passwords when central identity and SSO are supported.

For each application, record:

- Application name
- Assigned role
- Approval source
- Date granted
- Expiry date when applicable
- Administrator who completed the change

### 9. Prepare and secure the endpoint

If a company-managed device is required:

- Record the approved asset identifier.
- Enrol the device in the endpoint-management or MDM platform.
- Apply the correct security baseline.
- Enable disk encryption.
- Enable endpoint protection.
- Apply current operating-system and application updates.
- Configure screen-lock requirements.
- Confirm firewall status.
- Confirm device compliance.
- Restrict local administrator access.
- Verify remote support capability according to policy.

Personal devices must not receive organisational data unless they meet the approved BYOD and MDM requirements.

### 10. Apply conditional access

Where available, apply policies requiring:

- MFA
- Approved authentication methods
- Compliant or managed devices
- Approved locations where appropriate
- Blocked legacy authentication
- Increased protection for privileged roles

Do not exclude a user from security controls merely to make onboarding faster. Any exception must be approved, documented and time-limited.

### 11. Verify the account

Test or confirm:

- Account is enabled at the correct time.
- User can complete sign-in.
- MFA registration succeeds.
- Email and calendar work.
- Required applications are visible.
- Approved resources can be accessed.
- Unapproved privileged resources remain inaccessible.
- Device appears compliant.
- SSO works where configured.
- No unexpected permission error appears.

Testing must not require the administrator to know or retain the user’s password.

### 12. Provide the user with guidance

Provide:

- Sign-in address
- Username
- Secure initial-access instructions
- MFA registration instructions
- Password-reset instructions
- Security-awareness information
- Support contact method
- Instructions for reporting suspicious sign-in activity
- List of approved business applications

Do not send confidential access information through an unapproved channel.

### 13. Record the completed changes

The onboarding record should include:

| Field | Example |
|---|---|
| Request reference | NS-ONB-2026-001 |
| User | Fictional User |
| Department | Support |
| Manager approval | Confirmed |
| Identity created | Yes |
| MFA required | Yes |
| Licences assigned | Standard productivity licence |
| Groups assigned | All Employees, Support Department |
| Application roles | Service Desk User |
| Device assigned | Fictional asset reference |
| Completion date | Fictional date |
| Completed by | Administrator role |
| Follow-up review | Scheduled |

Do not record passwords, recovery codes, access tokens or unnecessary personal information.

### 14. Obtain user and manager confirmation

Confirm that:

- The user can sign in.
- Required access works.
- The manager agrees that the access is appropriate.
- No unnecessary access was granted.
- Outstanding problems have separate support records.

### 15. Perform a post-onboarding review

Review access after an appropriate period, such as 7 or 30 days.

Check:

- Whether all assigned licences are being used.
- Whether temporary access should expire.
- Whether the user received excessive permissions.
- Whether group membership matches the current role.
- Whether the device remains compliant.
- Whether unresolved access problems remain.

Remove unnecessary access promptly.

## Exception handling

If onboarding cannot be completed:

1. Record the exact failed step.
2. Record the visible error without including secrets.
3. Confirm identity-platform and application status.
4. Check licence availability.
5. Check group and role assignments.
6. Check conditional-access requirements.
7. Confirm device compliance.
8. Escalate to the correct system owner.
9. Document the resolution.
10. Verify access with the user.

Emergency access must be:

- Explicitly approved
- Limited in scope
- Time-limited
- Logged
- Reviewed after use
- Removed when no longer required

## Completion criteria

Onboarding is complete only when:

- The identity is active.
- MFA is configured.
- Required licences are assigned.
- Approved groups and roles are assigned.
- Required applications work.
- The endpoint is compliant when applicable.
- The user and manager confirm access.
- All changes are documented.
- A follow-up access review is scheduled.