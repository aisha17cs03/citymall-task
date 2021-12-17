from logging import exception
from pymongo import MongoClient  
from dotenv import load_dotenv
import os, traceback
import certifi, uuid

from pymongo.collection import ReturnDocument


ca = certifi.where()

load_dotenv()

dbUri = os.getenv('DB_URI')
databaseName = os.getenv('DATABASE')
collectionName = os.getenv('COLLECTION')

class MongoDB:
    def __init__(self):
        self.client = MongoClient(dbUri, tlsCAFile=ca)
        
        cursor = self.client[databaseName]
        self.collection = cursor[collectionName]
      

    def create_user(self, name, user_id, password):
        data = {"name":name, "user_id":user_id, "password":password, "tasklist":{}}
        try:
            response = self.collection.insert_one(data)
            return response.inserted_id
        except Exception as e:
            print(traceback.format_exc(e))
            return False

    def create_task(self, task_name, user_id):
        taskId = str(uuid.uuid4())
        data = {'$set': {f'tasklist.{taskId}':task_name}}
        id = {'user_id':user_id}
        try:
            response = self.collection.update_one(id, data)
            return response
        except Exception as e:
            print(traceback.format_exc(e))
            return False
    
    def update_task(self, task_id, user_id, task_name):
        data = {'$set': {f"tasklist.{task_id}":task_name}}
        id = {'user_id':user_id}
        try:
            response = self.collection.update_one(id, data,upsert=False)
            return response
        except Exception as e:
            print(traceback.format_exc(e))
            return False

    def delete_task(self, task_id, user_id):
        data = {'$unset': {f"tasklist.{task_id}":1}}
        id = {'user_id':user_id}
        try:
            response = self.collection.update_one(id, data,upsert=False)
            return response
        except Exception as e:
            print(traceback.format_exc(e))
            return False
    
    def get_user(self,data):
        try: 
            doc = self.collection.find_one(data)
            return doc
        except Exception as e:
            print(traceback.format_exc(e))
            return False

    def get_task(self,user_id,data=None):
        try:
            if data:
                task = self.collection.find_one(data,{'tasklist':1})
                return task
            else:
                taskList = self.collection.find({'user_id':user_id},{'tasklist':1})
                return taskList[0]['tasklist']
        except Exception as e:
            print(traceback.format_exc(e))
            return False
      

    



