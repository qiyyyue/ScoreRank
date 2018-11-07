from flask import request, session, json
from StudentInfoDB import *
from TeacherInfoDB import *
from flask import Blueprint, render_template, redirect, make_response
log_reg_bp = Blueprint('log_reg_bp',__name__)

@log_reg_bp.route('/Login', methods=['POST', 'GET'])
def login():

    username = request.form.get('username', None)
    password = request.form.get('password', None)

    #print(username, password)

    if stu_login(username, password):
        return json.dumps({"code": "True", "user_role": 1}, ensure_ascii=False)
    elif tc_login(username, password):
        return json.dumps({"code": "True", "user_role": 0}, ensure_ascii=False)
    else:
        return json.dumps({"code": "False"}, ensure_ascii=False)

@log_reg_bp.route('/StuRegister', methods=['POST', 'GET'])
def student_register():
    username = request.form['username']
    password = request.form['password']

    if stu_login(username, password):
        return json.dumps({"code": "False", "msg": "username already exists"}, ensure_ascii=False)

    if stu_register(username, password) != -1:
        return json.dumps({"code": "True"}, ensure_ascii=False)
    else:
        return json.dumps({"code": "False", "msg": "sign failed"}, ensure_ascii=False)


@log_reg_bp.route('/TeacherRegister', methods=['POST', 'GET'])
def teacher_register():
    username = request.form['username']
    password = request.form['password']

    if tc_login(username, password):
        return json.dumps({"code": "False", "msg": "username already exists"}, ensure_ascii=False)

    if tc_register(username, password) != -1:
        return json.dumps({"code": "True"}, ensure_ascii=False)
    else:
        return json.dumps({"code": "False", "msg": "sign failed"}, ensure_ascii=False)