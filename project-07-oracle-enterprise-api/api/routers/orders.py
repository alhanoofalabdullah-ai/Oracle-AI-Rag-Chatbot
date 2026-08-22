from fastapi import APIRouter

from api.models.order import (
    OrderCreate,
    OrderItemCreate,
)


router = APIRouter(

    prefix="/api/v1/orders",

    tags=["Orders"]
)


@router.get("/")
def list_orders():

    return {

        "status":
            "success",

        "data": []

    }


@router.post(
    "/",
    status_code=201
)
def create_order(
    order: OrderCreate
):

    return {

        "status":
            "success",

        "message":
            "Order created",

        "data":
            order.model_dump()

    }


@router.post(
    "/{order_id}/items",
    status_code=201
)
def add_item(

    order_id: int,

    item: OrderItemCreate

):

    return {

        "status":
            "success",

        "order_id":
            order_id,

        "item":
            item.model_dump()

    }
