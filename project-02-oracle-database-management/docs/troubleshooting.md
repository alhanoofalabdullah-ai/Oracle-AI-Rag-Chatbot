# Troubleshooting

## ORA-01017

Invalid username/password.

Verify the Oracle credentials.

---

## ORA-00942

The monitoring account may not have access to the required
Oracle view.

---

## ORA-01031

The monitoring account may not have sufficient privileges.

---

## Connection refused

Verify:

- Oracle listener
- Host
- Port
- Service name
- DSN

Example:

localhost:1521/FREEPDB1

---

## Streamlit error

Run:

```bash
pip install -r requirements.txt
