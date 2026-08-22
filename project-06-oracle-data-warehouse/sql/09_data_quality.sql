-- =========================================================
-- DATA QUALITY CHECKS
-- =========================================================

-- Customers without email

SELECT
    COUNT(*) AS missing_email_count

FROM src_customers

WHERE email IS NULL;


-- Products without prices

SELECT
    COUNT(*) AS missing_price_count

FROM src_products

WHERE unit_price IS NULL;


-- Negative quantities

SELECT
    COUNT(*) AS invalid_quantity_count

FROM src_order_items

WHERE quantity <= 0;


-- Negative prices

SELECT
    COUNT(*) AS invalid_price_count

FROM src_order_items

WHERE unit_price < 0;


-- Orders without customer

SELECT
    COUNT(*) AS orphan_orders

FROM src_orders o

LEFT JOIN src_customers c

    ON c.customer_id =
       o.customer_id

WHERE c.customer_id IS NULL;


-- Order items without product

SELECT
    COUNT(*) AS orphan_items

FROM src_order_items oi

LEFT JOIN src_products p

    ON p.product_id =
       oi.product_id

WHERE p.product_id IS NULL;
