CREATE ROLE api_read_role;

CREATE ROLE api_write_role;

GRANT SELECT
ON api_customers
TO api_read_role;

GRANT SELECT
ON api_products
TO api_read_role;

GRANT SELECT
ON api_orders
TO api_read_role;

GRANT SELECT
ON api_order_items
TO api_read_role;

GRANT INSERT, UPDATE
ON api_customers
TO api_write_role;

GRANT INSERT, UPDATE
ON api_orders
TO api_write_role;

GRANT INSERT
ON api_order_items
TO api_write_role;
