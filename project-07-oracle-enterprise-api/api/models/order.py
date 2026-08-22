from pydantic import BaseModel


class OrderCreate(BaseModel):

    customer_id: int


class OrderItemCreate(BaseModel):

    product_id: int

    quantity: int
