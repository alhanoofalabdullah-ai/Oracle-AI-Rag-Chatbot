CREATE OR REPLACE PACKAGE pkg_customer
AS

    PROCEDURE create_customer(

        p_customer_code
            IN VARCHAR2,

        p_customer_name
            IN VARCHAR2,

        p_email
            IN VARCHAR2,

        p_phone
            IN VARCHAR2,

        p_customer_id
            OUT NUMBER

    );


    PROCEDURE update_customer(

        p_customer_id
            IN NUMBER,

        p_customer_name
            IN VARCHAR2,

        p_phone
            IN VARCHAR2

    );


    PROCEDURE deactivate_customer(

        p_customer_id
            IN NUMBER

    );

END pkg_customer;
/

---

## Package Body

CREATE OR REPLACE PACKAGE BODY pkg_customer
AS

    PROCEDURE create_customer(

        p_customer_code
            IN VARCHAR2,

        p_customer_name
            IN VARCHAR2,

        p_email
            IN VARCHAR2,

        p_phone
            IN VARCHAR2,

        p_customer_id
            OUT NUMBER

    )

    AS

    BEGIN

        INSERT INTO api_customers (

            customer_code,

            customer_name,

            email,

            phone

        )

        VALUES (

            p_customer_code,

            p_customer_name,

            p_email,

            p_phone

        )

        RETURNING customer_id
        INTO p_customer_id;

        COMMIT;

    END;


    PROCEDURE update_customer(

        p_customer_id
            IN NUMBER,

        p_customer_name
            IN VARCHAR2,

        p_phone
            IN VARCHAR2

    )

    AS

    BEGIN

        UPDATE api_customers

        SET

            customer_name =
                p_customer_name,

            phone =
                p_phone,

            updated_at =
                SYSTIMESTAMP

        WHERE customer_id =
              p_customer_id;

        IF SQL%ROWCOUNT = 0 THEN

            RAISE_APPLICATION_ERROR(
                -20001,
                'Customer not found'
            );

        END IF;

        COMMIT;

    END;


    PROCEDURE deactivate_customer(

        p_customer_id
            IN NUMBER

    )

    AS

    BEGIN

        UPDATE api_customers

        SET

            status = 'INACTIVE',

            updated_at =
                SYSTIMESTAMP

        WHERE customer_id =
              p_customer_id;

        IF SQL%ROWCOUNT = 0 THEN

            RAISE_APPLICATION_ERROR(
                -20002,
                'Customer not found'
            );

        END IF;

        COMMIT;

    END;

END pkg_customer;
/
