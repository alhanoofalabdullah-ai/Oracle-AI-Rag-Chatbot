# Oracle Database Management & Health Monitoring

## Overview

Oracle Database Management & Health Monitoring is an enterprise-oriented
database monitoring platform built with Python, Oracle Database, SQL,
and Streamlit.

The platform provides centralized visibility into:

- Database health
- Database status
- Instance information
- Tablespace utilization
- Session activity
- SQL performance
- Wait events
- Operational health reports

---

## Architecture

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

## Features

- Database Health
- Database status
- Open mode
- Database role
- Protection mode
- Instance status
- Startup time

## Storage Monitoring

- Tablespace capacity
- Used space
- Free space
- Utilization percentage
- Warning status
- Critical status

## Session Monitoring

- Total sessions
- Active sessions
- Sessions by user
- Sessions by machine
- Long-running sessions

## Performance Monitoring

- Oracle system metrics
- Top SQL
- CPU time
- Elapsed time
- Buffer gets
- Physical reads
- Wait events

## Reporting

Generate JSON operational health reports.

---

## Technology Stack

| Technology      | Purpose             |
| --------------- | ------------------- |
| Python          | Application         |
| Oracle Database | Database            |
| SQL             | Monitoring          |
| python-oracledb | Oracle connectivity |
| Pandas          | Data processing     |
| Streamlit       | Dashboard           |
| Pytest          | Testing             |
| Docker          | Containerization    |
| GitHub          | Version control     |


---

Installation

1. Clone

git clone https://github.com/alhanoofalabdullah-ai/Oracle-System-Projects.git

2. Navigate

cd Oracle-System-Projects/project-02-oracle-database-management

3. Create environment

python3 -m venv .venv

4. Activate

source .venv/bin/activate

Windows:

.venv\Scripts\activate

5. Install

pip install -r requirements.txt

---

## Configuration

Copy:

.env.example

to:

.env

Configure:

ORACLE_USER=monitoring_user
ORACLE_PASSWORD=change_me
ORACLE_DSN=localhost:1521/FREEPDB1

Run

streamlit run app/main.py

Open:

http://localhost:8501

---

Testing
Run:

pytest -v

---

Docker

Build:

docker build -t oracle-database-management .

Run:

docker run \
  --env-file .env \
  -p 8501:8501 \
  oracle-database-management

Or:

docker compose up --build

---

## Project Structure

project-02-oracle-database-management/
│
├── app/
│   ├── database/
│   ├── monitoring/
│   ├── reports/
│   └── ui/
│
├── sql/
├── tests/
├── docs/
├── reports/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── pyproject.toml
├── .env.example
├── .gitignore
├── LICENSE
└── README.md

---

Monitoring Model

The project follows four operational dimensions:

Availability
     |
     v
Capacity
     |
     v
Activity
     |
     v
Performance

---


Security
The project follows basic security principles:
•	Credentials are stored in environment variables. 
•	.env is excluded from Git. 
•	Production credentials should use a secrets manager. 
•	Least privilege should be applied. 
•	Production monitoring output should not be publicly exposed. 
 
Roadmap
•	Oracle connection 
•	Database health 
•	Instance information 
•	Tablespace monitoring 
•	Session monitoring 
•	Performance monitoring 
•	Streamlit dashboard 
•	JSON reporting 
•	Automated tests 
•	Docker support 
Future:
•	Historical metrics 
•	Email alerts 
•	Teams notifications 
•	Multi-database support 
•	Authentication 
•	RBAC 
•	Prometheus 
•	Grafana 
•	AWR 
•	ASH 
•	Advanced SQL tuning 
 
Use Cases
The platform can support:
•	Oracle database administration 
•	IT operations 
•	Application support 
•	Database engineering 
•	DevOps monitoring 
•	Enterprise systems 
•	Capacity planning 
•	Performance investigation 
 
Portfolio Value
This project demonstrates practical experience with:
•	Oracle Database 
•	SQL 
•	Python 
•	Database connectivity 
•	Monitoring 
•	Automation 
•	Dashboard development 
•	Testing 
•	Docker 
•	Technical documentation 
•	Enterprise architecture 
 
Author
Alhanoof Alabdullah
