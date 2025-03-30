from fastapi import FastAPI
from routes import task

app = FastAPI(title="TaskServer")

app.include_router(task.router)

