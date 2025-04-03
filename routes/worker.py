from fastapi import APIRouter,HTTPException

from models.worker import Worker, WorkerWithContact

router = APIRouter()
improvised_storage = {}

# get all worker
@router.get("get/all/worker")
async def get_all_worker():
    return improvised_storage

# add worker
@router.post("/add/worker")
async def add_worker(worker: Worker):
    if worker.name in improvised_storage:
        raise HTTPException(status_code=400, detail=f"Worker with name {worker.name} already exists.")
    improvised_storage[worker.name] = worker
    return {"message": "Worker added successfully"}

# add worker with contact
@router.post("/add/worker_with_contact")
async def add_worker(worker: WorkerWithContact):
    if worker.name in improvised_storage:
        raise HTTPException(status_code=400, detail=f"Worker with name {worker.name} already exists.")
    improvised_storage[worker.name] = worker
    return {"message": "Worker added successfully"}