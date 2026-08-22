CREATE OR REPLACE PACKAGE pkg_data_quality
AS

    FUNCTION missing_customer_emails
    RETURN NUMBER;

    FUNCTION invalid_order_items
    RETURN NUMBER;

    FUNCTION orphan_orders
    RETURN NUMBER;

END pkg_data_quality;
/

---

CREATE OR REPLACE PACKAGE BODY pkg_data_quality
AS

    FUNCTION missing_customer_emails
    RETURN NUMBER

    AS

        v_count NUMBER;

    BEGIN

        SELECT COUNT(*)

        INTO v_count

        FROM src_customers

        WHERE email IS NULL;

        RETURN v_count;

    END;


    FUNCTION invalid_order_items
    RETURN NUMBER

    AS

        v_count NUMBER;

    BEGIN

        SELECT COUNT(*)

        INTO v_count

        FROM src_order_items

        WHERE quantity <= 0
        OR unit_price < 0;

        RETURN v_count;

    END;


    FUNCTION orphan_orders
    RETURN NUMBER

    AS

        v_count NUMBER;

    BEGIN

        SELECT COUNT(*)

        INTO v_count

        FROM src_orders o

        LEFT JOIN src_customers c

        ON c.customer_id =
           o.customer_id

        WHERE c.customer_id IS NULL;

        RETURN v_count;

    END;

END pkg_data_quality;
/

---

