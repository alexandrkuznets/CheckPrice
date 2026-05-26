from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException

from app.schemas.users import UserCreate
from app.models.user import User
from app.core.security import get_password_hash

async def create_user_in_db(user: UserCreate, session: AsyncSession) -> User:
    if user.password != user.password2:
        raise HTTPException(status_code=400, detail="Пароли не совпадают")

    result = await session.execute(select(User).where(User.email == user.email))
    if result.fetchall():
        raise HTTPException(status_code=409, detail="Этот email уже используется")

    password_hashed = get_password_hash(user.password)
    try:
        user = User(email=user.email, password=password_hashed)
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user
    except Exception as ex:
        await session.rollback()
        raise HTTPException(status_code=400, detail=str(ex))

