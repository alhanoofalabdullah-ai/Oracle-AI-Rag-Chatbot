-- =========================================================
-- FACT INDEXES
-- =========================================================

CREATE INDEX idx_fact_sales_date
ON fact_sales(date_key);

CREATE INDEX idx_fact_sales_customer
ON fact_sales(customer_key);

CREATE INDEX idx_fact_sales_product
ON fact_sales(product_key);

CREATE INDEX idx_fact_sales_location
ON fact_sales(location_key);


-- =========================================================
-- DIMENSION INDEXES
-- =========================================================

CREATE INDEX idx_dim_customer_business
ON dim_customer(customer_id);

CREATE INDEX idx_dim_product_business
ON dim_product(product_id);

CREATE INDEX idx_dim_location_city
ON dim_location(city);
