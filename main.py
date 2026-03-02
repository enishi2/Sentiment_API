from fastapi import FastAPI
from sentiment_routes import router
from database import engine, Base


app = FastAPI()

app.include_router(router)

Base.metadata.create_all(bind=engine)