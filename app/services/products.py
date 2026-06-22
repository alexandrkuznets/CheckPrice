from typing import List

from fastapi.responses import JSONResponse
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, and_

from app.models.user import User
from app.models.product import Product
from app.logger import logger


async def create_product_in_db(
        marketplace: str,
        product_url: str,
        desired_price: int,
        current_user: User,
        session: AsyncSession
) -> Product:
    try:
        logger.info(f"Создание записи БД: Пользователь {current_user.email} Артикул {product_url}")
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
        logger.error(f"Ошибка создания записи в БД: Пользователь {current_user.email} Артикул {product_url}. {ex}")
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(ex))


async def get_products_user(current_user: User, session: AsyncSession) -> List[Product]:
    try:
        logger.info(f" БД: Пользователь {current_user.email}")
        result = await session.execute(select(Product).where(Product.user_id == current_user.id))
        products = result.scalars().all()
        return products
    except SQLAlchemyError as ex:
        logger.error(f"Ошибка обращения к БД: Пользователь {current_user.email}. {ex}")
        raise HTTPException(status_code=400, detail=str(ex))


async def delete_products_on_db(product_id: int, current_id: int, session: AsyncSession):
    result = await session.execute(delete(Product).where(and_(Product.id == product_id, Product.user_id == current_id)))
    await session.commit()
    if result.rowcount > 0:
        return JSONResponse(status_code=200, content="Товар удален")
    else:
        raise HTTPException(status_code=404, detail="Товар не найден")
