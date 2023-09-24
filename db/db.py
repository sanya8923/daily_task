from dotenv import load_dotenv
import os
from pymongo import MongoClient
from pymongo.results import (InsertOneResult,
                             UpdateResult,
                             DeleteResult)
from pymongo.errors import PyMongoError
from typing import (Any,
                    List,
                    Dict,
                    Optional)
from abc import (ABC,
                 abstractmethod)
from tkinter import messagebox


load_dotenv()
var_name = os.getenv('MONGO')
try:

    cluster = MongoClient(var_name)

except PyMongoError as e:
    with open('log.txt', 'a') as log_file:
        log_file.write(f"PyMongoError: {e}\n")
    messagebox.showerror('Error', 'An error occurred while working with the database. Please try again.')


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
    try:

        db = cluster['daily_task']
        collection = db['tasks']

    except PyMongoError as e:
        with open('log.txt', 'a') as log_file:
            log_file.write(f"PyMongoError: {e}\n")
        messagebox.showerror('Error', 'An error occurred while working with the database. Please try again.')

    def insert_one(self, data: dict, *args, **kwargs) -> Optional[InsertOneResult]:
        """
        Inserts a single document into the collection.

        :param data: The document to be inserted.
        :return: The result of the insertion.
        """
        try:

            return self.collection.insert_one(data)

        except PyMongoError as e:
            with open('log.txt', 'a') as log_file:
                log_file.write(f"PyMongoError: {e}\n")
            messagebox.showerror('Error', 'An error occurred while working with the database. Please try again.')
            return None

    def find_one(self, fltr: Dict[str, Any], *args, **kwargs) -> Optional['Model']:
        """
        Finds a single document in the collection.

        :param fltr: The filter to apply for the search.
        :return: The document found or None if no document matches the filter.
        """
        try:

            return self.collection.find_one(fltr)

        except PyMongoError as e:
            with open('log.txt', 'a') as log_file:
                log_file.write(f"PyMongoError: {e}\n")
            messagebox.showerror('Error', 'An error occurred while working with the database. Please try again.')
            return None

    def find_many(self, *args, **kwargs) -> Optional[List['Model']]:
        """
        Finds multiple documents in the collection.

        :return: A list of documents found or None if no documents match the filter.
        """
        try:

            cursor = self.collection.find(*args, **kwargs)
            result = [doc for doc in cursor]

            if result:
                return result
            else:
                return None

        except PyMongoError as e:
            with open('log.txt', 'a') as log_file:
                log_file.write(f"PyMongoError: {e}\n")
            messagebox.showerror('Error', 'An error occurred while working with the database. Please try again.')
            return None

    def update_one(self, fltr: Dict[str, Any], update: Dict[str, Any], *args, **kwargs) -> Optional[UpdateResult]:
        """
        Updates a single document in the collection.

        :param fltr: The filter to apply for the search.
        :param update: The modifications to apply.
        :return: The result of the update.
        """
        try:

            return self.collection.update_one(fltr, update)

        except PyMongoError as e:
            with open('log.txt', 'a') as log_file:
                log_file.write(f"PyMongoError: {e}\n")
            messagebox.showerror('Error', 'An error occurred while working with the database. Please try again.')
            return None

    def delete_one(self, fltr: Dict[str, Any], *args, **kwargs) -> Optional[DeleteResult]:
        """
        Deletes a single document from the collection.

        :param fltr: The filter to apply for the search.
        :return: The result of the deletion.
        """
        try:

            return self.collection.delete_one(fltr)

        except PyMongoError as e:
            with open('log.txt', 'a') as log_file:
                log_file.write(f"PyMongoError: {e}\n")
            messagebox.showerror('Error', 'An error occurred while working with the database. Please try again.')
            return None

