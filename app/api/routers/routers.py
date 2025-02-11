from app.api.routers.users import router as users_router
from app.api.routers.tasks import router as tasks_router


all_routers = (users_router,
               tasks_router,)

