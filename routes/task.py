from fastapi import HTTPException
from fastapi import APIRouter
from models.task import Task

router = APIRouter()
improvised_storage = {}

@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/get/all/tasks")
async def get_all_tasks():
    return improvised_storage



@router.post("/add/task")
async def add_task(task: Task):
    if task.id in improvised_storage:
        raise HTTPException(status_code=400, detail=f"Task with ID {task.id} already exists.")

    improvised_storage[task.id] = task
    return {"message": "Task added successfully"}



