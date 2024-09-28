from .models import (
    Meter,
    Customer,
    MeterReading,
)
from .db import get_db_session

session = get_db_session()


def create_reading(data:dict):
    return MeterReading.create(**data)

