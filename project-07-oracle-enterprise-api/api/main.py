from fastapi import FastAPI

from api.routers import (
    health,
    customers,
    products,
    orders,
)


app = FastAPI(

    title=
        "Oracle Enterprise API",

    description=
        """
        Enterprise REST API integrated
        with Oracle Database.
        """,

    version="1.0.0",
)


app.include_router(
    health.router
)

app.include_router(
    customers.router
)

app.include_router(
    products.router
)

app.include_router(
    orders.router
)


@app.get("/")
def root():

    return {

        "application":
            "Oracle Enterprise API",

        "version":
            "1.0.0",

        "status":
            "running"

    }
