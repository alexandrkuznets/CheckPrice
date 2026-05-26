from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.db_config import get_session
from app.schemas.users import UserCreate
from app.services.users import create_user_in_db

router = APIRouter()

@router.post("/create_user", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, session: AsyncSession = Depends(get_session)):
    result = await create_user_in_db(user, session)
    return result