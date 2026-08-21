
---

# Troubleshooting

## RMAN Not Found

Verify:

```bash
which rman

Windows:

where rman

---

Oracle Connection Failure
Verify:
•	Oracle Listener 
•	Host 
•	Port 
•	Service Name 
•	Username 
•	Password 

Example:
localhost:1521/FREEPDB1

---

Backup Failure

Check:

SELECT
    session_key,
    input_type,
    status,
    start_time,
    completion_time
FROM v$rman_backup_job_details
WHERE status <> 'COMPLETED';

---

Archive Gap

Run:

SELECT
    thread#,
    low_sequence#,
    high_sequence#
FROM v$archive_gap;

If rows are returned, investigate the missing archive
log sequences.

---

Missing Controlfile Backup

Run:

SELECT
    MAX(completion_time)
FROM v$rman_backup_job_details
WHERE input_type = 'CONTROLFILE'
AND status = 'COMPLETED';

---

Dashboard Error

Run:
pytest -v

Then verify:
streamlit run app/main.py

---

