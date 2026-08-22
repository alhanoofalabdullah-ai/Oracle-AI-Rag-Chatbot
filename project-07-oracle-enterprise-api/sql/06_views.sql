
## Customer Summary

CREATE OR REPLACE VIEW vw_customer_summary AS

SELECT

    c.customer_id,

    c.customer_code,

    c.customer_name,

    c.email,

    c.status,

    COUNT(o.order_id)
        AS total_orders,

    NVL(
        SUM(o.total_amount),
        0
    )
        AS total_spend

FROM api_customers c

LEFT JOIN api_orders o

    ON o.customer_id =
       c.customer_id

GROUP BY

    c.customer_id,

    c.customer_code,

    c.customer_name,

    c.email,

    c.status;

---

## Product Summary

CREATE OR REPLACE VIEW vw_product_summary AS

SELECT

    p.product_id,

    p.product_code,

    p.product_name,

    p.category,

    p.price,

    p.stock_quantity,

    p.status

FROM api_products p;

---
