from flask import request, session, json
from UserInfoDB import *
from ParticipantDB import *
from PerformanceDB import *
from AppInfoDB import *
from DuolingoAPI import *
from flask import Blueprint, render_template, redirect, make_response
user_info = Blueprint('user_info',__name__)


@user_info.route("/LinkDuolingo", methods=["POST", 'GET'])
def link_duolingo():
    username = request.form['username']
    duo_username = request.form['duo_username']
    duo_password = request.form['duo_password']

    # if 'username' not in session:
    #     return json.dumps({"code": "False", "msg": "no log in"}, ensure_ascii=False)

    user_id = user_query_id_by_name(username)
    if user_id == -1:
        return json.dumps({"code": "False", 'msg': 'wrong username'}, ensure_ascii=False)

    duolingo_score = get_duolingo_score(duo_username, duo_password)
    if duolingo_score == {}:
        return json.dumps({"code": "False", 'msg': 'wrong duolingo info'}, ensure_ascii=False)

    if not performance_clear_by_id(user_id):
        return json.dumps({"code": "False", 'msg': 'clear performance info failed'}, ensure_ascii=False)
    if not participant_clear_by_id(user_id):
        return json.dumps({"code": "False", 'msg': 'clear participant info failed'}, ensure_ascii=False)

    point = duolingo_score['points']
    level = duolingo_score['level']

    participant_id = participant_insert(user_id, 1, duo_username, duo_password, level, point)
    if participant_id == -1:
        return json.dumps({"code": "False", 'msg': 'insert participant error'}, ensure_ascii=False)

    performance_id = performance_insert(user_id, 1)
    if performance_id == -1:
        return json.dumps({"code": "False", 'msg': 'insert performance error'}, ensure_ascii=False)

    if not performance_update(performance_id, level, point):
        return json.dumps({"code": "False", 'msg': 'update performance error'}, ensure_ascii=False)

    return json.dumps({"code": "True"}, ensure_ascii=False)

@user_info.route("/UserInfoUpdate", methods=["POST", "GET"])
def user_update():
    username = request.form['old_username']
    password = request.form['old_pwd']

    new_username = request.form['new_username']
    new_email = request.form['new_email']
    new_country = request.form['new_country']
    new_city = request.form['new_city']
    new_password = request.form['new_pwd']
    new_timezone = request.form['new_timezone']
    new_class = request.form['new_class']

    print(username, password, new_username, new_email, new_country, new_city, new_password, new_timezone, new_class)
    if not user_login(username, password):
        return json.dumps({"code": "False", 'msg': 'wrong old pwd'}, ensure_ascii=False)

    if user_info_update(username, new_username, new_password, new_email, new_country, new_city, new_timezone):
        return json.dumps({"code": "True"}, ensure_ascii=False)
    else:
        return json.dumps({"code": "True", 'msg': 'update user info erro'}, ensure_ascii=False)

@user_info.route('/login', methods=['POST', 'GET'])
def login():

    username = request.form.get('username', None)
    password = request.form.get('password', None)

    #print(username, password)


    if user_login(username, password):
        session['username'] = username
        user_role = user_query_role(username)
        return json.dumps({"code": "True", "user_role": user_role}, ensure_ascii=False)
    else:
        return json.dumps({"code": "False"}, ensure_ascii=False)

@user_info.route('/register', methods=['POST', 'GET'])
def register():
    username = request.form['username']
    password = request.form['password']

    if user_login(username, password):
        return json.dumps({"code": "False", "msg": "username already exists"}, ensure_ascii=False)

    if user_register(username, password) != -1:
        session['username'] = username
        return json.dumps({"code": "True"}, ensure_ascii=False)
    else:
        return json.dumps({"code": "False", "msg": "sign failed"}, ensure_ascii=False)