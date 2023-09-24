from db import Db
from pymongo.results import (InsertOneResult,
                             UpdateResult,
                             DeleteResult)
from typing import (Optional,
                    List,
                    Dict,
                    Any)


class DbManager:
    def __init__(self, db: Db):
        self.db = db

    def load_one(self, data: dict) -> Optional[InsertOneResult]:
        return self.db.insert_one(data)

    def get_one(self, fltr: dict) -> Optional['Model']:
        return self.db.find_one(fltr)

    def get_many(self, *args, **kwargs) -> Optional[List['Model']]:
        return self.db.find_many(*args,
                                 **kwargs)

    def update_one(self,
                   fltr: Dict[str, Any],
                   update: Dict[str, Any],
                   *args,
                   **kwargs) -> Optional[UpdateResult]:
        return self.db.update_one(fltr,
                                  update,
                                  *args,
                                  **kwargs)

    def delete_one(self,
                   fltr: Dict[str, Any],
                   *args,
                   **kwargs) -> Optional[DeleteResult]:
        return self.db.delete_one(fltr,
                                  *args,
                                  **kwargs)

