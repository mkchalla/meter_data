import json
from functools import lru_cache

from typing import Any, List, Tuple, Type
from pydantic.fields import FieldInfo
from dotenv import load_dotenv

load_dotenv()

from pydantic_settings import (
    BaseSettings,
    EnvSettingsSource,
    PydanticBaseSettingsSource,
)



class ParsedEnvVariables(EnvSettingsSource):
    def prepare_field_value(
        self, field_name: str, field: FieldInfo, value: Any, value_is_complex: bool
    ) -> Any:
        if field_name == "CASSANDRA_DB_HOST_IPS":
            return value.split(',')
        return value


class Settings(BaseSettings):
    CASSANDRA_DB_HOST_IPS: list = list()
    CASSANDRA_DB_PORT: str
    CASSANDRA_DB_USERNAME: str = ""
    CASSANDRA_DB_PASSWORD: str = ""
    CASSANDRA_DB_KEYSPACE: str = "uprofile"


    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[PydanticBaseSettingsSource, ...]:
        return (ParsedEnvVariables(settings_cls),)


@lru_cache
def get_settings():
    return Settings()