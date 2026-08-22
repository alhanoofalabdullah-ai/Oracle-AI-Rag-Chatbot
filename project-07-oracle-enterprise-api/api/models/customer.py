from pydantic import BaseModel, EmailStr


class CustomerCreate(BaseModel):

    customer_code: str

    customer_name: str

    email: EmailStr

    phone: str | None = None


class CustomerUpdate(BaseModel):

    customer_name: str

    phone: str | None = None
