from fastapi import FastAPI
from sentiment_routes import router
from database import engine, Base
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI()

app.include_router(router)

app.mount("/static", StaticFiles(directory="static"), name="static")

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return FileResponse(os.path.join("static", "index.html"))







__version__ = "0.2.0"