from fastapi import FastAPI
from routes import router

app = FastAPI(title="TaskServer")

app.include_router(router)

