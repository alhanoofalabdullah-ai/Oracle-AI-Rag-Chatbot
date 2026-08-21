# Architecture

## Overview

The project follows a layered architecture.

```text
User
 |
 v
Streamlit Dashboard
 |
 v
Monitoring Services
 |
 v
Repository Layer
 |
 v
Oracle Connection Pool
 |
 v
Oracle Database

---

Layers

Presentation

Streamlit dashboard.

Monitoring

Business and monitoring logic.

Repository

Database query execution.

Connection

Oracle connection pooling.

Database

Oracle Database dynamic performance and data dictionary views.

---

