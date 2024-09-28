import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine import models
from datetime import datetime


class Customer(models.Model):
    __keyspace__ = "meter_data"
    customer_id = columns.UUID(primary_key=True, required=True, default=uuid.uuid4)
    first_name = columns.Text()
    last_name = columns.Text()
    address_line1 = columns.Text()
    address_line2 = columns.Text()
    city = columns.Text()
    state = columns.Text()
    postal_code = columns.Integer()
    country = columns.Text()
    phone = columns.Text()
    email = columns.Text()


class Meter(models.Model):
    __keyspace__ = "meter_data"
    meter_id = columns.UUID(primary_key=True, required=True, default=uuid.uuid4)
    nmi = columns.Text(required=True, index=True)
    customer_id = columns.UUID()


class MeterReading(models.Model):
    __keyspace__ = "meter_data"
    reading_id = columns.UUID(primary_key=True, required=True, default=uuid.uuid4)
    reading = columns.Float(required=True)
    reading_date_time = columns.DateTime(required=True)

