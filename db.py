from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()
var_name = os.getenv('MONGO')


class Db:
    pass


class MongoDb(Db):
    db = MongoClient(var_name)

    def insert_one(self):
        pass

    def insert_many(self):
        pass

    def find_one(self):
        pass

    def find_many(self):
        pass

    def update_one(self):
        pass

    def update_many(self):
        pass

    def delete_one(self):
        pass

    def delete_many(self):
        pass
