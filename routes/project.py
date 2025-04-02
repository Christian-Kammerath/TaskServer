from fastapi import APIRouter, HTTPException
from models.project import Project
from models.task import ProjectTask
from models.worker import ProjectWorker, ProjectWorkerWithContact

router = APIRouter()


improvised_storage = {}

# get all projects
@router.get("/get/all/project")
async def get_project():
    return improvised_storage

# add project
@router.post("/add/project")
async def add_project(project: Project):
    if project.id in improvised_storage:
        raise HTTPException(status_code=400, detail=f"Project with name {project.id} already exists.")
    improvised_storage[project.id] = project
    return {"message": "Project added successfully"}


# add Task to project
@router.post("/add/task_to_project")
async def add_task_to_project(task: ProjectTask):
    if task.project_id not in improvised_storage:
        raise HTTPException(status_code=404, detail=f"Project with id {task.project_id} not found.")
    improvised_storage[task.project_id].task_list.append(task)
    return {"message": "Task added successfully"}


# add worker to project
@router.post("/add/worker_to_project")
async def add_worker_to_project(worker: ProjectWorker):
    if worker.project_id not in improvised_storage:
                raise HTTPException(status_code=404, detail=f"Project with id {worker.project_id} not found.")
    improvised_storage[worker.project_id].worker_list.append(worker)
    return {"message": "Worker added successfully"}


# add worker with contact information to project
@router.post("/add/worker_with_contact_to_project")
async def add_worker_with_kontakt_to_project(worker: ProjectWorkerWithContact):
    if worker.project_id not in improvised_storage:
                raise HTTPException(status_code=404, detail=f"Project with id {worker.project_id} not found.")
    improvised_storage[worker.project_id].worker_list.append(worker)
    return {"message": "Worker added successfully"}