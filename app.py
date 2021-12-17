from flask import Flask, Response
import json
from src.routes.authetication import auth_handler
from flask_cors import CORS
from src.routes.todoapp import todoapp_handler


app = Flask(__name__)
CORS(app)

app.register_blueprint(auth_handler)
app.register_blueprint(todoapp_handler)


if __name__ == "__main__":
    app.run(threaded=True, debug=True,port=5000)