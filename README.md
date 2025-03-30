# TaskServer
A lightweight REST API backend for a task management application.


# dependencies
- fastapi:
  -  pip install "fastapi[standard]"
  -  Doku: https://fastapi.tiangolo.com/tutorial/
  -  https://github.com/fastapi/fastapi  
  


# models
## Task
  {
    id: str (use 'auto' for crate automatic a UUI id),
    title: str,
    done: bool,
    created_at: datetime,
    updated_at: List[datetime],
    dones_at: Optional[datetime] = None
  }

## Worker
  {
    id: int,
    name: str
  }
## Project
  {
    id: int,
    name: str,
    description: str,
    worker_list: List[Worker],
    task_list: List[Task]
  }

# API

## POST /add/task
### add a task
{
    id: str (use 'auto' for crate automatic a UUI id),
    title: str,
    done: bool
  }

## GET /get/all/tasks
### return a list with all tasks





