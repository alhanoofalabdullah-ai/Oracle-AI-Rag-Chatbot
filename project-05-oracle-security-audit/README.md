# Oracle Database Security & Audit Platform
---

## Overview

Oracle Database Security & Audit Platform is an
enterprise-oriented security monitoring solution designed
to provide visibility into Oracle database users,
privileges, roles, authentication activity, audit events
and security compliance findings.

The project combines Oracle Database, Oracle SQL, Python,
Streamlit and automated testing to create a centralized
security operations dashboard.

---

# Objectives

The platform focuses on:

- Oracle database security
- User account monitoring
- Privilege monitoring
- Role monitoring
- Privileged access monitoring
- Authentication monitoring
- Failed login detection
- Audit event monitoring
- Password expiration monitoring
- Security risk scoring
- Compliance findings
- Security reporting

---

# Architecture

```text
                       +----------------------+
                       |        Security      |
                       |         Team         |
                       +----------+-----------+
                                  |
                                  v
                       +----------------------+
                       | Streamlit Dashboard  |
                       +----------+-----------+
                                  |
                                  v
              +------------------------------------------+
              |         Security Monitoring Layer        |
              |                                          |
              | Users | Privileges | Roles | Audit       |
              | Risk  | Compliance                       |
              +--------------------+---------------------+
                                   |
                                   v
                       +----------------------+
                       | Repository Layer     |
                       +----------+-----------+
                                  |
                                  v
                       +----------------------+
                       | Oracle Connection    |
                       | Pool                 |
                       +----------+-----------+
                                  |
                                  v
                       +----------------------+
                       | Oracle Database      |
                       +----------------------+


Key Features
1. Database User Monitoring
The platform monitors:
•	Username 
•	Account status 
•	Creation date 
•	Lock date 
•	Password expiration 
•	Profile 
•	Authentication type 
•	Default tablespace 
 
2. Privilege Monitoring
The platform identifies powerful privileges such as:
ALTER SYSTEM
CREATE USER
DROP USER
GRANT ANY PRIVILEGE
GRANT ANY ROLE
SELECT ANY DICTIONARY
CREATE ANY TABLE
DROP ANY TABLE


This provides visibility into potentially high-impact database permissions.



3. Role Monitoring
The platform monitors:
•	Database roles 
•	Role membership 
•	DBA assignments 
•	Administrative role assignments 
•	Default roles 
•	Admin options 
 
4. Audit Monitoring
The platform analyzes Unified Audit events.
Examples:
Successful Login
Failed Login
Database Action
Object Access
Administrative Activity


5. Failed Login Monitoring
Failed authentication events are surfaced in the dashboard.
Example risk thresholds:
Attempts	Severity
0–4	LOW
5–9	HIGH
10+	CRITICAL
These are portfolio defaults and should be tuned to
organizational requirements.
 
6. Security Risk Engine
The Python risk engine converts security observations
into findings.
Example:
Finding
   |
   +-- Category
   |
   +-- Severity
   |
   +-- Score
   |
   +-- Description
   |
   +-- Recommendation


7. Compliance Monitoring
The platform can identify:
•	Expired accounts 
•	Locked accounts 
•	Accounts requiring review 
•	Privileged users 
•	High-risk privileges 
 
8. Security Reporting
The platform generates JSON reports containing:
•	User inventory 
•	Privileged users 
•	Failed logins 
•	Audit events 
•	Security findings 
 
Technology Stack
Technology	Purpose
Oracle Database	Database platform
Oracle SQL	Security queries
Python	Automation
python-oracledb	Oracle connectivity
Pandas	Data processing
Streamlit	Security dashboard
Pytest	Automated testing
Docker	Containerization
GitHub	Version control
 

Project Structure
project-05-oracle-security-audit/
│
├── app/
│   ├── database/
│   ├── security/
│   ├── reports/
│   └── ui/
│
├── sql/
│
├── policies/
│
├── tests/
│
├── docs/
│
├── reports/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── pyproject.toml
├── .env.example
├── .gitignore
├── LICENSE
└── README.md


Create Virtual Environment
python3 -m venv .venv

Linux/macOS:
source .venv/bin/activate

Windows:
.venv\Scripts\activate


Install Dependencies
pip install -r requirements.txt


Configuration
Copy the environment template:
cp .env.example .env

Configure the Oracle connection:
ORACLE_USER=security_monitor
ORACLE_PASSWORD=change_me
ORACLE_DSN=localhost:1521/FREEPDB1


Run Tests

pytest -v

Expected result:
tests/test_risk.py
tests/test_users.py
tests/test_compliance.py


Security Architecture
The project follows several security principles.
Least Privilege
Monitoring accounts should receive only the permissions
required for monitoring.
 
Credential Protection
Credentials are stored outside source code:
.env
The .env file is excluded from Git.


Role-Based Access
The project provides visibility into role-based access
assignments.
 
Privileged Access Monitoring
High-impact privileges are explicitly monitored.
 
Security Monitoring Workflow
                 Oracle Database
                       |
                       v
               Collect Security Data
                       |
        +--------------+--------------+
        |              |              |
        v              v              v
      Users       Privileges        Audit
        |              |              |
        +--------------+--------------+
                       |
                       v
                Risk Evaluation
                       |
                       v
                Security Findings
                       |
                       v
                 Dashboard
                       |
                       v
                   Report


Security Use Cases
The platform can support:
•	Oracle DBA Operations 
•	Database Security 
•	Security Operations 
•	Identity & Access Management 
•	Privileged Access Monitoring 
•	Compliance 
•	Audit 
•	Incident Investigation 
•	Enterprise Systems 
•	Production Support 
 
Skills Demonstrated
This project demonstrates practical knowledge of:
•	Oracle Database Security 
•	Oracle SQL 
•	Database Users 
•	Roles 
•	System Privileges 
•	Object Privileges 
•	Unified Auditing 
•	Authentication Monitoring 
•	Security Risk Assessment 
•	Compliance Monitoring 
•	Python 
•	Streamlit 
•	Pandas 
•	Automated Testing 
•	Docker 
•	Technical Documentation 
 
Future Enhancements
Potential enhancements include:
•	Real-time security alerts 
•	Email notifications 
•	Microsoft Teams integration 
•	SIEM integration 
•	Splunk integration 
•	Microsoft Sentinel integration 
•	Grafana dashboards 
•	Prometheus metrics 
•	Security event correlation 
•	AI-based anomaly detection 
•	Automated privilege review 
•	Password policy scoring 
•	Security baseline comparison 
•	Multi-database monitoring 
•	Oracle Data Guard security monitoring 
•	Centralized audit management 
 
Portfolio Roadmap
This project is the fifth project in the Oracle portfolio.
Project 01
Oracle AI / Intelligent Database Application
        |
        v
Project 02
Oracle Database Management & Health
        |
        v
Project 03
Oracle Performance Monitoring & SQL Tuning
        |
        v
Project 04
Oracle Backup, Recovery & Disaster Recovery
        |
        v
Project 05
Oracle Database Security & Audit


Author
Alhanoof Alabdullah




<img width="468" height="649" alt="image" src="https://github.com/user-attachments/assets/e0c7d592-456c-48bb-88a5-40f1df358d0b" />
