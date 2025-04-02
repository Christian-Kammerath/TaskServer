
from pydantic import BaseModel, Field, field_validator
from typing import List, Optional, Union
from datetime import datetime, UTC
import uuid



# Task model: If 'id' is set to "auto", a UUID is generated automatically.
class Task(BaseModel):
    id: str  = "auto"
    title: str
    done: bool = False
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    updated_at: List[datetime] = Field(default_factory=lambda: [datetime.now(UTC)])
    dones_at: Optional[datetime] = None

    @field_validator("id", mode="before")
    def generate_uuid_if_auto(cls, v):
        if isinstance(v, str) and v.lower() == "auto":
            return str(uuid.uuid4())
        return v

class ProjectTask(Task):
    project_id: str







