from contextlib import contextmanager
from functools import lru_cache
from typing import Generator

import oracledb

from app.config import get_settings


@lru_cache
def get_pool() -> oracledb.ConnectionPool:
    """
    Create and cache the Oracle connection pool.
    """

    settings = get_settings()

    pool = oracledb.create_pool(
        user=settings.oracle_user,
        password=settings.oracle_password,
        dsn=settings.oracle_dsn,
        min=settings.pool_min,
        max=settings.pool_max,
        increment=settings.pool_increment,
    )

    return pool


@contextmanager
def get_connection() -> Generator:
    """
    Acquire and release an Oracle connection.
    """

    pool = get_pool()

    connection = pool.acquire()

    try:
        yield connection

    finally:
        pool.release(connection)


def ping_database() -> bool:
    """
    Test Oracle database connectivity.
    """

    try:

        with get_connection() as connection:

            with connection.cursor() as cursor:

                cursor.execute(
                    "SELECT 1 FROM dual"
                )

                result = cursor.fetchone()

                return (
                    result is not None
                    and result[0] == 1
                )

    except Exception:

        return False


def close_pool() -> None:
    """
    Close the Oracle connection pool.
    """

    try:

        pool = get_pool()

        pool.close(
            force=True
        )

    except Exception:
        pass
