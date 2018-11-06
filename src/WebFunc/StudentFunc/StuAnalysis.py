import datetime

from flask import request, session, json
from flask import Blueprint, render_template, redirect
from StudentInfoDB import *
from PerformanceDB import *
from AppInfoDB import *
from DuolingoAPI import *

stu_analysis_bp = Blueprint('stu_analysis', __name__)

@stu_analysis_bp.route("/GetHistoryRank", methods=["POST", 'GET'])
def get_history_rank():
    period = request.form['period']
    username = request.form['username']

    stu_id = stu_query_id_by_name(username)
    if stu_id == -1:
        return json.dumps({"code": "False", 'msg': 'wrong username'}, ensure_ascii=False)

    if period == 'Weekly':
        history_rank_list = performance_get_history_rank_by_id(stu_id)
    else:
        history_rank_list = performance_get_history_rank_by_id(stu_id)

    # print(history_rank_list)
    return json.dumps({"code": "True", 'msg': '', "history_rank_list": history_rank_list}, ensure_ascii=False)


@stu_analysis_bp.route("/GetHistoryPoint", methods=["POST", 'GET'])
def get_history_point():
    period = request.form['period']
    username = request.form['username']

    stu_id = user_query_id_by_name(username)
    if stu_id == -1:
        return json.dumps({"code": "False", 'msg': 'wrong username'}, ensure_ascii=False)

    if period == 'Weekly':
        history_point_list = performance_get_history_point_by_id(stu_id)
    else:
        history_point_list = performance_get_history_point_by_id(stu_id)

    print(history_point_list)
    return json.dumps({"code": "True", 'msg': '', "history_point_list": history_point_list}, ensure_ascii=False)

@stu_analysis_bp.route("/GetHistoryAvgPoint", methods=["POST", 'GET'])
def get_history_avg_point():
    period = request.form['period']
    username = request.form['username']

    stu_info = stu_query_info_by_username(username)
    avg_his_point_list = [0 for i in range(7)]
    try:
        stu_list = stu_query_stus_by_loc(stu_info[5], stu_info[6], stu_info[7])
        count = 0
        for stu_id in stu_list:
            tmp_his_point_list = performance_get_history_point_by_id(stu_id)
            for i in range(len(avg_his_point_list)):
                avg_his_point_list[i] += tmp_his_point_list[i]
            count += 1
        if count > 0:
            for i in range(len(avg_his_point_list)):
                avg_his_point_list[i] = int(avg_his_point_list[i]/count)
    except Exception as e:
        print(e)
        return json.dumps({"code": "False", 'msg': ''}, ensure_ascii=False)
        #print(e)

    return json.dumps({"code": "True", 'msg': '', "history_avg_point_list": avg_his_point_list}, ensure_ascii=False)

@stu_analysis_bp.route("/GetHistoryDate", methods=["POST", 'GET'])
def get_history_date():
    period = request.form['period']
    username = request.form['username']

    history_date_list = []
    days = 7

    # if period == 'Weekly':
    #     days

    try:
        start_time = datetime.datetime.now() + datetime.timedelta(days=0 - days)
        for i in range(0, days):
            tmp_day = start_time + datetime.timedelta(days=i)
            history_date_list.append(tmp_day.strftime('%Y-%m-%d'))
    except:
        return json.dumps({"code": "False", 'msg': ''}, ensure_ascii=False)
        print(e)

    return json.dumps({"code": "True", 'msg': '', "history_date_list": history_date_list}, ensure_ascii=False)








# -------------------------------------------------------------------------------------------------
@stu_analysis_bp.route("/GetRank", methods=["POST", 'GET'])
def get_rank():
    username = request.form['username']

    user_id = user_query_id_by_name(username)
    if user_id == -1:
        return json.dumps({"code": "False", 'msg': 'wrong username'}, ensure_ascii=False)

    rank = performance_get_rank(user_id)
    if rank != -1:
        return json.dumps({"code": "True", 'msg': '', "rank": rank}, ensure_ascii=False)
    else:
        return json.dumps({"code": "False", 'msg': 'get rank fail'}, ensure_ascii=False)

@stu_analysis_bp.route("/GetRankAndPoint", methods=["POST", 'GET'])
def get_rank_point():
    username = request.form['username']

    user_id = user_query_id_by_name(username)
    if user_id == -1:
        return json.dumps({"code": "False", 'msg': 'wrong username'}, ensure_ascii=False)

    rank, point = performance_get_rank_point(user_id)
    if rank != -1:
        return json.dumps({"code": "True", 'msg': '', "rank": rank, 'point': point}, ensure_ascii=False)
    else:
        return json.dumps({"code": "False", 'msg': 'get rank fail'}, ensure_ascii=False)

@stu_analysis_bp.route("/GetLeaderBoard", methods=['POST', 'GET'])
def get_leader_board():
    leader_board_list = performance_get_all_rank()

    if leader_board_list != []:
        return json.dumps({"code": "True", 'msg': '', "leader_board_list": leader_board_list}, ensure_ascii=False)
    else:
        return json.dumps({"code": "False", 'msg': 'get leaderboard fail'}, ensure_ascii=False)

@stu_analysis_bp.route("/GetLeaderBoardAllDaily", methods=['POST', 'GET'])
def get_leader_board_All_daily():
    try:
        user_list = query_users_by_loc()

        re_list = []
        for user_id in user_list:
            user_name = query_user_name_by_id(user_id)
            point = performance_query_daily_by_id(user_id)
            re_list.append({'username': user_name, 'point': point})

        re_list.sort(key=lambda user_info: user_info['point'],reverse=True)
        for i in range(len(re_list)):
            re_list[i]['rank'] = i + 1

        return json.dumps({"code": "True", 'msg': '', "leader_board_list": re_list}, ensure_ascii=False)
    except:
        return json.dumps({"code": "False", 'msg': 'query erro'}, ensure_ascii=False)

@stu_analysis_bp.route("/GetLeaderBoardAllWeekly", methods=['POST', 'GET'])
def get_leader_board_All_weekly():
    try:
        user_list = query_users_by_loc()

        re_list = []
        for user_id in user_list:
            user_name = query_user_name_by_id(user_id)
            point = performance_query_weekly_by_id(user_id)
            re_list.append({'username': user_name, 'point': point})

        re_list.sort(key=lambda user_info: user_info['point'], reverse=True)
        for i in range(len(re_list)):
            re_list[i]['rank'] = i + 1
        return json.dumps({"code": "True", 'msg': '', "leader_board_list": re_list}, ensure_ascii=False)
    except:
        return json.dumps({"code": "False", 'msg': 'query erro'}, ensure_ascii=False)

@stu_analysis_bp.route("/GetLeaderBoardAllMonthly", methods=['POST', 'GET'])
def get_leader_board_All_Monthly():
    try:
        user_list = query_users_by_loc()

        re_list = []
        for user_id in user_list:
            user_name = query_user_name_by_id(user_id)
            point = performance_query_monthly_by_id(user_id)
            re_list.append({'username': user_name, 'point': point})
        re_list.sort(key=lambda user_info: user_info['point'], reverse=True)
        for i in range(len(re_list)):
            re_list[i]['rank'] = i + 1
        return json.dumps({"code": "True", 'msg': '', "leader_board_list": re_list}, ensure_ascii=False)
    except:
        return json.dumps({"code": "False", 'msg': 'query erro'}, ensure_ascii=False)

@stu_analysis_bp.route("/GetLeaderBoardCountryDaily", methods=['POST', 'GET'])
def get_leader_board_country_daily():
    country = request.form['country']
    try:
        user_list = query_users_by_loc(country=country)

        re_list = []
        for user_id in user_list:
            user_name = query_user_name_by_id(user_id)
            point = performance_query_daily_by_id(user_id)
            re_list.append({'username': user_name, 'point': point})
        re_list.sort(key=lambda user_info: user_info['point'], reverse=True)
        for i in range(len(re_list)):
            re_list[i]['rank'] = i + 1
        return json.dumps({"code": "True", 'msg': '', "leader_board_list": re_list}, ensure_ascii=False)
    except:
        return json.dumps({"code": "False", 'msg': 'query erro'}, ensure_ascii=False)

@stu_analysis_bp.route("/GetLeaderBoardCountryWeekly", methods=['POST', 'GET'])
def get_leader_board_country_weekly():
    country = request.form['country']
    try:
        user_list = query_users_by_loc(country=country)

        re_list = []
        for user_id in user_list:
            user_name = query_user_name_by_id(user_id)
            point = performance_query_weekly_by_id(user_id)
            re_list.append({'username': user_name, 'point': point})
        re_list.sort(key=lambda user_info: user_info['point'], reverse=True)
        for i in range(len(re_list)):
            re_list[i]['rank'] = i + 1
        return json.dumps({"code": "True", 'msg': '', "leader_board_list": re_list}, ensure_ascii=False)
    except:
        return json.dumps({"code": "False", 'msg': 'query erro'}, ensure_ascii=False)


@stu_analysis_bp.route("/GetLeaderBoardCountryMonthly", methods=['POST', 'GET'])
def get_leader_board_country_monthly():
    country = request.form['country']
    try:
        user_list = query_users_by_loc(country=country)

        re_list = []
        for user_id in user_list:
            user_name = query_user_name_by_id(user_id)
            point = performance_query_monthly_by_id(user_id)
            re_list.append({'username': user_name, 'point': point})
        re_list.sort(key=lambda user_info: user_info['point'], reverse=True)
        for i in range(len(re_list)):
            re_list[i]['rank'] = i + 1
        return json.dumps({"code": "True", 'msg': '', "leader_board_list": re_list}, ensure_ascii=False)
    except:
        return json.dumps({"code": "False", 'msg': 'query erro'}, ensure_ascii=False)



