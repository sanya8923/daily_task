from pydantic import BaseModel
from typing import Union
import bson


class Base(BaseModel):
    _id: Union[bson.objectid.ObjectId, int] = -1
