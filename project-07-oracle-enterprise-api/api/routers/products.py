from fastapi import APIRouter


router = APIRouter(

    prefix="/api/v1/products",

    tags=["Products"]
)


@router.get("/")
def list_products():

    return {

        "status":
            "success",

        "data": []

    }


@router.get("/{product_id}")
def get_product(
    product_id: int
):

    return {

        "status":
            "success",

        "product_id":
            product_id

    }
