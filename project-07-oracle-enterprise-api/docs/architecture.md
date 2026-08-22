# Architecture

The project implements a layered enterprise integration architecture.

```text
Client Applications
        |
        v
REST API
        |
        v
API Services
        |
        v
PL/SQL Business Logic
        |
        v
Oracle Database

---

Layers


Presentation

REST API endpoints.

Service

Business logic and orchestration.

Database

Oracle tables, views, packages, constraints and indexes.

Audit

Request and error logging.

Security

Authentication and database roles.

---
