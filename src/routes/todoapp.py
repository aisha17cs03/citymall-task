from flask import Blueprint, request, Response, g
import traceback, os
import json
from src.modules.utils import *
from src.modules.authentication import validate_login
todoapp_handler = Blueprint("app_service",__name__,url_prefix='/todo')

@todoapp_handler.before_request
def before_request():
    response = validate_login(token=request.headers)
    if response['status']==200:
        g.user_id=response['user_id']
    else:
        return Response(json.dumps({"message":response['message']}),status=response['status'],mimetype='application/json')

@todoapp_handler.route('/create',methods=['POST'])
def create_task():
    try:
        req_body = request.get_json()
        if not req_body:
            return Response(json.dumps({"message":"Required field not found"}),status=422,mimetype='application/json')
        response = create_todo_task(task_name=req_body, user_id=g.user_id['user_id'])
        return Response(json.dumps({"message":response['message']}),status=response['status'],mimetype='application/json')
    except Exception as e:
        print(traceback.format_exc(e))
        return Response(json.dumps({"message":"Interval sever error"}),status=500,mimetype='application/json')



@todoapp_handler.route('/update/<string:task_id>',methods=['POST'])
def update_task(task_id):
    try:
        req_body = request.get_json()
        if not req_body:
            return Response(json.dumps({"message":"Required field not found"}),status=422,mimetype='application/json')
        response = update_todo_task(task_id, req_body, g.user_id['user_id'])
        return Response(json.dumps({"message":response['message']}),status=response['status'],mimetype='application/json')
    except Exception as e:
        print(traceback.format_exc(e))
        return Response(json.dumps({"message":"Interval sever error"}),status=500,mimetype='application/json')


@todoapp_handler.route('/delete/<string:task_id>',methods=['GET'])
def delete_task(task_id):
    try:
        response = delete_todo_task(task_id, g.user_id['user_id'])
        return Response(json.dumps({"message":response['message']}),status=response['status'],mimetype='application/json')
    except Exception as e:
        print(traceback.format_exc(e))
        return Response(json.dumps({"message":"Internal sever error"}),status=500,mimetype='application/json')


@todoapp_handler.route('/list', methods=['GET'])
def list_task(task_id=None):
    #task_id = request.args.get('task_id')
    try:
        response = list_todo_task(g.user_id['user_id'], task_id)
        return Response(json.dumps({"task_list":response['total_task']}),status=response['status'],mimetype='application/json')
    except Exception as e:
        print(traceback.format_exc(e))
        return Response(json.dumps({"message":"Interval sever error"}),status=500,mimetype='application/json')

