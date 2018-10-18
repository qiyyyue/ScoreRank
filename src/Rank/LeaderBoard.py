
from flask import request, session, json
from flask import Blueprint, render_template, redirect
from src.DB.UserInfoDB import *
from src.DB.ParticipantDB import *
from src.DB.PerformanceDB import *
from src.DB.AppInfoDB import *
from src.API.DuolingoAPI import *

leader_board = Blueprint('leader_board',__name__)

@leader_board.route("/GetHistoryRank", methods=["POST", 'GET'])
def get_history_rank():
    period = request.form['period']
    username = request.form['username']

    user_id = user_query_id_by_name(username)
    if user_id == -1:
        return json.dumps({"code": "False", 'msg': 'wrong username'}, ensure_ascii=False)

    if period == 'Weekly':
        history_rank_list = performance_get_history_rank_by_id(user_id)
    else:
        history_rank_list = performance_get_history_rank_by_id(user_id)

    print(history_rank_list)
    return json.dumps({"code": "True", 'msg': '', "history_rank_list": history_rank_list}, ensure_ascii=False)


@leader_board.route("/GetHistoryPoint", methods=["POST", 'GET'])
def get_history_point():
    period = request.form['period']
    username = request.form['username']

    user_id = user_query_id_by_name(username)
    if user_id == -1:
        return json.dumps({"code": "False", 'msg': 'wrong username'}, ensure_ascii=False)

    if period == 'Weekly':
        history_point_list = performance_get_history_point_by_id(user_id)
    else:
        history_point_list = performance_get_history_point_by_id(user_id)

    print(history_point_list)
    return json.dumps({"code": "True", 'msg': '', "history_point_list": history_point_list}, ensure_ascii=False)







# -------------------------------------------------------------------------------------------------
@leader_board.route("/GetRank", methods=["POST", 'GET'])
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

@leader_board.route("/GetRankAndPoint", methods=["POST", 'GET'])
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

@leader_board.route("/GetLeaderBoard", methods=['POST', 'GET'])
def get_leader_board():
    leader_board_list = performance_get_all_rank()

    if leader_board_list != []:
        return json.dumps({"code": "True", 'msg': '', "leader_board_list": leader_board_list}, ensure_ascii=False)
    else:
        return json.dumps({"code": "False", 'msg': 'get leaderboard fail'}, ensure_ascii=False)

@leader_board.route("/GetLeaderBoardAllDaily", methods=['POST', 'GET'])
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

@leader_board.route("/GetLeaderBoardAllWeekly", methods=['POST', 'GET'])
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

@leader_board.route("/GetLeaderBoardAllMonthly", methods=['POST', 'GET'])
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

@leader_board.route("/GetLeaderBoardCountryDaily", methods=['POST', 'GET'])
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

@leader_board.route("/GetLeaderBoardCountryWeekly", methods=['POST', 'GET'])
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


@leader_board.route("/GetLeaderBoardCountryMonthly", methods=['POST', 'GET'])
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



