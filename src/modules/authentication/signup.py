import traceback
from src.modules.db import MongoDB
from  werkzeug.security import generate_password_hash

def signup(data):
    if not ('email' in data and 'password' in data):
        return {"status":422, "message":"Required feilds are not found"}
    if data["email"] and data["password"]:
        try:
            user_id =  data["email"]
            password = data["password"]
            db = MongoDB()
            exist = db.get_user({"user_id":user_id})
            if exist:
                return {"status":409, "message":"User already exits"}
            else:
                name = data['name'] if 'name' in data else "Unknown"
                new_password = generate_password_hash(password)
                user_data = db.create_user(name=name, user_id=user_id, password=new_password)
                if user_data:
                    return {"status":200, "message":"Signup successfull"}
        except Exception as e:
            print(traceback.format_exc(e))
            return {"status":500, "message":"Something went worng"}

    else:
        return {"status":422, "message":"Required feilds are not found"}
    