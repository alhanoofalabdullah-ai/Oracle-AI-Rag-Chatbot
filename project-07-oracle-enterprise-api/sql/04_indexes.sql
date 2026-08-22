CREATE INDEX idx_customer_status
ON api_customers(status);

CREATE INDEX idx_product_category
ON api_products(category);

CREATE INDEX idx_product_status
ON api_products(status);

CREATE INDEX idx_order_customer
ON api_orders(customer_id);

CREATE INDEX idx_order_status
ON api_orders(order_status);

CREATE INDEX idx_order_created
ON api_orders(created_at);

CREATE INDEX idx_audit_request
ON api_audit_log(request_id);

CREATE INDEX idx_audit_timestamp
ON api_audit_log(request_timestamp);

CREATE INDEX idx_error_request
ON api_error_log(request_id);
