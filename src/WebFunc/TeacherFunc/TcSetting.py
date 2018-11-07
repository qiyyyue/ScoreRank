# api of sub_page setting
# user's setting

from flask import request, session, json
from flask import Blueprint, render_template, redirect
from TeacherInfoDB import *
from ParticipantDB import *
from PerformanceDB import *
from AppInfoDB import *
from CourseInfoDB import *
from DuolingoAPI import *

tc_setting_bp = Blueprint('tc_setting_bp',__name__)


@tc_setting_bp.route("/TcGetSelfInfo", methods=["POST", "GET"])
def teacher_get_self_info():
    username = request.form.get('username', None)

    userinfo = tc_query_info_by_username(username)
    print(userinfo)
    teacher_id = tc_query_id_by_name(userinfo[0])
    course_list = course_id_list_by_tc_id(teacher_id)
    # print(userinfo)
    if userinfo == None:
        return json.dumps({"code": "False", 'msg': 'query userinfo fail'}, ensure_ascii=False)
    else:
        self_info = {}
        self_info['username'] = userinfo[0]
        self_info['teacher_name'] = userinfo[1]
        self_info['birthday'] = str(userinfo[2])
        self_info['teacher_number'] = userinfo[3]
        self_info['CI'] = userinfo[4]
        self_info['continent'] = userinfo[5]
        self_info['country'] = userinfo[6]
        self_info['city'] = userinfo[7]
        self_info['course_list'] = course_list
        # print(self_info)
        return json.dumps({"code": "True", 'self_info': self_info}, ensure_ascii=False)

@tc_setting_bp.route("/TcChangeUsername", methods=["POST", "GET"])
def teacher_change_username():
    username = request.form['username']

    new_username = request.form['new_username']

    if stu_change_username(username, new_username):
        return json.dumps({"code": "True"}, ensure_ascii=False)
    else:
        return json.dumps({"code": "False", 'msg': 'change username fail'}, ensure_ascii=False)


@tc_setting_bp.route("/TcChangePassword", methods=["POST", "GET"])
def teacher_change_password():
    username = request.form['username']

    password = request.form['password']

    #print(username, password)
    if tc_change_password(username, password):
        return json.dumps({"code": "True"}, ensure_ascii=False)
    else:
        return json.dumps({"code": "False", 'msg': 'change password fail'}, ensure_ascii=False)

@tc_setting_bp.route("/TcSetWight", methods=["POST", 'GET'])
def teacher_set_weight():
    username = request.form.get('username', None)
    app_id = (int)(request.form.get('app_id', None))
    weight = (int)(request.form.get('weight', None))

    #print(app_id, weight)
    if app_change_weigh(app_id, weight):
        return json.dumps({"code": "True"}, ensure_ascii=False)
    else:
        return json.dumps({"code": "False", 'msg': 'change weight fail'}, ensure_ascii=False)

@tc_setting_bp.route("/TcGetWight", methods=["POST", 'GET'])
def teacher_get_weight():
    username = request.form.get('username', None)
    app_id = (int)(request.form.get('app_id', None))

    weight = app_get_weight(app_id)

    if weight == -1:
        return json.dumps({"code": "False", 'msg': 'get weight fail'}, ensure_ascii=False)
    return json.dumps({"code": "True", 'weight': weight}, ensure_ascii=False)