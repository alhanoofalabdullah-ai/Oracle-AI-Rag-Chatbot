CREATE OR REPLACE PACKAGE pkg_etl
AS

    PROCEDURE run_full_etl;

    PROCEDURE load_dimensions;

    PROCEDURE load_facts;

END pkg_etl;
/

---

CREATE OR REPLACE PACKAGE BODY pkg_etl
AS

    PROCEDURE load_dimensions
    AS
    BEGIN

        load_dim_customer;

        load_dim_product;

        load_dim_date(
            DATE '2025-01-01',
            DATE '2027-12-31'
        );

    END;


    PROCEDURE load_facts
    AS
    BEGIN

        load_stg_sales;

        load_fact_sales;

    END;


    PROCEDURE run_full_etl
    AS
    BEGIN

        load_dimensions;

        load_facts;

    END;

END pkg_etl;
/
---
