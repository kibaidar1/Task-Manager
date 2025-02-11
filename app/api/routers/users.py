from fastapi import APIRouter
from starlette import status
from starlette.responses import RedirectResponse

from app.api.dependencies import UsersUseCaseDep
from app.schemas.users import UserCreate, UserRead

router = APIRouter(prefix='/users',
                   tags=['Users'])


@router.get('/{user_id}',
            response_model=UserRead,
            status_code=status.HTTP_200_OK)
async def get_user(users_use_case: UsersUseCaseDep,
                   user_id: int):
    return await users_use_case.get_user(user_id)


@router.post('/',
             status_code=status.HTTP_303_SEE_OTHER)
async def register_user(users_use_case: UsersUseCaseDep,
                        user: UserCreate):
    user_id = await users_use_case.register_user(user)
    redirect_url = router.url_path_for(get_user.__name__,
                                       user_id=user_id)
    return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)




