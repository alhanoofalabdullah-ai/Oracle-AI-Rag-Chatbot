INSERT INTO api_customers (
    customer_code,
    customer_name,
    email,
    phone
)
VALUES (
    'CUS-0001',
    'Ahmed Alotaibi',
    'ahmed@example.com',
    '+966500000001'
);

INSERT INTO api_customers (
    customer_code,
    customer_name,
    email,
    phone
)
VALUES (
    'CUS-0002',
    'Sara Alharbi',
    'sara@example.com',
    '+966500000002'
);

INSERT INTO api_products (
    product_code,
    product_name,
    category,
    price,
    stock_quantity
)
VALUES (
    'PRD-0001',
    'Enterprise Laptop',
    'Technology',
    5500,
    100
);

INSERT INTO api_products (
    product_code,
    product_name,
    category,
    price,
    stock_quantity
)
VALUES (
    'PRD-0002',
    'Business Monitor',
    'Technology',
    1800,
    50
);

INSERT INTO api_products (
    product_code,
    product_name,
    category,
    price,
    stock_quantity
)
VALUES (
    'PRD-0003',
    'Wireless Keyboard',
    'Accessories',
    350,
    200
);

COMMIT;
