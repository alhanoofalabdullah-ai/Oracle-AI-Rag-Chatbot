CREATE OR REPLACE PACKAGE pkg_order
AS

    PROCEDURE create_order(

        p_customer_id
            IN NUMBER,

        p_order_id
            OUT NUMBER,

        p_order_number
            OUT VARCHAR2

    );


    PROCEDURE add_order_item(

        p_order_id
            IN NUMBER,

        p_product_id
            IN NUMBER,

        p_quantity
            IN NUMBER

    );


    PROCEDURE recalculate_total(

        p_order_id
            IN NUMBER

    );

END pkg_order;
/

---

CREATE OR REPLACE PACKAGE BODY pkg_order
AS

    PROCEDURE create_order(

        p_customer_id
            IN NUMBER,

        p_order_id
            OUT NUMBER,

        p_order_number
            OUT VARCHAR2

    )

    AS

    BEGIN

        p_order_number :=
            'ORD-' ||
            seq_order_number.NEXTVAL;

        INSERT INTO api_orders (

            order_number,

            customer_id

        )

        VALUES (

            p_order_number,

            p_customer_id

        )

        RETURNING order_id
        INTO p_order_id;

        COMMIT;

    END;


    PROCEDURE add_order_item(

        p_order_id
            IN NUMBER,

        p_product_id
            IN NUMBER,

        p_quantity
            IN NUMBER

    )

    AS

        v_price NUMBER;

        v_stock NUMBER;

    BEGIN

        SELECT

            price,

            stock_quantity

        INTO

            v_price,

            v_stock

        FROM api_products

        WHERE product_id =
              p_product_id

        FOR UPDATE;


        IF v_stock < p_quantity THEN

            RAISE_APPLICATION_ERROR(
                -20020,
                'Insufficient stock'
            );

        END IF;


        INSERT INTO api_order_items (

            order_id,

            product_id,

            quantity,

            unit_price,

            line_total

        )

        VALUES (

            p_order_id,

            p_product_id,

            p_quantity,

            v_price,

            p_quantity * v_price

        );


        UPDATE api_products

        SET stock_quantity =
            stock_quantity -
            p_quantity

        WHERE product_id =
              p_product_id;


        COMMIT;

    END;


    PROCEDURE recalculate_total(

        p_order_id
            IN NUMBER

    )

    AS

    BEGIN

        UPDATE api_orders

        SET total_amount = (

            SELECT NVL(
                SUM(line_total),
                0
            )

            FROM api_order_items

            WHERE order_id =
                  p_order_id

        )

        WHERE order_id =
              p_order_id;

        COMMIT;

    END;

END pkg_order;
/
