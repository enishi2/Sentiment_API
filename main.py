from fastapi import FastAPI
from sentiment_routes import router
from database import engine, Base
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# CORS para permitir acesso público de qualquer origem
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

app.mount("/static", StaticFiles(directory="static"), name="static")

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return FileResponse(os.path.join("static", "index.html"))







__version__ = "0.2.0"