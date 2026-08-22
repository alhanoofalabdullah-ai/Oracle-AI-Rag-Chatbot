-- =========================================================
-- PROJECT 06
-- Oracle Data Warehouse
-- Schema Setup
-- =========================================================

-- Run with appropriate administrative privileges.

CREATE USER dw_owner
IDENTIFIED BY "ChangeMe_123";

GRANT CREATE SESSION TO dw_owner;

GRANT CREATE TABLE TO dw_owner;

GRANT CREATE VIEW TO dw_owner;

GRANT CREATE SEQUENCE TO dw_owner;

GRANT CREATE PROCEDURE TO dw_owner;

GRANT CREATE TRIGGER TO dw_owner;

GRANT UNLIMITED TABLESPACE TO dw_owner;
