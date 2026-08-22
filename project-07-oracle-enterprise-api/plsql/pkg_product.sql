CREATE OR REPLACE PACKAGE pkg_product
AS

    PROCEDURE create_product(

        p_product_code
            IN VARCHAR2,

        p_product_name
            IN VARCHAR2,

        p_category
            IN VARCHAR2,

        p_price
            IN NUMBER,

        p_stock
            IN NUMBER,

        p_product_id
            OUT NUMBER

    );


    PROCEDURE update_stock(

        p_product_id
            IN NUMBER,

        p_quantity
            IN NUMBER

    );

END pkg_product;
/

---

CREATE OR REPLACE PACKAGE BODY pkg_product
AS

    PROCEDURE create_product(

        p_product_code
            IN VARCHAR2,

        p_product_name
            IN VARCHAR2,

        p_category
            IN VARCHAR2,

        p_price
            IN NUMBER,

        p_stock
            IN NUMBER,

        p_product_id
            OUT NUMBER

    )

    AS

    BEGIN

        INSERT INTO api_products (

            product_code,

            product_name,

            category,

            price,

            stock_quantity

        )

        VALUES (

            p_product_code,

            p_product_name,

            p_category,

            p_price,

            p_stock

        )

        RETURNING product_id
        INTO p_product_id;

        COMMIT;

    END;


    PROCEDURE update_stock(

        p_product_id
            IN NUMBER,

        p_quantity
            IN NUMBER

    )

    AS

    BEGIN

        UPDATE api_products

        SET

            stock_quantity =
                stock_quantity +
                p_quantity,

            updated_at =
                SYSTIMESTAMP

        WHERE product_id =
              p_product_id;

        IF SQL%ROWCOUNT = 0 THEN

            RAISE_APPLICATION_ERROR(
                -20010,
                'Product not found'
            );

        END IF;

        COMMIT;

    END;

END pkg_product;
/

