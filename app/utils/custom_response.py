import typing
from fastapi import BackgroundTasks
import json
from typing import Any

from fastapi.responses import JSONResponse
from pydantic import BaseModel


class ResponseData(BaseModel):
    success: bool = True
    data: Any = None
    message: str | None = None


class CustomJSONResponse(JSONResponse):

    media_type = "application/json"

    def __init__(
        self,
        content: Any,
        status_code: int = 200,
        headers: typing.Mapping[str, str] | None = None,
        media_type: str | None = None,
        background: BackgroundTasks | None = None,
    ) -> None:
        super().__init__(content, status_code, headers, media_type, background)

    def render(self, content) -> bytes:
        return json.dumps(ResponseData(
            success=True,
            data=content,
            message=None
        ).model_dump()).encode('utf-8')
