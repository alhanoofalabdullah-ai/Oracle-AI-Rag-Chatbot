
---

# Security Model

## Principle of Least Privilege

Users should only receive the permissions required
to perform their responsibilities.

---

## Privilege Categories

### System Privileges

Examples:

- CREATE USER
- ALTER SYSTEM
- SELECT ANY DICTIONARY
- GRANT ANY PRIVILEGE

---

### Object Privileges

Examples:

- SELECT
- INSERT
- UPDATE
- DELETE
- EXECUTE

---

## Role-Based Access

Roles should be preferred over uncontrolled direct
privilege assignments where appropriate.

Example:

```text
User
 |
 +---- Role
       |
       +---- SELECT
       +---- INSERT
       +---- EXECUTE

---

Privileged Access

Privileged accounts should be:

- Identified
- Reviewed
- Monitored
- Audited
- Protected

---

Account Lifecycle

Create
  |
  v
Active
  |
  v
Review
  |
  +----> Lock
  |
  +----> Disable
  |
  v
Retire

---
