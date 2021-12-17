Welcome file
Welcome file
# Citymall-task

Api's  bulid in Flask perfom to manage Todo Task.


## Installation
### Requrements : 
**Python**: `3.10.0`

**MongoDB**

create ```.env``` file with variables

    DB_URI= <Enter Database Url>
    DATABASE = TodoApp
    COLLECTION = sample1
    SECRET_KEY = <Enter Secret key to genrate jwt>

For linux : 
```bash run.sh```

For other os:
```bash
python3 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```



##  To create user

url : ```/user/create```

method : ```POST```

request body :  

    {
        "name":"<value --Optinal>",
        
        "email":"<value>", 
        
        "password":"<value>",
      
    }

##  To login

url : ```/user/login```

method : ```POST```

request body :  

    {
        "email":"<value>", 
        
        "password":"<value>" 
    }

##  To create task

url : ```/todo/create```

method : ```POST```

request header : 

    "authToken" : "<token>" 

request body :  

    {
        "title":"<value>", 
    }

##  To update task

url : ```/todo/update<taskid>```

method : ```POST```

request header : 

    "authToken" : "<token>" 
    
request body :  

    {
        "title":"<value>", 
    }


##  To delete task

url : ```/todo/delete<taskid>```

method : ```GET```

request header : 

    "authToken" : "<token>" 



##  To list tasks
url : ```/todo/list```

method : ```GET```

request header :  

    "authToken" : "<token>"
    
##  Note
>**Note:  Task identified by based on uuid()

>**Note:  mime type for hole application is 'application/json'

>**Note:  Database Sample Schema

   

     {
            "_id": {
                "$oid": "61bb414683ea3057af8d2ef1"
            },
            "name": "Aisha Tayyaba",
            "user_id": "example@gmail.com",
            "password": "pbkdf2:sha256:260000$wjtTXbzXTm26HeJz$5350efbd8bb18e81c6db671ad0e822e82dcfcf87a3d90ab4994bac8107b28378",
            "tasklist": {
                "8eec9230-50b8-4808-9961-5b908c03f703": "example task 1",
                "942ab88d-595f-417b-963d-59147cbc455f": "example task 2"
            }
        }

