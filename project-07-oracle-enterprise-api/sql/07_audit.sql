## Customers

CREATE OR REPLACE TRIGGER trg_customer_update
AFTER UPDATE ON api_customers

FOR EACH ROW

BEGIN

    :NEW.updated_at :=
        SYSTIMESTAMP;

END;
/

---

## product

CREATE OR REPLACE TRIGGER trg_product_update
BEFORE UPDATE ON api_products

FOR EACH ROW

BEGIN

    :NEW.updated_at :=
        SYSTIMESTAMP;

END;
/
