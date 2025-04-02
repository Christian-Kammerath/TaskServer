# TaskServer
A lightweight REST API backend for a task management application.


# dependencies
- fastapi:
  -  pip install "fastapi[standard]"
  -  Doku: https://fastapi.tiangolo.com/tutorial/
  -  https://github.com/fastapi/fastapi  
  


# models
## Task
```json
  {
    id: str // (use 'auto' for crate automatic a UUID id. => str),
    title: str,
    done: bool,
    created_at: datetime,
    updated_at: List[datetime], 
    dones_at: Optional[datetime] = None
  }
  
## ProjectTask
```json
 {
    id: str // (use 'auto' for crate automatic a UUID id. => str),
    title: str,
    done: bool,
    created_at: datetime,
    updated_at: List[datetime], 
    dones_at: Optional[datetime] = None
    project_id: str // target project id
 } 

## Worker
```json
  {
    id: str // (use 'auto' for crate automatic a UUID id. => str),
    name: str
    surname: Optional
  }

## WorkerWithContact extend from Worker
```json
 {
    email: str,
    phone: str
 }

## ProjectWorker extend from Worker
```json
 {
    project_id: str
    
 }

## ProjectWorkerWithContact
```json
 {
    project_id: str,
    kontakt: WorkerWithContact // (instance from WorkerWithContact)
 }

## Project
```json
  {
    id: str // (use 'auto' for crate automatic a UUI id. UUID => str),
    name: str,
    description: str,
    worker_list: List[Worker], // (Do not include in post request unless it is sent with correct entries)
    task_list: List[Task] // (Do not include in post request unless it is sent with correct entries)
  }

# API

## POST /add/task
### add a task

```json
{
    id: str // (use 'auto' for crate automatic a UUI id),
    title: str,
    done: bool
  }


## GET /get/all/tasks
### return a list with all tasks
look model Task


## GET /get/all/project
### return a list with all projects
look model Project


## POST /add/project
### add a project

only project
```json
  {
    id: str // (use 'auto' for crate automatic a UUI id. UUID => str),
    name: str,
    description: str,
  }

with worker and task
```json
 {
    {
    id: str // (use 'auto' for crate automatic a UUI id. UUID => str),
    name: str,
    description: str,
    worker_list: [
        {
          id: str // (use 'auto' for crate automatic a UUID id. => str),
          name: str
          surname: Optional
        }
    ]
    task_list: [
         {
            id: str // (use 'auto' for crate automatic a UUID id. => str),
            title: str,
            done: bool
        }
    ]
  }
 }

## POST /add/task_to_project
### add a task to a project
```json
 {
    id: str // (use 'auto' for crate automatic a UUID id. => str),
    title: str,
    done: bool,
    project_id: str // target project id
 }


## POST /add/worker_to_project
### add a worker to project
```json
 {
    id: str // (use 'auto' for crate automatic a UUID id. => str),
    name: str,
    surname: Optional
    project_id: str // target project id
 }

## /add/worker_with_contact_to_project
### add a worker with connect information
```json
 {
    project_id: str, // target project id
    contact: {
      id: str // (use 'auto' for crate automatic a UUID id. => str),
      name: str,
      surname: Optional,
      email: str,
      phone: str
    }
    
 }





