from dotenv import load_dotenv
import os
from pymongo import MongoClient
from pymongo.results import InsertOneResult, UpdateResult, DeleteResult
from typing import Any, List, Dict, Optional
from logger import print, log_function
from abc import ABC, abstractmethod


load_dotenv()
var_name = os.getenv('MONGO')
cluster = MongoClient(var_name)


class Db(ABC):
    """
    Base class for database interaction.
    """
    @abstractmethod
    def insert_one(self, data: dict, *args, **kwargs):
        pass

    @abstractmethod
    def find_one(self, fltr: Dict[str, Any], *args, **kwargs):
        pass

    @abstractmethod
    def find_many(self, *args, **kwargs):
        pass

    @abstractmethod
    def update_one(self, fltr: Dict[str, Any], update: Dict[str, Any], *args, **kwargs):
        pass

    @abstractmethod
    def delete_one(self, fltr: Dict[str, Any], *args, **kwargs):
        pass


class MongoDb(Db):
    """
    MongoDB's interaction class, inheriting from the base Db class.
    Provides methods for basic CRUD operations.
    """
    db = cluster['daily_task']
    collection = db['tasks']

    @log_function
    def insert_one(self, data: dict, *args, **kwargs) -> InsertOneResult:
        """
        Inserts a single document into the collection.

        :param data: The document to be inserted.
        :return: The result of the insertion.
        """
        return self.collection.insert_one(data)

    @log_function
    def find_one(self, fltr: Dict[str, Any], *args, **kwargs) -> Optional['Model']:
        """
        Finds a single document in the collection.

        :param fltr: The filter to apply for the search.
        :return: The document found or None if no document matches the filter.
        """
        return self.collection.find_one(fltr)

    @log_function
    def find_many(self, *args, **kwargs) -> Optional[List['Model']]:
        """
        Finds multiple documents in the collection.

        :return: A list of documents found or None if no documents match the filter.
        """
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

    @log_function
    def update_one(self, fltr: Dict[str, Any], update: Dict[str, Any], *args, **kwargs) -> Optional[UpdateResult]:
        """
        Updates a single document in the collection.

        :param fltr: The filter to apply for the search.
        :param update: The modifications to apply.
        :return: The result of the update.
        """
        return self.collection.update_one(fltr, update)

    @log_function
    def delete_one(self, fltr: Dict[str, Any], *args, **kwargs) -> Optional[DeleteResult]:
        """
        Deletes a single document from the collection.

        :param fltr: The filter to apply for the search.
        :return: The result of the deletion.
        """
        return self.collection.delete_one(fltr)
