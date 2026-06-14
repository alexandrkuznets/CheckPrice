from typing import Annotated
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies.auth import get_current_active_user
from app.database.db_config import get_session
from app.models.user import User
from app.services.products import create_product_in_db, get_products_user
from app.schemas.products import ProductResponse
from app.logger import logger

router = APIRouter()


@router.post("/products", status_code=status.HTTP_201_CREATED)
async def create_product(
        marketplace: str,
        product_url: str,
        desired_price: int,
        current_user: Annotated[User, Depends(get_current_active_user)],
        session: AsyncSession = Depends(get_session)
) -> ProductResponse:
    logger.info(f"POST запрос к /products на создание товара: user_id={current_user.id}")
    result = await create_product_in_db(
        marketplace,
        product_url,
        desired_price,
        current_user,
        session
    )
    return result


@router.get("/products", status_code=status.HTTP_200_OK, response_model=list[ProductResponse])
async def get_products(
        current_user: Annotated[User, Depends(get_current_active_user)],
        session: AsyncSession = Depends(get_session)
):
    logger.info(f"GET запрос к /products: user_id={current_user.id}")
    result = await get_products_user(current_user, session)
    return result
