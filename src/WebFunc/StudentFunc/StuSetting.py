# api of sub_page setting
# user's setting

from flask import request, session, json
from flask import Blueprint, render_template, redirect
from StudentInfoDB import *
from ParticipantDB import *
from PerformanceDB import *
from AppInfoDB import *
from DuolingoAPI import *

stu_setting_bp = Blueprint('stu_setting_bp',__name__)


@stu_setting_bp.route("/StuGetSelfInfo", methods=["POST", "GET"])
def student_get_self_info():
    username = request.form.get('username', None)

    userinfo = stu_query_info_by_username(username)
    # print(userinfo)
    if userinfo == None:
        return json.dumps({"code": "False", 'msg': 'query userinfo fail'}, ensure_ascii=False)
    else:
        self_info = {}
        self_info['username'] = userinfo[0]
        self_info['student_name'] = userinfo[1]
        self_info['birthday'] = str(userinfo[2])
        self_info['student_number'] = userinfo[3]
        self_info['CI'] = userinfo[4]
        self_info['continent'] = userinfo[5]
        self_info['country'] = userinfo[6]
        self_info['city'] = userinfo[7]
        # print(self_info)
        return json.dumps({"code": "True", 'self_info': self_info}, ensure_ascii=False)

@stu_setting_bp.route("/StuChangeUsername", methods=["POST", "GET"])
def student_change_username():
    username = request.form['username']

    new_username = request.form['new_username']

    if stu_change_username(username, new_username):
        return json.dumps({"code": "True"}, ensure_ascii=False)
    else:
        return json.dumps({"code": "False", 'msg': 'change username fail'}, ensure_ascii=False)


@stu_setting_bp.route("/StuChangePassword", methods=["POST", "GET"])
def student_change_password():
    username = request.form['username']

    password = request.form['password']

    if stu_change_password(username, password):
        return json.dumps({"code": "True"}, ensure_ascii=False)
    else:
        return json.dumps({"code": "False", 'msg': 'change password fail'}, ensure_ascii=False)

@stu_setting_bp.route("/StuLinkDuolingo", methods=["POST", 'GET'])
def student_link_duolingo():
    username = request.form.get('username', None)
    duo_username = request.form.get('duo_username', None)
    duo_password = request.form.get('duo_password', None)

    # if 'username' not in session:
    #     return json.dumps({"code": "False", "msg": "no log in"}, ensure_ascii=False)

    try:
        stu_id = stu_query_id_by_name(username)
        if stu_id == -1:
            return json.dumps({"code": "False", 'msg': 'wrong username'}, ensure_ascii=False)

        duolingo_score = get_duolingo_score(duo_username, duo_password)
        if duolingo_score == {}:
            return json.dumps({"code": "False", 'msg': 'wrong duolingo info'}, ensure_ascii=False)

        if not performance_clear_by_id(stu_id):
            return json.dumps({"code": "False", 'msg': 'clear performance info failed'}, ensure_ascii=False)
        if not participant_clear_by_id(stu_id):
            return json.dumps({"code": "False", 'msg': 'clear participant info failed'}, ensure_ascii=False)

        point = duolingo_score['points']
        level = duolingo_score['level']

        participant_id = participant_insert(stu_id, 1, duo_username, duo_password, level, point)
        if participant_id == -1:
            return json.dumps({"code": "False", 'msg': 'insert participant error'}, ensure_ascii=False)

        performance_id = performance_insert(stu_id, 1)
        if performance_id == -1:
            return json.dumps({"code": "False", 'msg': 'insert performance error'}, ensure_ascii=False)

        if not performance_update(performance_id, level, point):
            return json.dumps({"code": "False", 'msg': 'update performance error'}, ensure_ascii=False)
    except Exception as e:
        return json.dumps({"code": "False", 'msg': 'bind wrong'}, ensure_ascii=False)

    return json.dumps({"code": "True"}, ensure_ascii=False)