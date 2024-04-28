from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
 
load_dotenv()

CONNECTION_STRING = os.environ.get("CONNECTION_STRING")
DB_NAME = os.environ.get("DB_NAME")

class DatabaseManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.client = MongoClient(CONNECTION_STRING, server_api=ServerApi('1'))
            cls._instance.db = cls._instance.client[DB_NAME]
        return cls._instance

    @classmethod
    def get_database(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance.db

  
database_manager = DatabaseManager()

