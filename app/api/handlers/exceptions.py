from fastapi import FastAPI
from sqlalchemy.exc import NoResultFound, IntegrityError
from starlette.requests import Request
from starlette.responses import JSONResponse


def init_exception_handlers(app: FastAPI):
    @app.exception_handler(NoResultFound)
    async def not_found_exception_handler(request: Request,
                                          exc: NoResultFound):
        return JSONResponse(
            status_code=404,
            content={"detail": "Instance is not exists"}
        )

    @app.exception_handler(IntegrityError)
    async def any_exception_handler(request: Request,
                                    exc: IntegrityError):
        return JSONResponse(
            status_code=400,
            content={"detail": "Instance already exists"}
        )

    @app.exception_handler(ValueError)
    async def value_error_exception_handler(request: Request,
                                            exc: ValueError):
        return JSONResponse(
            status_code=400,
            content={"detail": exc.args}
        )

    @app.exception_handler(Exception)
    async def generic_exception_handler(request: Request,
                                        exc: Exception):
        return JSONResponse(
            status_code=500,
            content={"detail": "An error occurred"}
        )

