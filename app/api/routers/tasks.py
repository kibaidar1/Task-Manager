from fastapi.routing import APIRouter
from starlette import status
from starlette.responses import RedirectResponse

from app.api.dependencies import TasksUseCaseDep
from app.schemas.tasks import TaskCreate, TaskRead, TaskUpdate


router = APIRouter(prefix='/tasks',
                   tags=['Tasks'])


@router.get('/{task_id}',
            response_model=TaskRead,
            status_code=status.HTTP_200_OK)
async def get_task(tasks_use_case: TasksUseCaseDep,
                   task_id: int):
    return await tasks_use_case.get_task(task_id)


@router.post('/',
             status_code=status.HTTP_303_SEE_OTHER)
async def create_task(tasks_use_case: TasksUseCaseDep,
                      task: TaskCreate):
    task_id = await tasks_use_case.create_task(task)
    redirect_url = router.url_path_for(get_task.__name__,
                                       task_id=task_id)
    return RedirectResponse(redirect_url,
                            status_code=status.HTTP_303_SEE_OTHER)


@router.get('/',
            response_model=list[TaskRead],
            status_code=status.HTTP_200_OK)
async def get_tasks(tasks_use_case: TasksUseCaseDep,
                    user_id: int = None):
    return await tasks_use_case.get_tasks(user_id)


@router.patch('/{task_id}',
              status_code=status.HTTP_303_SEE_OTHER)
async def update_task(tasks_use_case: TasksUseCaseDep,
                      task_id: int,
                      task: TaskUpdate):
    print(task)
    task_id = await tasks_use_case.update_task(task_id, task)
    print(task_id)
    redirect_url = router.url_path_for(get_task.__name__,
                                       task_id=task_id)
    return RedirectResponse(redirect_url,
                            status_code=status.HTTP_303_SEE_OTHER)


@router.delete('/{task_id}',
               status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(tasks_use_case: TasksUseCaseDep,
                      task_id: int):
    await tasks_use_case.delete_task(task_id)


