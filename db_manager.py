from db import Db
from pymongo.results import (InsertOneResult,
                             UpdateResult,
                             DeleteResult)
from typing import (Optional,
                    List,
                    Dict,
                    Any)


class DbManager:
    """
    A class used to manage database operations.

    Attributes
    ----------
    db : Db
        The database object used for performing database operations.

    Methods
    -------
    load_one(data: dict) -> Optional[InsertOneResult]:
        Inserts a single document into the database.
    get_one(fltr: dict) -> Optional['Model']:
        Retrieves a single document from the database matching the filter.
    get_many(*args, **kwargs) -> Optional[List['Model']]:
        Retrieves multiple documents from the database.
    update_one(fltr: Dict[str, Any], update: Dict[str, Any], *args, **kwargs) -> Optional[UpdateResult]:
        Updates a single document in the database matching the filter.
    delete_one(fltr: Dict[str, Any], *args, **kwargs) -> Optional[DeleteResult]:
        Deletes a single document from the database matching the filter.
    """
    def __init__(self, db: Db):
        """
        Initializes the DbManager with the given database object.

        Parameters
        ----------
        db : Db
            The database object used for performing database operations.
        """
        self.db = db

    def load_one(self, data: dict) -> Optional[InsertOneResult]:
        """
        Inserts a single document into the database.

        Parameters
        ----------
        data : dict
            The document to be inserted.

        Returns
        -------
        Optional[InsertOneResult]
            The result of the insertion operation.
        """
        return self.db.insert_one(data)

    def get_one(self, fltr: dict) -> Optional['Model']:
        """
        Retrieves a single document from the database matching the filter.

        Parameters
        ----------
        fltr : dict
            The filter to apply.

        Returns
        -------
        Optional['Model']
            The retrieved document.
        """
        return self.db.find_one(fltr)

    def get_many(self, *args, **kwargs) -> Optional[List['Model']]:
        """
        Retrieves multiple documents from the database.

        Returns
        -------
        Optional[List['Model']]
            A list of retrieved documents.
        """
        return self.db.find_many(*args, **kwargs)

    def update_one(self, fltr: Dict[str, Any], update: Dict[str, Any], *args, **kwargs) -> Optional[UpdateResult]:
        """
        Updates a single document in the database matching the filter.

        Parameters
        ----------
        fltr : Dict[str, Any]
            The filter to apply.
        update : Dict[str, Any]
            The update to apply.

        Returns
        -------
        Optional[UpdateResult]
            The result of the update operation.
        """
        return self.db.update_one(fltr, update, *args, **kwargs)

    def delete_one(self, fltr: Dict[str, Any], *args, **kwargs) -> Optional[DeleteResult]:
        """
        Deletes a single document from the database matching the filter.

        Parameters
        ----------
        fltr : Dict[str, Any]
            The filter to apply.

        Returns
        -------
        Optional[DeleteResult]
            The result of the delete operation.
        """
        return self.db.delete_one(fltr, *args, **kwargs)

