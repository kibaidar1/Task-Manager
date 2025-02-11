from fastapi import FastAPI

from app.api.handlers.exceptions import init_exception_handlers
from app.api.routers.routers import all_routers

app = FastAPI()

for router in all_routers:
    app.include_router(router)

init_exception_handlers(app)
