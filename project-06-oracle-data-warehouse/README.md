# Oracle Data Warehouse & ETL Analytics Platform

## 📌 Overview

An enterprise-oriented Oracle Data Warehouse and ETL Analytics Platform designed to transform operational data into structured, reliable, and analytics-ready information.

The project demonstrates:

- Oracle Database
- SQL and PL/SQL
- Data Warehousing
- ETL and staging
- Dimensional Modeling
- Star Schema
- Data Quality
- Analytical SQL
- Python
- Streamlit
- Automated Testing
- Docker
- Enterprise Data Architecture

---

## 🎯 Business Problem

Operational databases are optimized for transactions, while management and analytics require historical, aggregated, and business-oriented information.

Typical questions include:

- What is the monthly revenue trend?
- Which products generate the highest revenue?
- Which customers contribute the most value?
- Which locations generate the highest sales?
- What is the average order value?
- Are there incomplete or invalid records?
- How can operational data be transformed into trusted analytical information?

This project addresses these requirements through a dedicated Oracle Data Warehouse.

---

## 💡 Solution

```text
Operational Data
       |
       v
+----------------------+
|    Source Tables     |
| Customers            |
| Products             |
| Orders               |
| Order Items          |
+----------+-----------+
           |
           v
+----------------------+
|       Staging        |
| Validation           |
| Cleansing            |
| Transformation       |
+----------+-----------+
           |
           v
+----------------------+
|    Data Warehouse    |
| Dimensions + Fact    |
| Star Schema          |
+----------+-----------+
           |
           v
+----------------------+
|      Analytics       |
| KPIs / Trends / SQL  |
+----------+-----------+
           |
           v
+----------------------+
|  Streamlit Dashboard |
+----------------------+
```

---

# 🏗️ Architecture

The platform contains five logical layers.

### 1. Source Layer

```text
SRC_CUSTOMERS
SRC_PRODUCTS
SRC_ORDERS
SRC_ORDER_ITEMS
```

### 2. Staging Layer

```text
STG_SALES
```

Responsibilities:

- Data cleansing
- Validation
- Null handling
- Revenue calculation
- Discount calculation
- Filtering cancelled transactions
- Preparation for warehouse loading

### 3. Data Warehouse Layer

```text
DIM_CUSTOMER
DIM_PRODUCT
DIM_DATE
DIM_LOCATION
FACT_SALES
```

### 4. Analytics Layer

Provides:

- Revenue analysis
- Customer analysis
- Product analysis
- Location analysis
- KPI calculations
- Aggregations

### 5. Presentation Layer

A Python/Streamlit dashboard provides analytical views.

---

# ⭐ Star Schema

```text
                       DIM_DATE
                           |
                           |
DIM_CUSTOMER ---- FACT_SALES ---- DIM_PRODUCT
                           |
                           |
                     DIM_LOCATION
```

---

# 📊 Data Warehouse Model

## FACT_SALES

Central fact table containing measurable sales events.

### Measures

- Quantity
- Unit Price
- Discount Amount
- Gross Amount
- Net Amount

### Keys

- Date Key
- Customer Key
- Product Key
- Location Key

### Business Identifiers

- Order ID
- Order Item ID

---

## DIM_CUSTOMER

Attributes:

- Customer ID
- Customer Name
- Email
- City
- Country
- Customer Segment
- Effective From
- Effective To
- Current Flag

## DIM_PRODUCT

Attributes:

- Product ID
- Product Name
- Category
- Subcategory
- Unit Price
- Active Flag
- Effective From
- Effective To
- Current Flag

## DIM_DATE

Attributes:

- Calendar Date
- Day
- Month
- Month Name
- Quarter
- Year
- Week
- Day Name
- Weekend Indicator

## DIM_LOCATION

Attributes:

- City
- Country
- Region

---

# 🔄 ETL Pipeline

```text
EXTRACT
   |
   v
STAGE
   |
   v
VALIDATE
   |
   v
TRANSFORM
   |
   v
LOAD DIMENSIONS
   |
   v
LOAD FACTS
   |
   v
ANALYTICS
```

## Extract

Data is sourced from:

```text
SRC_CUSTOMERS
SRC_PRODUCTS
SRC_ORDERS
SRC_ORDER_ITEMS
```

## Stage

Order and order-item data is combined in `STG_SALES`.

## Validate

Checks include:

- Missing customer email
- Missing product price
- Invalid quantity
- Negative price
- Orphan orders
- Orphan order items

## Transform

```text
Gross Amount = Quantity × Unit Price

Net Amount = Gross Amount − Discount Amount
```

Cancelled transactions are excluded from the analytical fact table.

## Load

Dimensions are loaded first, followed by the fact table.

Oracle `MERGE` is used for insert/update processing.

---

# 🧠 PL/SQL Automation

Main ETL package:

```text
PKG_ETL
```

Procedures:

```text
RUN_FULL_ETL
LOAD_DIMENSIONS
LOAD_FACTS
```

Execute:

```sql
BEGIN
    pkg_etl.run_full_etl;
END;
/
```

---

# 🛡️ Data Quality

The project implements checks for:

- Completeness
- Validity
- Referential integrity
- Consistency

Data Quality package:

```text
PKG_DATA_QUALITY
```

Functions:

```text
MISSING_CUSTOMER_EMAILS
INVALID_ORDER_ITEMS
ORPHAN_ORDERS
```

Example:

```sql
SELECT pkg_data_quality.missing_customer_emails
FROM dual;
```

---

# 📈 Analytics

## Revenue by Month

```sql
SELECT
    d.year_number,
    d.month_number,
    d.month_name,
    SUM(f.net_amount) AS revenue
FROM fact_sales f
JOIN dim_date d
    ON d.date_key = f.date_key
GROUP BY
    d.year_number,
    d.month_number,
    d.month_name
ORDER BY
    d.year_number,
    d.month_number;
```

## Revenue by Product

```sql
SELECT
    p.product_name,
    p.category,
    SUM(f.quantity) AS units_sold,
    SUM(f.net_amount) AS revenue
FROM fact_sales f
JOIN dim_product p
    ON p.product_key = f.product_key
GROUP BY
    p.product_name,
    p.category
ORDER BY revenue DESC;
```

## Revenue by Customer

```sql
SELECT
    c.customer_name,
    c.customer_segment,
    SUM(f.net_amount) AS revenue
FROM fact_sales f
JOIN dim_customer c
    ON c.customer_key = f.customer_key
GROUP BY
    c.customer_name,
    c.customer_segment
ORDER BY revenue DESC;
```

## Revenue by Location

```sql
SELECT
    l.country,
    l.city,
    SUM(f.net_amount) AS revenue
FROM fact_sales f
JOIN dim_location l
    ON l.location_key = f.location_key
GROUP BY
    l.country,
    l.city
ORDER BY revenue DESC;
```

## Average Order Value

```sql
SELECT
    SUM(net_amount) /
    COUNT(DISTINCT order_id) AS average_order_value
FROM fact_sales;
```

---

# 🐍 Python Layer

Structure:

```text
app/
├── __init__.py
├── main.py
├── config.py
│
├── database/
│   ├── __init__.py
│   ├── connection.py
│   └── repository.py
│
├── analytics/
│   ├── __init__.py
│   ├── sales.py
│   ├── customers.py
│   └── products.py
│
└── dashboard/
    ├── __init__.py
    └── dashboard.py
```

The Python layer provides:

- Oracle connectivity
- Connection pooling
- SQL execution
- Pandas analytics
- Dashboard integration
- Environment-based configuration

---

# 📊 Streamlit Dashboard

The dashboard provides:

- Revenue trend
- Top products
- Top customers
- Revenue by category
- Analytical tables

Run:

```bash
streamlit run app/main.py
```

Open:

```text
http://localhost:8501
```

---

# 🧪 Testing

Tests:

```text
tests/
├── test_etl.py
├── test_data_quality.py
└── test_analytics.py
```

Run:

```bash
pytest -v
```

---

# 🐳 Docker

Build:

```bash
docker build -t oracle-data-warehouse .
```

Run:

```bash
docker run -p 8501:8501 oracle-data-warehouse
```

---

# 📁 Project Structure

```text
project-06-oracle-data-warehouse/
│
├── README.md
│
├── sql/
│   ├── 01_create_schemas.sql
│   ├── 02_source_tables.sql
│   ├── 03_staging_tables.sql
│   ├── 04_dimension_tables.sql
│   ├── 05_fact_tables.sql
│   ├── 06_sequences.sql
│   ├── 07_indexes.sql
│   ├── 08_etl_procedures.sql
│   ├── 09_data_quality.sql
│   ├── 10_analytics.sql
│   └── 11_sample_data.sql
│
├── plsql/
│   ├── pkg_etl.sql
│   ├── pkg_data_quality.sql
│   └── pkg_reporting.sql
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── database/
│   ├── analytics/
│   └── dashboard/
│
├── tests/
│   ├── test_etl.py
│   ├── test_data_quality.py
│   └── test_analytics.py
│
├── docs/
│   ├── architecture.md
│   ├── dimensional-model.md
│   ├── etl-process.md
│   └── data-quality.md
│
├── reports/
├── screenshots/
├── requirements.txt
├── pyproject.toml
├── .env.example
├── .gitignore
└── Dockerfile
```

---

# ⚙️ Requirements

Recommended:

```text
Oracle Database 19c+
Python 3.11+
SQL Developer or SQLcl
Git
Docker (optional)
```

Python packages:

```text
oracledb
pandas
streamlit
python-dotenv
pytest
```

---

# 🚀 Installation

## 1. Clone

```bash
git clone https://github.com/alhanoofalabdullah-ai/Oracle-System-Projects.git
cd Oracle-System-Projects/project-06-oracle-data-warehouse
```

## 2. Create Virtual Environment

```bash
python3 -m venv .venv
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Windows:

```powershell
.venv\Scripts\activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure Environment

Copy `.env.example` to `.env`.

Example:

```env
ORACLE_USER=dw_owner
ORACLE_PASSWORD=change_me
ORACLE_DSN=localhost:1521/FREEPDB1
```

Never commit `.env` to GitHub.

---

# 🗄️ Oracle Setup

Execute SQL files in this order:

```text
01_create_schemas.sql
02_source_tables.sql
03_staging_tables.sql
04_dimension_tables.sql
05_fact_tables.sql
06_sequences.sql
07_indexes.sql
08_etl_procedures.sql
09_data_quality.sql
10_analytics.sql
11_sample_data.sql
```

Then run:

```sql
BEGIN
    pkg_etl.run_full_etl;
END;
/
```

Verify:

```sql
SELECT COUNT(*) FROM dim_customer;
SELECT COUNT(*) FROM dim_product;
SELECT COUNT(*) FROM dim_date;
SELECT COUNT(*) FROM fact_sales;
```

---

# 🔐 Security

Security practices include:

- Environment variables for credentials
- `.env` excluded from Git
- No passwords in application source code
- Separation of database and analytics layers
- Externalized configuration

Production enhancements:

- Oracle Wallet
- Secrets Management
- RBAC
- Least Privilege
- Auditing
- Encryption
- Secure database connections

---

# ⚡ Performance

Indexes are created for common fact-table joins:

```text
FACT_SALES.DATE_KEY
FACT_SALES.CUSTOMER_KEY
FACT_SALES.PRODUCT_KEY
FACT_SALES.LOCATION_KEY
```

Future performance enhancements:

- Partitioning
- Materialized Views
- Query optimization
- Statistics management
- Parallel processing
- Bulk loading
- Incremental ETL

---

# 🔁 Incremental ETL Roadmap

A production implementation can use Change Data Capture or timestamp-based extraction:

```text
Source
  |
  v
CDC / Last Updated Timestamp
  |
  v
Incremental Staging
  |
  v
MERGE
  |
  v
Warehouse
```

This reduces unnecessary processing for large datasets.

---

# 🧩 Slowly Changing Dimensions

The dimensions include:

```text
effective_from
effective_to
current_flag
```

These provide a foundation for Slowly Changing Dimension Type 2.

Example:

```text
Customer
  |
  +-- Version 1
  |     effective_from = 2026-01-01
  |     effective_to   = 2026-06-30
  |
  +-- Version 2
        effective_from = 2026-07-01
        effective_to   = NULL
        current_flag   = Y
```

---

# 📋 Data Lineage

```text
SRC_CUSTOMERS
      |
      v
DIM_CUSTOMER
      |
      v
FACT_SALES
      |
      v
ANALYTICS
```

```text
SRC_PRODUCTS
      |
      v
DIM_PRODUCT
      |
      v
FACT_SALES
      |
      v
ANALYTICS
```

```text
SRC_ORDERS + SRC_ORDER_ITEMS
              |
              v
          STG_SALES
              |
              v
          FACT_SALES
```

---

# 📌 Key Performance Indicators

Supported KPIs include:

### Total Revenue

```text
SUM(Net Amount)
```

### Units Sold

```text
SUM(Quantity)
```

### Average Order Value

```text
Revenue / Distinct Orders
```

### Revenue per Customer

```text
Revenue / Distinct Customers
```

### Product Revenue Contribution

```text
Product Revenue / Total Revenue
```

---

# 🏢 Enterprise Use Cases

The architecture can be adapted for:

- Retail Analytics
- Enterprise Sales Analytics
- Customer Analytics
- Product Analytics
- Financial Reporting
- Supply Chain Analytics
- Project Analytics
- Operational Reporting
- Management Dashboards
- Business Intelligence Platforms

---

# 🎓 Skills Demonstrated

## Oracle

- Oracle Database
- SQL
- PL/SQL
- Tables
- Constraints
- Indexes
- Sequences
- Procedures
- Packages
- MERGE
- Referential Integrity

## Data Engineering

- ETL
- Staging
- Data Transformation
- Data Validation
- Data Quality
- Data Lineage
- Incremental Loading Concepts

## Data Warehousing

- Star Schema
- Fact Tables
- Dimension Tables
- Surrogate Keys
- Business Keys
- Historical Data
- SCD Type 2 Foundation

## Analytics

- Aggregations
- KPI Development
- Analytical SQL
- Revenue Analysis
- Customer Analysis
- Product Analysis
- Geographic Analysis

## Python

- Oracle Connectivity
- Connection Pooling
- Pandas
- Repository Pattern
- Application Configuration

## DevOps

- Git
- Environment Variables
- Docker
- Automated Testing

## Business Intelligence

- Dashboard Design
- Executive Reporting
- KPI Visualization
- Decision Support

---

# 📦 Project Deliverables

- Oracle database schema
- Source data model
- Staging layer
- Dimensional model
- Fact table
- ETL procedures
- PL/SQL packages
- Data quality framework
- Analytical SQL
- Python database layer
- Streamlit dashboard
- Automated tests
- Docker configuration
- Documentation

---

# 🔮 Future Enhancements

### Oracle

- Oracle Partitioning
- Materialized Views
- Advanced Query Optimization
- Oracle Scheduler
- Oracle Enterprise Manager
- Oracle GoldenGate

### ETL

- Incremental ETL
- CDC
- Retry mechanism
- ETL logging
- Error handling
- Batch monitoring
- Audit tables

### Data Governance

- Data lineage
- Metadata management
- Data catalog
- Business glossary
- Data ownership
- Data classification

### Analytics

- Power BI integration
- Tableau integration
- Advanced KPI framework
- Forecasting
- Anomaly detection
- Customer segmentation

### Orchestration

- Apache Airflow
- Scheduled ETL
- Pipeline monitoring
- Alerting

### AI

- Revenue forecasting
- Demand prediction
- Customer churn prediction
- Sales anomaly detection
- Automated business insights

---

# 🗺️ Oracle Portfolio Roadmap

This is Project 06 in the Oracle portfolio:

```text
01 ─ Oracle Intelligent Database
       |
       v
02 ─ Oracle Database Management
       |
       v
03 ─ Oracle Performance & SQL Tuning
       |
       v
04 ─ Oracle Backup & Disaster Recovery
       |
       v
05 ─ Oracle Security & Audit
       |
       v
06 ─ Oracle Data Warehouse & ETL
```

The portfolio covers multiple Oracle disciplines rather than focusing only on SQL development.

---

# 💼 Professional Portfolio Value

This project is relevant to roles involving:

- Oracle Database
- Data Engineering
- Data Warehousing
- Business Intelligence
- Enterprise Systems
- Digital Transformation
- Data & Analytics
- Database Engineering
- ETL Development
- Technical Project Delivery
- Enterprise Applications

It demonstrates the ability to connect database engineering, data architecture, ETL, analytics, and business decision support.

---

# 🏆 Project Highlights

```text
✓ Oracle Data Warehouse
✓ Star Schema
✓ Fact & Dimension Modeling
✓ ETL Pipeline
✓ PL/SQL Automation
✓ Data Quality
✓ Analytical SQL
✓ Python Integration
✓ Streamlit Dashboard
✓ Automated Testing
✓ Docker Support
✓ Enterprise Architecture
✓ Data Lineage
✓ SCD Type 2 Foundation
```

---

# 👩‍💻 Author

Alhanoof Alabdullah

GitHub:

https://github.com/alhanoofalabdullah-ai

---

# 📜 License

MIT License

See the `LICENSE` file for details.

---

## ⭐ Project Status

Status: Portfolio / Educational Enterprise Project

Project: 06

Domain: Oracle Data Warehousing & ETL

Focus: Enterprise Data Engineering, Analytics & Business Intelligence
