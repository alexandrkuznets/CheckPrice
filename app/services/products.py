from typing import List

from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.user import User
from app.models.product import Product


async def create_product_in_db(
        marketplace: str,
        product_url: str,
        desired_price: int,
        current_user: User,
        session: AsyncSession
) -> Product:
    try:
        product = Product(
            user_id=current_user.id,
            marketplace=marketplace,
            product_url=product_url,
            desired_price=desired_price
        )
        session.add(product)
        await session.commit()
        await session.refresh(product)
        return product
    except SQLAlchemyError as ex:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(ex))


async def get_products_user(current_user: User, session: AsyncSession) -> List[Product]:
    result = await session.execute(select(Product).where(Product.user_id == current_user.id))
    products = result.scalars().all()
    return products

