
---
# Recovery Strategy

## RPO

Recovery Point Objective defines the maximum acceptable
amount of data loss.

Example:

```text
RPO = 15 minutes

This normally requires frequent archive log protection.

RTO

Recovery Time Objective defines the target time to restore
business service.

Example:

RTO = 2 hours

Recovery Workflow

Incident
   |
   v
Assess Database
   |
   v
Identify Recovery Point
   |
   v
Validate Backups
   |
   v
Restore Database
   |
   v
Recover Database
   |
   v
Validate Objects
   |
   v
Open Database
   |
   v
Application Validation

---

Recovery Testing
Recovery should be tested regularly.
Testing should validate:
•	Backup integrity 
•	Restore process 
•	Archive logs 
•	Controlfile recovery 
•	SPFILE recovery 
•	Database consistency 
•	Application connectivity 

