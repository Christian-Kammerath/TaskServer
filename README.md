# TaskServer
A lightweight REST API backend for a task management application.


# dependencies
- fastapi:
  -  pip install "fastapi[standard]"
  -  Doku: https://fastapi.tiangolo.com/tutorial/
  -  https://github.com/fastapi/fastapi  
  


# models
- Task
  {
    id: int,
    title: str,
    done: bool,
    created_at: datetime,
    updated_at: List[datetime],
    dones_at: Optional[datetime] = None
  }

- Worker
  {
    id: int,
    name: str
  }
- Project
  {
    id: int,
    name: str,
    description: str,
    worker_list: List[Worker],
    task_list: List[Task]
  }