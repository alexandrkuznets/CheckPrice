import uvicorn
from fastapi import FastAPI
import models
# from config import settings

app = FastAPI()


if __name__=="__main__":
    uvicorn.run("main:app", reload=True)