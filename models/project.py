import uuid
from pydantic import BaseModel, field_validator, Field
from models.worker import Worker, ProjectWorkerWithContact, ProjectWorker
from models.task import Task
from typing import List, Union


# Model for project : If 'id' is set to "auto", a UUID is generated automatically.
class Project(BaseModel):
    id: str = "auto"
    name: str
    description: str
    worker_list: List[Union[Worker,ProjectWorker,ProjectWorkerWithContact]] = Field(default_factory=list)
    task_list: List[Task] = Field(default_factory=list)

    @field_validator("id", mode="before")
    def generate_uuid_if_auto(cls, v):
        if isinstance(v, str) and v.lower() == "auto":
            return str(uuid.uuid4())
        return v