from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()
var_name = os.getenv('MONGO')


class Db:
    pass


class MongoDb(Db):
    db = MongoClient(var_name)

