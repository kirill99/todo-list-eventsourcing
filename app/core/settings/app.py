from typing import List
from app.core.settings.base import BaseAppSettings


class AppSettings(BaseAppSettings):
    title: str = "FastAPI with eventsourcing"
    version: str = "1.0.0"
    debug: bool = False
    docs_url: str = "/docs"
    openapi_prefix: str = ""
    openapi_url: str = "/openapi.json"
    redoc_url: str = "/redoc"
    api_prefix: str = "/api"
    jwt_secret_key: str = 'secret'
    database_url: str = ""
    test_database_url: str = ""
    allowed_hosts: List[str] = ["*"]
    max_connection_count: int = 10
    min_connection_count: int = 10

    # access_token_expire_sec: int = 180  # 3 min
    # refresh_token_expire_sec: int = 1800  # 30 min


    @property
    def fastapi_kwargs(self):
        return {
            "debug": self.debug,
            "docs_url": self.docs_url,
            "openapi_prefix": self.openapi_prefix,
            "openapi_url": self.openapi_url,
            "redoc_url": self.redoc_url,
            "title": self.title,
            "version": self.version,
        }
