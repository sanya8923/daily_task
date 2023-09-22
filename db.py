from dotenv import load_dotenv
import os
from pymongo import MongoClient
from pymongo.results import InsertOneResult
from typing import Any, List, Dict, Optional


load_dotenv()
var_name = os.getenv('MONGO')
cluster = MongoClient(var_name)


class Db:
    pass


class MongoDb(Db):
    db = cluster['daily_task']
    collection = db['tasks']

    def insert_one(self, data: dict, *args, **kwargs) -> InsertOneResult:
        return self.collection.insert_one(data)

    def insert_many(self, data: List[Dict[str, Any]], *args, **kwargs):
        self.collection.insert_many(data)

    def find_one(self, fltr: Dict[str, Any], *args, **kwargs) -> 'Model':
        return self.collection.find_one(fltr)

    def find_many(self, *args, **kwargs) -> Optional[List['Model']]:
        result = []
        cursor = self.collection.find(*args, **kwargs)

        try:
            result = [doc for doc in cursor]
        except Exception as e:
            print(e)

        if len(result) > 0:
            return result
        else:
            return None

    def update_one(self):
        pass

    def update_many(self):
        pass

    def delete_one(self):
        pass

    def delete_many(self):
        pass
