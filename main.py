from fastapi import FastAPI
from routes import route1
from database.db import engine
from database import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="model FastAPI",)

app.include_router(route1.router)