from pydantic import BaseModel, ValidationError
from typing import Union
import bson


class Base(BaseModel):
    """
    Base class for creating Pydantic models with serialization and deserialization methods.
    """
    _id: Union[bson.objectid.ObjectId, int] = -1

    def serialize(self):
        """
        Serializes the model instance into a dictionary.

        :return: A dictionary representation of the model instance.
        :raises ValidationError: If the model instance is invalid.
        """
        try:
            return self.model_dump()
        except ValidationError as e:
            print(e)

    @classmethod
    def deserialize(cls, serialized_data: dict) -> 'Base':
        """
        Deserializes a dictionary into a model instance.

        :param serialized_data: A dictionary representation of the model instance.
        :return: A model instance.
        :raises ValidationError: If the input dictionary is invalid.
                """
        try:
            return cls(**serialized_data)
        except ValidationError as e:
            print(e)


class Task(Base):
    pass
