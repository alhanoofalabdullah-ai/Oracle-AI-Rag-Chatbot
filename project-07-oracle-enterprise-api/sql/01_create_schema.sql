-- =========================================================
-- PROJECT 07
-- Oracle Enterprise API & Integration Platform
-- =========================================================

CREATE USER enterprise_api
IDENTIFIED BY "ChangeMe_123";

GRANT CREATE SESSION TO enterprise_api;

GRANT CREATE TABLE TO enterprise_api;

GRANT CREATE VIEW TO enterprise_api;

GRANT CREATE SEQUENCE TO enterprise_api;

GRANT CREATE PROCEDURE TO enterprise_api;

GRANT CREATE TRIGGER TO enterprise_api;

GRANT UNLIMITED TABLESPACE TO enterprise_api;
