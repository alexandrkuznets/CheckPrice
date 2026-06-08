from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.config import settings

async_engine = create_async_engine(f"postgresql+asyncpg://"
                                   f"{settings.postgres_user}:{settings.postgres_password}@"
                                   f"localhost:{settings.postgres_port}/{settings.postgres_db}")
Async_session = async_sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=True)


sync_engine = create_engine(f"postgresql://"
                        f"{settings.postgres_user}:{settings.postgres_password}@"
                        f"localhost:{settings.postgres_port}/{settings.postgres_db}")

Session = sessionmaker(bind=sync_engine)


class Base(DeclarativeBase):
    pass


async def get_session():
    async with Async_session() as session:
        yield session
