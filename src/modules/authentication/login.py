import traceback
import os, jwt
from src.modules.db import MongoDB
from  werkzeug.security import check_password_hash
from dotenv import load_dotenv


load_dotenv()

secret_key = os.getenv('SECRET_KEY')

def login(data):
    if not ('email' in data and 'password' in data):
        return {"status":422, "message":"Required feilds are not found"}
    if data["email"] and data["password"]:
        try:
            user_id =  data["email"]
            password = data["password"]
            db = MongoDB()
            user = db.get_user({"user_id":user_id})
            if user:
                if check_password_hash(user["password"], password):
                    token = jwt.encode({'user_id':user['user_id']}, secret_key)
                    return {"status":200, "authToken":token}
                else:
                    return {"status":403, "message":"Wrong id or password"}
            else:
                return {"status":403, "message":"Wrong id or password"}
        except Exception as e:
            print(traceback.format_exc(e))
            return {"status":500, "message":"Something went worng"}
    else:
        return {"status":422, "message":"Required feilds are not found"}



def validate_login(token):
    if not ("authToken" in token):
        return {"status":401, "message":"Token is missing"}
    if token['authToken']:
        try:
            user_id = jwt.decode(token['authToken'], secret_key, algorithms=["HS256"])
            return {"status":200, "user_id":user_id}
        except Exception as e:
            print(traceback.format_exc(e))
            return {"status":401, "message":"Invalid token"}
    else:
        return {"status":401, "message":"Invalid token"}


        

