from app.utils.custom_response import ResponseData
from fastapi import status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi import HTTPException, Request
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.utils.messages import FIELD_VALIDATION_ERROR_MESSAGE, URL_NOT_FOUND_MESSAGE


async def validation_error_handler(
    _: Request,
    exc: Exception,
) -> JSONResponse:
    content = ResponseData(
        success=False,
        data=None,
        message=str(FIELD_VALIDATION_ERROR_MESSAGE)
    )

    if isinstance(exc, RequestValidationError):
        content.data = exc.errors()

    return JSONResponse(
        content=content.model_dump(),
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    )


async def http_exception_error_handler(
        _: Request,
        exc: Exception,
) -> JSONResponse:
    content = ResponseData(
        success=False,
        data=None,
        message=None
    )

    if isinstance(exc, HTTPException):
        content.message = exc.detail

    return JSONResponse(
        content=content.model_dump(),
        status_code=status.HTTP_200_OK,
    )


async def http_not_found_exception_error_handler(
        _: Request,
        exc: Exception,
) -> JSONResponse:

    content = ResponseData(
        success=False,
        data=None,
        message=str(URL_NOT_FOUND_MESSAGE)
    )

    if isinstance(exc, HTTPException):
        content.message = exc.detail

    return JSONResponse(
        content=content.model_dump(),
        status_code=status.HTTP_404_NOT_FOUND,
    )


def http_bad_request_exception_error_handler(
        _: Request,
        exc: Exception,
) -> JSONResponse:

    content = ResponseData(
        success=False,
        data=None,
        message=None
    )
    if isinstance(exc, StarletteHTTPException):
        content.message = exc.detail

    return JSONResponse(
        content=content.model_dump(),
        status_code=status.HTTP_400_BAD_REQUEST,
    )


def http_unauthorized_exception_error_handler(
        _: Request,
        exc: Exception,
) -> JSONResponse:

    content = ResponseData(
        success=False,
        data=None,
        message=None
    )
    if isinstance(exc, StarletteHTTPException):
        content.message = exc.detail

    return JSONResponse(
        content=content.model_dump(),
        status_code=status.HTTP_401_UNAUTHORIZED,
    )


def http_forbidden_exception_error_handler(
        _: Request,
        exc: Exception,
) -> JSONResponse:

    content = ResponseData(
        success=False,
        data=None,
        message=None
    )
    if isinstance(exc, StarletteHTTPException):
        content.message = exc.detail

    return JSONResponse(
        content=content.model_dump(),
        status_code=status.HTTP_403_FORBIDDEN,
    )


def http_method_not_allowed_exception_error_handler(
        _: Request,
        exc: Exception,
) -> JSONResponse:

    content = ResponseData(
        success=False,
        data=None,
        message=None
    )
    if isinstance(exc, StarletteHTTPException):
        content.message = exc.detail

    return JSONResponse(
        content=content.model_dump(),
        status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
    )
