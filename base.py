from pydantic import BaseModel, ValidationError
from typing import Union
import bson


class Base(BaseModel):
    _id: Union[bson.objectid.ObjectId, int] = -1

    def serialize(self):
        pass

    @classmethod
    def unserialize(cls, serialized_data: dict) -> Base:
        try:
            return cls(**serialized_data)
        except ValidationError as e:
            print(e)


class Task(Base):
    pass
