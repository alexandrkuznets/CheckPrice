import uvicorn
from fastapi import FastAPI
import models

from app.routes.users import router as users_router
from app.routes.login import router as auth_router
from app.routes.products import router as products_router

app = FastAPI()

app.include_router(users_router)
app.include_router(auth_router)
app.include_router(products_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
