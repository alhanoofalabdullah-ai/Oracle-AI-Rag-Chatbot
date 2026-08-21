# Oracle Performance Monitoring & SQL Tuning Platform

## Overview

Oracle Performance Monitoring & SQL Tuning Platform is an
enterprise-oriented monitoring solution designed to provide
visibility into Oracle Database performance.

The platform combines:

- Oracle Database
- Oracle SQL
- Python
- python-oracledb
- Pandas
- Streamlit
- Pytest
- Docker

The solution provides a centralized dashboard for database
performance analysis, SQL monitoring, session analysis,
wait-event analysis, and operational reporting.

---

# Objectives

The main objectives are:

- Monitor Oracle database performance.
- Identify expensive SQL statements.
- Analyze CPU consumption.
- Analyze elapsed time.
- Analyze logical and physical I/O.
- Monitor active sessions.
- Identify long-running sessions.
- Analyze Oracle wait events.
- Monitor system statistics.
- Generate operational performance reports.

---

# Architecture

```text
                         +----------------------+
                         |        User          |
                         +----------+-----------+
                                    |
                                    v
                         +----------------------+
                         |  Streamlit Dashboard |
                         +----------+-----------+
                                    |
                                    v
                  +------------------------------------+
                  |       Monitoring Services          |
                  |                                    |
                  | Performance | SQL | Sessions       |
                  | Wait Events | Health | Metrics     |
                  +----------------+-------------------+
                                   |
                                   v
                         +----------------------+
                         | Repository Layer     |
                         +----------+-----------+
                                    |
                                    v
                         +----------------------+
                         | Oracle Connection     |
                         | Pool                  |
                         +----------+-----------+
                                    |
                                    v
                         +----------------------+
                         |   Oracle Database     |
                         +----------------------+

Key Features
1. Database Performance Health
The dashboard provides:
•	Database name 
•	Open mode 
•	Database role 
•	Instance name 
•	Instance status 
•	Host name 
 
2. System Metrics
The system collects Oracle performance metrics including:
•	Database activity 
•	System metrics 
•	Performance indicators 
•	Database statistics 
 
3. SQL Performance Analysis
The platform analyzes SQL statements using:
•	SQL ID 
•	Parsing schema 
•	Executions 
•	Total elapsed time 
•	Average elapsed time 
•	CPU time 
•	Buffer gets 
•	Disk reads 
•	Rows processed 
 
4. Top SQL
SQL statements can be analyzed according to:
Elapsed Time
Identifies SQL statements consuming the most total
database elapsed time.
CPU
Identifies SQL statements consuming the most CPU.
I/O
Identifies SQL statements generating high physical I/O.
 
SQL Performance Classification
SQL statements are classified using configurable thresholds.
                 SQL Performance
                       |
          +------------+------------+
          |                         |
       < 5 sec                  >= 5 sec
          |                         |
       HEALTHY                  WARNING
                                    |
                                  >= 30 sec
                                    |
                                CRITICAL

Default thresholds:
Classification	Threshold
Healthy	< 5 seconds
Warning	>= 5 seconds
Critical	>= 30 seconds

These values can be customized through environment variables.


 
5. Wait Event Analysis
The platform monitors Oracle wait events.
Examples include:
•	I/O waits 
•	Concurrency waits 
•	Configuration waits 
•	Application waits 
•	Network-related waits 
Idle events are excluded from the primary performance view.
 
6. Session Monitoring
The application provides:
•	Active session count 
•	Active session details 
•	Long-running sessions 
•	Username 
•	Machine 
•	Program 
•	SQL ID 
•	Current event 
•	Wait class 
 
7. I/O Analysis
The SQL layer provides visibility into:
•	Data files 
•	File size 
•	Physical reads 
•	Physical writes 
•	Read time 
•	Write time 
•	Single block reads 


8. Reporting
The platform can generate JSON performance reports containing:
Database Health
System Metrics
Top SQL
Wait Events
Sessions
Generation Timestamp
Reports are stored in:
reports/

Technology Stack

Technology	Purpose
Python 3.11+	Application logic
Oracle Database	Database platform
Oracle SQL	Performance monitoring
python-oracledb	Database connectivity
Pandas	Data processing
Streamlit	Dashboard
Pytest	Automated testing
Docker	Containerization
GitHub	Version control


Project Structure

project-03-oracle-performance-monitoring/
│
├── app/
│   ├── database/
│   │   ├── connection.py
│   │   └── repository.py
│   │
│   ├── monitoring/
│   │   ├── performance.py
│   │   ├── sql_analysis.py
│   │   ├── wait_events.py
│   │   ├── sessions.py
│   │   ├── system_metrics.py
│   │   └── health.py
│   │
│   ├── reports/
│   │   └── generator.py
│   │
│   └── ui/
│       └── dashboard.py
│
├── sql/
│   ├── 01_system_metrics.sql
│   ├── 02_top_sql.sql
│   ├── 03_sql_tuning.sql
│   ├── 04_wait_events.sql
│   ├── 05_session_analysis.sql
│   ├── 06_io_analysis.sql
│   └── 07_performance_health.sql
│
├── tests/
│   ├── test_performance.py
│   ├── test_sql_analysis.py
│   └── test_thresholds.py
│
├── docs/
│   ├── architecture.md
│   ├── performance-monitoring.md
│   ├── sql-tuning.md
│   └── troubleshooting.md
│
├── reports/
├── screenshots/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── pyproject.toml
├── .env.example
├── .gitignore
├── LICENSE
└── README.md


Installation
Step 1 — Clone the repository

git clone https://github.com/alhanoofalabdullah-ai/Oracle-AI-Rag-Chatbot


Step 2 — Navigate to Project 03

cd Oracle-System-Projects/project-03-oracle-performance-monitoring


Step 3 — Create Python environment

python3 -m venv .venv


Step 4 — Activate environment

source .venv/bin/activate
Windows:
.venv\Scripts\activate


Step 5 — Install dependencies

Configuration
Create .env from .env.example.
cp .env.example .env
Configure:
ORACLE_USER=monitoring_user

ORACLE_PASSWORD=change_me

ORACLE_DSN=localhost:1521/FREEPDB1

Host: localhost
Port: 1521
Service: FREEPDB1
DSN:

localhost:1521/FREEPDB1


Running the Dashboard
Run:
streamlit run app/main.py

Testing
Run:
pytest -v

Expected result:

All tests passed


Docker
Build
docker build \
  -t oracle-performance-monitoring .

Run

docker run \
  --env-file .env \
  -p 8501:8501 \
  oracle-performance-monitoring


Docker Compose
Run:
docker compose up –build

Stop:

docker compose down


Monitoring Workflow

Oracle Database
       |
       v
Collect Metrics
       |
       v
Analyze Performance
       |
       +------------------+
       |                  |
       v                  v
    Top SQL          Wait Events
       |                  |
       +---------+--------+
                 |
                 v
          Session Analysis
                 |
                 v
        Performance Health
                 |
                 v
        Streamlit Dashboard
                 |
                 v
          JSON Report


SQL Tuning Workflow

Identify SQL
     |
     v
Check SQL_ID
     |
     v
Review Executions
     |
     v
Review Elapsed Time
     |
     v
Review CPU
     |
     v
Review Buffer Gets
     |
     v
Review Physical Reads
     |
     v
Review Wait Events
     |
     v
Review Execution Plan
     |
     v
Optimize
     |
     v
Validate Performance


Performance Indicators
Elapsed Time
Measures the total time consumed by SQL execution.
 
CPU Time
Helps identify CPU-intensive SQL.
 
Buffer Gets
Provides visibility into logical reads.
 
Disk Reads
Helps identify SQL statements generating
physical I/O.
 
Executions
Provides context for SQL resource consumption.
 
Recommended SQL Investigation
When a SQL statement appears as a top consumer:
1.	Identify the SQL ID. 
2.	Review execution frequency. 
3.	Review average elapsed time. 
4.	Review CPU consumption. 
5.	Review logical reads. 
6.	Review physical reads. 
7.	Review wait events. 
8.	Review execution plan. 
9.	Evaluate indexes. 
10.	Validate query predicates. 
11.	Test optimization. 
12.	Compare before/after performance. 
 
Security
Security considerations include:
•	Environment-based credentials. 
•	.env excluded from Git. 
•	Dedicated monitoring account. 
•	Least-privilege access. 
•	No hard-coded production passwords. 
•	Secure database connectivity. 
•	Restricted dashboard access. 
Production deployments should use a secure secrets
management solution.
 
Operational Use Cases
The platform can be used for:
•	Oracle Database Administration 
•	Database Performance Engineering 
•	SQL Tuning 
•	IT Operations 
•	Application Support 
•	Enterprise Systems 
•	Capacity Planning 
•	Performance Troubleshooting 
•	Database Monitoring 
•	DevOps Operations 
 
Future Enhancements
Planned enhancements include:
•	Historical performance repository 
•	Time-series metrics 
•	Grafana integration 
•	Prometheus integration 
•	Email alerts 
•	Microsoft Teams alerts 
•	Slack alerts 
•	Multi-database monitoring 
•	Authentication 
•	Role-Based Access Control 
•	AWR integration 
•	ASH integration 
•	Execution plan visualization 
•	Automatic anomaly detection 
•	AI-assisted SQL tuning recommendations 
 
Portfolio Skills Demonstrated
This project demonstrates practical knowledge of:
•	Oracle Database 
•	Oracle SQL 
•	Python 
•	Database Connectivity 
•	SQL Performance Analysis 
•	SQL Tuning 
•	Database Monitoring 
•	Performance Engineering 
•	Session Analysis 
•	Wait Event Analysis 
•	I/O Analysis 
•	Streamlit 
•	REST-ready architecture 
•	Automated Testing 
•	Docker 
•	Technical Documentation 
•	Enterprise Architecture 
 
Project Position in Oracle Portfolio
This project is part of a broader Oracle engineering portfolio.

Author
Alhanoof Alabdullah
<img width="468" height="640" alt="image" src="https://github.com/user-attachments/assets/3c669648-074e-49f3-a500-35b1c2505152" />
