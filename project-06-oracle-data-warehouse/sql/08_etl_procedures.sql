## ETL Process

-- =========================================================
-- ETL PROCEDURES
-- =========================================================

CREATE OR REPLACE PROCEDURE load_dim_customer
AS

BEGIN

    MERGE INTO dim_customer target

    USING (

        SELECT
            customer_id,
            customer_name,
            email,
            city,
            country,
            customer_segment

        FROM src_customers

    ) source

    ON (
        target.customer_id =
        source.customer_id

        AND target.current_flag = 'Y'
    )

    WHEN MATCHED THEN

        UPDATE SET

            target.customer_name =
                source.customer_name,

            target.email =
                source.email,

            target.city =
                source.city,

            target.country =
                source.country,

            target.customer_segment =
                source.customer_segment

    WHEN NOT MATCHED THEN

        INSERT (
            customer_id,
            customer_name,
            email,
            city,
            country,
            customer_segment,
            effective_from,
            current_flag
        )

        VALUES (
            source.customer_id,
            source.customer_name,
            source.email,
            source.city,
            source.country,
            source.customer_segment,
            SYSDATE,
            'Y'
        );

    COMMIT;

END;

---

## Product ETL

CREATE OR REPLACE PROCEDURE load_dim_product
AS

BEGIN

    MERGE INTO dim_product target

    USING (

        SELECT
            product_id,
            product_name,
            category,
            subcategory,
            unit_price,
            active_flag

        FROM src_products

    ) source

    ON (
        target.product_id =
        source.product_id

        AND target.current_flag = 'Y'
    )

    WHEN MATCHED THEN

        UPDATE SET

            target.product_name =
                source.product_name,

            target.category =
                source.category,

            target.subcategory =
                source.subcategory,

            target.unit_price =
                source.unit_price,

            target.active_flag =
                source.active_flag

    WHEN NOT MATCHED THEN

        INSERT (
            product_id,
            product_name,
            category,
            subcategory,
            unit_price,
            active_flag,
            effective_from,
            current_flag
        )

        VALUES (
            source.product_id,
            source.product_name,
            source.category,
            source.subcategory,
            source.unit_price,
            source.active_flag,
            SYSDATE,
            'Y'
        );

    COMMIT;

END;
/

---

## Date Dimension Loader

CREATE OR REPLACE PROCEDURE load_dim_date (
    p_start_date DATE,
    p_end_date DATE
)
AS

    v_date DATE;

BEGIN

    v_date := TRUNC(p_start_date);

    WHILE v_date <= TRUNC(p_end_date)
    LOOP

        INSERT INTO dim_date (
            date_key,
            calendar_date,
            day_number,
            month_number,
            month_name,
            quarter_number,
            year_number,
            week_number,
            day_name,
            is_weekend
        )

        SELECT

            TO_NUMBER(
                TO_CHAR(
                    v_date,
                    'YYYYMMDD'
                )
            ),

            v_date,

            EXTRACT(
                DAY FROM v_date
            ),

            EXTRACT(
                MONTH FROM v_date
            ),

            TO_CHAR(
                v_date,
                'MONTH'
            ),

            TO_NUMBER(
                TO_CHAR(
                    v_date,
                    'Q'
                )
            ),

            EXTRACT(
                YEAR FROM v_date
            ),

            TO_NUMBER(
                TO_CHAR(
                    v_date,
                    'IW'
                )
            ),

            TO_CHAR(
                v_date,
                'DAY'
            ),

            CASE
                WHEN TO_CHAR(
                    v_date,
                    'DY',
                    'NLS_DATE_LANGUAGE=ENGLISH'
                )
                IN ('FRI', 'SAT')
                THEN 'Y'
                ELSE 'N'
            END

        FROM dual

        WHERE NOT EXISTS (

            SELECT 1

            FROM dim_date

            WHERE calendar_date = v_date

        );

        v_date := v_date + 1;

    END LOOP;

    COMMIT;

END;
/

---

## Sales Staging

CREATE OR REPLACE PROCEDURE load_stg_sales
AS

BEGIN

    DELETE FROM stg_sales;

    INSERT INTO stg_sales (
        order_id,
        order_item_id,
        customer_id,
        product_id,
        order_date,
        city,
        country,
        quantity,
        unit_price,
        discount_amount,
        gross_amount,
        net_amount
    )

    SELECT

        o.order_id,

        oi.order_item_id,

        o.customer_id,

        oi.product_id,

        o.order_date,

        o.city,

        o.country,

        oi.quantity,

        oi.unit_price,

        NVL(
            oi.discount_amount,
            0
        ),

        oi.quantity *
        oi.unit_price,

        (
            oi.quantity *
            oi.unit_price
        )
        -
        NVL(
            oi.discount_amount,
            0
        )

    FROM src_orders o

    INNER JOIN src_order_items oi

        ON oi.order_id =
           o.order_id

    WHERE o.status <> 'CANCELLED';

    COMMIT;

END;
/

---

## Fact Loader

CREATE OR REPLACE PROCEDURE load_fact_sales
AS

BEGIN

    INSERT INTO fact_sales (

        order_id,

        order_item_id,

        date_key,

        customer_key,

        product_key,

        location_key,

        quantity,

        unit_price,

        discount_amount,

        gross_amount,

        net_amount

    )

    SELECT

        s.order_id,

        s.order_item_id,

        TO_NUMBER(
            TO_CHAR(
                s.order_date,
                'YYYYMMDD'
            )
        ),

        c.customer_key,

        p.product_key,

        l.location_key,

        s.quantity,

        s.unit_price,

        s.discount_amount,

        s.gross_amount,

        s.net_amount

    FROM stg_sales s

    INNER JOIN dim_customer c

        ON c.customer_id =
           s.customer_id

        AND c.current_flag = 'Y'

    INNER JOIN dim_product p

        ON p.product_id =
           s.product_id

        AND p.current_flag = 'Y'

    INNER JOIN dim_location l

        ON l.city = s.city

        AND l.country = s.country

    WHERE NOT EXISTS (

        SELECT 1

        FROM fact_sales f

        WHERE f.order_item_id =
              s.order_item_id

    );

    COMMIT;

END;
/

---
    
    
/
