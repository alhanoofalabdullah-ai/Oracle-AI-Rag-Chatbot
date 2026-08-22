# ETL Process

The ETL process consists of three primary stages.

## Extract

Data is extracted from source tables.

```text
SRC_CUSTOMERS
SRC_PRODUCTS
SRC_ORDERS
SRC_ORDER_ITEMS

---

Transform
The staging layer performs:
•	Data cleansing 
•	Revenue calculation 
•	Discount calculation 
•	Null handling 
•	Filtering cancelled transactions 
•	Business transformation 
 
Load
Data is loaded into:

DIM_CUSTOMER
DIM_PRODUCT
DIM_DATE
DIM_LOCATION
FACT_SALES

---

ETL Workflow

Source
  |
  v
Staging
  |
  v
Dimensions
  |
  v
Fact
  |
  v
Analytics

