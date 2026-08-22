-- =========================================================
-- STAGING TABLES
-- =========================================================

CREATE TABLE stg_sales (

    order_id NUMBER,

    order_item_id NUMBER,

    customer_id NUMBER,

    product_id NUMBER,

    order_date DATE,

    city VARCHAR2(100),

    country VARCHAR2(100),

    quantity NUMBER(12,2),

    unit_price NUMBER(12,2),

    discount_amount NUMBER(12,2),

    gross_amount NUMBER(14,2),

    net_amount NUMBER(14,2),

    load_timestamp TIMESTAMP
        DEFAULT SYSTIMESTAMP
);
