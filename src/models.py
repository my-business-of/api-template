from datetime import datetime

import orjson
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, root_validator

from src.utils import convert_datetime_to_gmt, orjson_dumps


class ORJSONModel(BaseModel):
    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps
        json_encoders = {
            datetime: convert_datetime_to_gmt
        }  # method for customer JSON encoding of datetime fields

    @root_validator()
    def set_null_microseconds(self, data: dict) -> dict:
        """Drops microseconds in all the datetime field values."""
        datetime_fields = {
            k: v.replace(microsecond=0)
            for k, v in data.items()
            if isinstance(k, datetime)
        }

        return {**data, **datetime_fields}

    def serializable_dict(self, **kwargs):
        """Return a dict which contains only serializable fields."""
        default_dict = super().dict(**kwargs)

        return jsonable_encoder(default_dict)
