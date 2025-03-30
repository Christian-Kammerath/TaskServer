from pydantic import BaseModel
from models.worker import Worker
from models.task import Task
from typing import List


class Project(BaseModel):
    id: int
    name: str
    description: str
    worker_list: List[Worker]
    task_list: List[Task]