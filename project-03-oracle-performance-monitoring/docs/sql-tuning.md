# SQL Tuning

## SQL Performance Indicators

The project identifies SQL statements based on:

- Total elapsed time
- Average elapsed time
- CPU consumption
- Buffer gets
- Physical reads
- Number of executions

## Classification

```text
Healthy
   |
   | < 5 seconds
   v

Warning
   |
   | >= 5 seconds
   v

Critical
   |
   | >= 30 seconds

---

Recommended Investigation

When a SQL statement is classified as critical:

Identify the SQL ID.
Review execution count.
Review average elapsed time.
Review CPU consumption.
Review logical reads.
Review physical reads.
Review related wait events.
Review execution plan.
Check indexing strategy.
Validate query predicates.

---
