import uvicorn
from fastapi import FastAPI
import models

from app.routes.users import router as users_router
from app.routes.login import router as auth_router
from app.routes.products import router as products_router
from app.logger import logger

app = FastAPI()

app.include_router(users_router, tags=["users"])
app.include_router(auth_router, tags=["auth"])
app.include_router(products_router, tags=["products"])

if __name__ == "__main__":
    logger.info("Приложение запущено")
    uvicorn.run("main:app", reload=True)
