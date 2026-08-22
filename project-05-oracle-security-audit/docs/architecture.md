# Architecture

The Oracle Security & Audit Platform follows a layered
enterprise architecture.

```text
+------------------------------------------+
|              User / Security Team        |
+----------------------+-------------------+
                       |
                       v
+------------------------------------------+
|             Streamlit Dashboard          |
+----------------------+-------------------+
                       |
                       v
+------------------------------------------+
|          Security Monitoring Layer       |
|                                          |
| Users | Privileges | Roles | Audit       |
| Risk  | Compliance                     |
+----------------------+-------------------+
                       |
                       v
+------------------------------------------+
|              Repository Layer            |
+----------------------+-------------------+
                       |
                       v
+------------------------------------------+
|          Oracle Connection Pool          |
+----------------------+-------------------+
                       |
                       v
+------------------------------------------+
|              Oracle Database             |
+------------------------------------------+

---

Security Monitoring Domains
Identity

Monitors database users and account status.

Authorization

Monitors:

System privileges
Object privileges
Roles
Privileged users
Auditing

Monitors:

Authentication
Database actions
Object activity
Failed logins
Compliance

Evaluates account security findings.

Risk

Assigns severity and risk scores.
