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

Then:
streamlit run app/main.py

Test error
Run:
pytest -v

---


---

# 30. `LICENSE`

```text
MIT License

Copyright (c) 2026 Alhanoof Alabdullah

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files
(the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge,
publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT.

---

