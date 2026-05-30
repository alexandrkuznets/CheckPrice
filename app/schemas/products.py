from pydantic import BaseModel


class ProductBase(BaseModel):
    marketplace: str
    product_url: str
    desired_price: int


class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: int
    user_id: int
    last_price: int
