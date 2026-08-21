# Oracle Backup, Recovery & Disaster Recovery Platform

---

## Overview

Oracle Backup, Recovery & Disaster Recovery Platform is an
enterprise-oriented solution for monitoring Oracle database
backup operations, recovery readiness, archive logs and
disaster recovery indicators.

The platform combines:

- Oracle Database
- Oracle RMAN
- Oracle SQL
- Python
- python-oracledb
- Pandas
- Streamlit
- Pytest
- Docker

The solution provides a centralized operational dashboard
for backup and recovery monitoring.

---

# Objectives

The project focuses on:

- Oracle backup monitoring
- RMAN backup history
- Backup health
- Recovery readiness
- Archive log monitoring
- Archive gap detection
- Controlfile backup monitoring
- SPFILE backup monitoring
- Recovery status
- Database role monitoring
- Backup validation
- Retention management
- Operational reporting

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
                 +---------------------------------------+
                 |       Backup & Recovery Services       |
                 |                                       |
                 | Backup | RMAN | Archive | Recovery    |
                 +-------------------+-------------------+
                                     |
                                     v
                         +----------------------+
                         | Repository Layer    |
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
                         | Oracle Database       |
                         +----------------------+

Key Features
1. Backup Health Monitoring
The platform evaluates:
•	Last successful backup 
•	Backup age 
•	Controlfile backup 
•	Backup status 
Default classification:
Status	Condition
HEALTHY	Backup within 24 hours
WARNING	Backup between 24–48 hours
CRITICAL	Backup older than 48 hours
 
2. RMAN Backup Monitoring
The dashboard provides:
•	Backup history 
•	Backup type 
•	Backup status 
•	Start time 
•	Completion time 
•	Duration 
•	Input size 
•	Output size 
•	Compression ratio 
 
3. Backup Types
The project demonstrates:
Full Database Backup
Database
+
Controlfile
+
SPFILE

Incremental Backup
Level 1 incremental backup.
Archive Log Backup
Protects archived redo logs.
Controlfile Backup
Dedicated controlfile protection.
SPFILE Backup
Dedicated database configuration backup.
 
4. Recovery Monitoring
The platform monitors:
•	Recovery status 
•	Database role 
•	Open mode 
•	Protection mode 
•	Protection level 
•	Instance status 
 
5. Archive Log Monitoring
The system monitors:
•	Archive log counts 
•	Sequence ranges 
•	Archive destinations 
•	Archive destination errors 
•	Archive gaps 
An archive gap can indicate missing archive logs that
may affect recovery readiness.
 
6. RMAN Validation
The project includes RMAN validation operations:
VALIDATE DATABASE
VALIDATE BACKUPSET ALL
VALIDATE ARCHIVELOG ALL

Production retention policies must be designed according to business requirements, compliance, RPO, RTO and storage capacity.


RPO
Recovery Point Objective describes the maximum acceptable
data loss.
Example:
RPO = 15 minutes

RTO
Recovery Time Objective describes the maximum acceptable
service restoration time.
Example:
RTO = 2 hours
Recovery Workflow
                 Incident
                    |
                    v
              Assess Database
                    |
                    v
              Identify RPO
                    |
                    v
              Validate Backup
                    |
                    v
             Restore Database
                    |
                    v
             Recover Database
                    |
                    v
            Validate Database
                    |
                    v
             Application Test
                    |
                    v
               Go Live


Backup Workflow
Database
   |
   +----------------------+
   |                      |
   v                      v
Full Backup         Incremental Backup
   |                      |
   +----------+-----------+
              |
              v
        Archive Logs
              |
              v
        Controlfile
              |
              v
           SPFILE
              |
              v
       Backup Validation
              |
              v
       Recovery Testing


Technology Stack
Technology	Purpose
Oracle Database	Database platform
RMAN	Backup & Recovery
Oracle SQL	Monitoring
Python	Automation
python-oracledb	Database connectivity
Pandas	Data processing
Streamlit	Dashboard
Pytest	Testing
Docker	Containerization
GitHub	Version control

Project Structure
project-04-oracle-backup-recovery/
│
├── app/
│   ├── database/
│   ├── backup/
│   ├── reports/
│   └── ui/
│
├── rman/
│   ├── 01_full_backup.rman
│   ├── 02_incremental_backup.rman
│   ├── 03_archivelog_backup.rman
│   ├── 04_controlfile_backup.rman
│   ├── 05_database_recovery.rman
│   ├── 06_backup_validation.rman
│   └── 07_cleanup_obsolete.rman
│
├── sql/
│   ├── 01_backup_history.sql
│   ├── 02_backup_status.sql
│   ├── 03_archivelog_monitoring.sql
│   ├── 04_recovery_status.sql
│   ├── 05_database_files.sql
│   ├── 06_rman_health.sql
│   └── 07_recovery_readiness.sql
│
├── tests/
│
├── docs/
│
├── reports/│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── pyproject.toml
├── .env.example
├── .gitignore
├── LICENSE
└── README.md
Python Environment
Create environment:
python3 -m venv .venv
Activate on Linux/macOS:
source .venv/bin/activate
Windows:
.venv\Scripts\activate

Install Dependencies
pip install -r requirements.txt

 
Configuration
Copy:
cp .env.example .env

Configure:
ORACLE_USER=monitoring_user
ORACLE_PASSWORD=change_me
ORACLE_DSN=localhost:1521/FREEPDB1

RMAN
Verify RMAN:
which rman
Then execute controlled scripts on an Oracle test
environment.
Example:
rman target / cmdfile=rman/01_full_backup.rman

 
Important Production Safety
Never execute RMAN cleanup or restore commands against
a production database without:
•	DBA approval 
•	Backup verification 
•	Change management 
•	Recovery plan 
•	Maintenance window 
•	Tested rollback procedure 
This repository is intended as a portfolio and training
implementation.
 
Security
The project follows several security practices:
•	Credentials stored in .env 
•	.env excluded from Git 
•	No production passwords in source code 
•	Dedicated monitoring user 
•	Least privilege 
•	Controlled RMAN execution 
•	Environment-specific configuration 
 
Monitoring Use Cases
The platform can support:
•	Oracle DBA Operations 
•	Backup Operations 
•	Disaster Recovery 
•	Business Continuity 
•	Database Administration 
•	IT Operations 
•	Enterprise Systems 
•	Production Support 
•	Recovery Readiness 
•	Operational Reporting 
 
Skills Demonstrated
This project demonstrates practical skills in:
•	Oracle Database 
•	Oracle RMAN 
•	Backup & Recovery 
•	Disaster Recovery 
•	RPO / RTO 
•	Archive Log Management 
•	Database Monitoring 
•	Python Automation 
•	SQL 
•	Streamlit 
•	Docker 
•	Automated Testing 
•	Technical Documentation 
•	Enterprise Architecture 
 
Future Enhancements
Potential enhancements:
•	Automated backup scheduling 
•	Email alerts 
•	Microsoft Teams notifications 
•	Slack notifications 
•	Grafana integration 
•	Prometheus integration 
•	Recovery Time tracking 
•	Backup SLA monitoring 
•	RPO compliance dashboard 
•	RTO tracking 
•	Multi-database monitoring 
•	Oracle Data Guard monitoring 
•	Standby database monitoring 
•	Automatic backup failure alerts 
•	Centralized backup history 
•	Object Storage integration 
•	Cloud backup integration 
•	AI-based recovery recommendations 
 
Portfolio Roadmap
This project is the fourth project in the Oracle
engineering portfolio.

 ---

Author
Alhanoof Alabdullah

<img width="468" height="649" alt="image" src="https://github.com/user-attachments/assets/43857dd2-dcba-4a85-a339-872cdc527243" />
