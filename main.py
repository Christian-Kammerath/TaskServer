from fastapi import FastAPI
from routes import task,project

# server start point
app = FastAPI(title="TaskServer")


app.include_router(task.router)
app.include_router(project.router)

