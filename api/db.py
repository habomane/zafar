from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
 
load_dotenv()

CONNECTION_STRING = os.environ.get("CONNECTION_STRING")
DB_NAME = os.environ.get("DB_NAME")

def get_database():
   client = MongoClient(CONNECTION_STRING, server_api=ServerApi('1'))
   try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    return client[DB_NAME]
   except Exception as e:
        print(e)

  
if __name__ == "__main__":   
   dbname = get_database()
   


