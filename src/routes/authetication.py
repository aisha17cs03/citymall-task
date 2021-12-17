from flask import Blueprint, request, Response
import traceback, os
from src.modules.authentication import login, signup
import json

auth_handler = Blueprint("auth_service",__name__,url_prefix='/user')

@auth_handler.route('/login',methods=['POST'])
def user_login():
    try:
        req_body = request.get_json()
        if not req_body:
            return Response(json.dumps({"message":"Required field not found"}),status=422,mimetype='application/json')
        response = login(data=req_body)
        if response['status']==200:
            return Response(json.dumps({"authToken":response['authToken']}),status=response['status'],mimetype='application/json')
        else:
            return Response(json.dumps({"message":response['message']}),status=response['status'],mimetype='application/json')
    except Exception as e:
        print(traceback.format_exc(e))
        return Response(json.dumps({"message":"Interval sever error"}),status=500,mimetype='application/json')



@auth_handler.route('/create',methods=['POST'])
def user_create():
    try:
        req_body = request.get_json()
        if not req_body:
            return Response(json.dumps({"message":"Required field not found"}),status=422,mimetype='application/json')
        response = signup(data=req_body)
        return Response(json.dumps({"message":response['message']}),status=response['status'],mimetype='application/json')
    except Exception as e:
        print(traceback.format_exc(e))
        return Response(json.dumps({"message":"Interval sever error"}),status=500,mimetype='application/json')




