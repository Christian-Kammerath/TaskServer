from time import struct_time
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class Task(BaseModel):
    id: int
    title: str
    done: bool
    created_at: datetime
    updated_at: List[datetime]
    dones_at: Optional[datetime] = None





