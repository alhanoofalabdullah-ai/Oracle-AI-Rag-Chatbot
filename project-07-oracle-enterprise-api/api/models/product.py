from decimal import Decimal

from pydantic import BaseModel


class ProductCreate(BaseModel):

    product_code: str

    product_name: str

    category: str | None = None

    price: Decimal

    stock_quantity: int = 0
