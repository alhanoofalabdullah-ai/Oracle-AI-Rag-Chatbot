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
/
