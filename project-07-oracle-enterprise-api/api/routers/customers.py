from fastapi import (
    APIRouter,
    HTTPException,
)

from api.models.customer import (
    CustomerCreate,
    CustomerUpdate,
)


router = APIRouter(
    prefix="/api/v1/customers",
    tags=["Customers"],
)


@router.get("/")
def list_customers():

    return {
        "status": "success",
        "data": []
    }


@router.get("/{customer_id}")
def get_customer(
    customer_id: int
):

    if customer_id <= 0:

        raise HTTPException(

            status_code=400,

            detail="Invalid customer ID"
        )

    return {

        "status":
            "success",

        "customer_id":
            customer_id
    }


@router.post(
    "/",
    status_code=201
)
def create_customer(
    customer: CustomerCreate
):

    return {

        "status":
            "success",

        "message":
            "Customer created",

        "data":
            customer.model_dump()
    }


@router.put(
    "/{customer_id}"
)
def update_customer(

    customer_id: int,

    customer: CustomerUpdate

):

    return {

        "status":
            "success",

        "customer_id":
            customer_id,

        "data":
            customer.model_dump()
    }
