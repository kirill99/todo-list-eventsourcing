import logging
from fastapi import FastAPI, HTTPException, status
from fastapi.exceptions import RequestValidationError
from starlette.middleware.cors import CORSMiddleware

from app.core.config import get_app_settings

from app.api.router import router as api_router
from app.core.handlers import http_bad_request_exception_error_handler, http_exception_error_handler, http_forbidden_exception_error_handler, http_method_not_allowed_exception_error_handler, http_not_found_exception_error_handler, http_unauthorized_exception_error_handler, validation_error_handler
from app.utils.custom_response import CustomJSONResponse
settings = get_app_settings()

logging.basicConfig(level=logging.ERROR, filename='app.log',
                    filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI(
    **settings.fastapi_kwargs,
    default_response_class=CustomJSONResponse,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_hosts,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(
    RequestValidationError,
    validation_error_handler
)

app.add_exception_handler(
    status.HTTP_404_NOT_FOUND,
    http_not_found_exception_error_handler
)

app.add_exception_handler(
    status.HTTP_400_BAD_REQUEST,
    http_bad_request_exception_error_handler
)

app.add_exception_handler(
    status.HTTP_401_UNAUTHORIZED,
    http_unauthorized_exception_error_handler
)

app.add_exception_handler(
    status.HTTP_403_FORBIDDEN,
    http_forbidden_exception_error_handler
)

app.add_exception_handler(
    status.HTTP_405_METHOD_NOT_ALLOWED,
    http_method_not_allowed_exception_error_handler
)

app.add_exception_handler(
    HTTPException,
    http_exception_error_handler
)

app.include_router(api_router, prefix=settings.api_prefix)
