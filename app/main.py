import uvicorn
from fastapi import FastAPI
import models
from app.client.wb import get_wb_card_data

from app.routes.users import router as users_router
from app.routes.login import router as auth_router
from app.routes.products import router as products_router
app = FastAPI()

app.include_router(users_router)
app.include_router(auth_router)
app.include_router(products_router, tags=["products"])

if __name__ == "__main__":
    get_wb_card_data("306038375")
    uvicorn.run("main:app", reload=True)
