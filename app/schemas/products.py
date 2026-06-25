from pydantic import BaseModel


class ProductBase(BaseModel):
    marketplace: str
    article: str
    desired_price: int


class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: int
    user_id: int
    last_price: int
    product_name: str
