## Revenue by Month

SELECT

    d.year_number,

    d.month_number,

    d.month_name,

    SUM(f.net_amount)
        AS revenue

FROM fact_sales f

JOIN dim_date d

    ON d.date_key =
       f.date_key

GROUP BY

    d.year_number,

    d.month_number,

    d.month_name

ORDER BY

    d.year_number,

    d.month_number;

---

## Revenue by Product

SELECT

    p.product_name,

    p.category,

    SUM(f.quantity)
        AS units_sold,

    SUM(f.net_amount)
        AS revenue

FROM fact_sales f

JOIN dim_product p

    ON p.product_key =
       f.product_key

GROUP BY

    p.product_name,

    p.category

ORDER BY revenue DESC;

---

## Revenue by Customer

SELECT

    c.customer_name,

    c.customer_segment,

    SUM(f.net_amount)
        AS revenue

FROM fact_sales f

JOIN dim_customer c

    ON c.customer_key =
       f.customer_key

GROUP BY

    c.customer_name,

    c.customer_segment

ORDER BY revenue DESC;

---

## Revenue by Location

SELECT

    l.country,

    l.city,

    SUM(f.net_amount)
        AS revenue

FROM fact_sales f

JOIN dim_location l

    ON l.location_key =
       f.location_key

GROUP BY

    l.country,

    l.city

ORDER BY revenue DESC;

---

## Average Order Value

SELECT

    SUM(net_amount)
    /
    COUNT(DISTINCT order_id)
        AS average_order_value

FROM fact_sales;

---
