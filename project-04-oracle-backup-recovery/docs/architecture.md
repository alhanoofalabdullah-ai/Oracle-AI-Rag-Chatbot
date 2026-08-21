# Architecture

The Oracle Backup & Recovery Platform uses a layered architecture.

```text
+--------------------------------------+
|          Streamlit Dashboard         |
+------------------+-------------------+
                   |
                   v
+--------------------------------------+
|       Backup / Recovery Services     |
|                                      |
| Backup | RMAN | Archive | Recovery   |
+------------------+-------------------+
                   |
                   v
+--------------------------------------+
|           Repository Layer           |
+------------------+-------------------+
                   |
                   v
+--------------------------------------+
|        Oracle Connection Pool        |
+------------------+-------------------+
                   |
                   v
+--------------------------------------+
|           Oracle Database            |
+--------------------------------------+

---

Main Components
Backup Monitoring
Monitors:
•	RMAN backup history 
•	Backup status 
•	Backup type 
•	Backup duration 
•	Backup size 
Recovery Monitoring
Monitors:
•	Database role 
•	Recovery status 
•	Instance status 
•	Protection mode 
Archive Monitoring
Monitors:
•	Archive log generation 
•	Archive destinations 
•	Archive gaps 
RMAN Layer
Provides controlled RMAN command files for:
•	Full backup 
•	Incremental backup 
•	Archive log backup 
•	Controlfile backup 
•	Validation 
•	Retention management 

---

