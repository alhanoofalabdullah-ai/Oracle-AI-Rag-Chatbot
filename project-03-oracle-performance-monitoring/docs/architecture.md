# Architecture

## Overview

Oracle Performance Monitoring Platform follows a layered
enterprise architecture.

```text
+-----------------------------+
|       Streamlit UI          |
+-------------+---------------+
              |
              v
+-----------------------------+
|     Monitoring Services     |
+-------------+---------------+
              |
              v
+-----------------------------+
|       Repository Layer      |
+-------------+---------------+
              |
              v
+-----------------------------+
|    Oracle Connection Pool   |
+-------------+---------------+
              |
              v
+-----------------------------+
|       Oracle Database       |
+-----------------------------+

---

Components
UI

Provides:

Performance dashboard
SQL analysis
Session monitoring
Wait-event monitoring
Report generation
Monitoring Layer

Contains business logic for:

Performance
SQL analysis
Sessions
Wait events
System metrics
Health
Repository Layer

Responsible for executing Oracle SQL.

Connection Layer

Uses Oracle connection pooling to efficiently
manage database connections.

Reporting

Produces machine-readable JSON performance reports.

---
