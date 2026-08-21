
---

# `docs/troubleshooting.md`

```markdown
# Troubleshooting

## ORA-01017

The Oracle username or password is incorrect.

Verify `.env`.

---

## ORA-00942

The monitoring account does not have access
to the required Oracle view.

---

## ORA-01031

Additional privileges may be required.

Use a dedicated monitoring account and apply
least-privilege access.

---

## Connection Failure

Check:

- Oracle listener
- Host
- Port
- Service name
- DSN

Example:

```text
localhost:1521/FREEPDB1

---

Streamlit Failure

Install dependencies:

pip install -r requirements.txt

Run:

streamlit run app/main.py

Tests

Run:

pytest -v

---
