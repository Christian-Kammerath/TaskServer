import uuid
from typing import Optional

from pydantic import BaseModel, field_validator, Field


#  Base Worker class with optional auto-generated UUID
class Worker(BaseModel):
    id: str = "auto"
    name: str
    surname: Optional[str] = ""

    @field_validator("id", mode="before")
    def generate_uuid_if_auto(cls, v):
        if isinstance(v, str) and v.lower() == "auto":
            return str(uuid.uuid4())
        return v


# Extends Worker with contact information
class WorkerWithContact(Worker):
    email: str
    phone: str

class ProjectWorker(Worker):
    project_id: str

class ProjectWorkerWithContact(BaseModel):
    project_id: str
    contact: WorkerWithContact