
from pydantic import BaseModel, Field, field_validator
from typing import List, Optional, Union
from datetime import datetime
import uuid




class Task(BaseModel):
    id: Union[str, uuid.UUID] = "auto"
    title: str
    done: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: List[datetime] = Field(default_factory=lambda: [datetime.utcnow()])
    dones_at: Optional[datetime] = None

    @field_validator("id", mode="before")
    def generate_uuid_if_auto(cls, v):
        if isinstance(v, str) and v.lower() == "auto":
            return uuid.uuid4()
        return v





