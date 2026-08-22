-- =========================================================
-- SAMPLE CUSTOMERS
-- =========================================================

INSERT INTO src_customers (
    customer_name,
    email,
    city,
    country,
    customer_segment
)
VALUES (
    'Ahmed Alotaibi',
    'ahmed@example.com',
    'Riyadh',
    'Saudi Arabia',
    'Enterprise'
);


INSERT INTO src_customers (
    customer_name,
    email,
    city,
    country,
    customer_segment
)
VALUES (
    'Sara Alharbi',
    'sara@example.com',
    'Jeddah',
    'Saudi Arabia',
    'Consumer'
);


INSERT INTO src_customers (
    customer_name,
    email,
    city,
    country,
    customer_segment
)
VALUES (
    'Omar Alqahtani',
    'omar@example.com',
    'Dammam',
    'Saudi Arabia',
    'SMB'
);


-- =========================================================
-- SAMPLE PRODUCTS
-- =========================================================

INSERT INTO src_products (
    product_name,
    category,
    subcategory,
    unit_price,
    active_flag
)
VALUES (
    'Enterprise Laptop',
    'Technology',
    'Computers',
    5500,
    'Y'
);


INSERT INTO src_products (
    product_name,
    category,
    subcategory,
    unit_price,
    active_flag
)
VALUES (
    'Business Monitor',
    'Technology',
    'Displays',
    1800,
    'Y'
);


INSERT INTO src_products (
    product_name,
    category,
    subcategory,
    unit_price,
    active_flag
)
VALUES (
    'Wireless Keyboard',
    'Accessories',
    'Input Devices',
    350,
    'Y'
);


COMMIT;
