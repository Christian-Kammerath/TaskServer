from fastapi import FastAPI
from fastapi import APIRouter


router = APIRouter()
improvised_storage = {}

@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/get/all/tasks")
async def get_all_tasks():
    return improvised_storage

@router.post("/get/{task_id}/task")
async def get_task(task_id: int):
    return improvised_storage[task_id]




