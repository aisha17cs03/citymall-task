from pymongo import message
from src.modules.db import MongoDB

def create_todo_task(task_name, user_id):
    if not ('title' in task_name):
        return {"status":422, "message":"Required feilds are not found"}
    if task_name['title']:
        try:
            db = MongoDB()
            response = db.create_task(task_name['title'], user_id)
            if response.modified_count:
                return {"status":200, "message":"sucessfully created"}
            else:
                return {"status":500, "message":"Oops can not create task"}
        except Exception as e:
            return {"status":500, "message":"Oops can not create task"}
    else:
        return {"status":422, "messaage":"Required field are not found"}

def update_todo_task(task_name, user_id):
    if not ('title' in task_name):
        return {"status":422, "message":"Required feilds are not found"}
    if task_name['title']:
        try:
            db = MongoDB()
            response = db.create_task(task_name['title'], user_id)
            if response.modified_count:
                return {"status":200, "message":"sucessfully created"}
            else:
                print(user_id, type(user_id))
                return {"status":500, "message":"Oops can not create task"}
        except Exception as e:
            print("exception")
            return {"status":500, "message":"Oops can not create task"}
    else:
        return {"status":422, "messaage":"Required field are not found"}



def update_todo_task(task_id, task_name, user_id):
    if not ('title' in task_name):
        return {"status":422, "message":"Required feilds are not found"}
    if task_name['title']:
        try:
            db = MongoDB()
            response = db.update_task(task_id, user_id, task_name['title'])
            if response.modified_count:
                return {"status":200, "message":"sucessfully updated"}
            else:
                return {"status":404, "message":"Task not found"}
        except Exception as e:
            return {"status":500, "message":"Oops can not update task"}
    else:
        return {"status":422, "messaage":"Required field are not found"}



def delete_todo_task(task_id, user_id):
    try:
        db = MongoDB()
        response = db.delete_task(task_id, user_id)
        if response.modified_count:
            return {"status":200, "message":"sucessfully deleted"}
        else:
            return {"status":404, "message":"Task not Found"}
    except Exception as e:
        return {"status":500, "message":"Oops can not delete data"}


def list_todo_task(user_id, task_id=None):
    total_task = []
    try:
        db = MongoDB()
        if task_id:
            to_get = {'user_id':user_id, f"tasklist.{task_id}" : { '$exists' : True }}
            response = db.get_task(user_id, to_get)
            if response:
                for task in response['tasklist'].items():
                    total_task.append({f"{task[0]}":task[1]})
        else:
            response = db.get_task(user_id, task_id)
            if response:
                for task in response.items():
                    total_task.append({f"{task[0]}":task[1]})
        return {"status":200, "total_task":total_task}
    except Exception as e:
        return {"status":500, "message":"Oops can not delete data"}