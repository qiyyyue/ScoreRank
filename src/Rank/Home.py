# api of sub_page home
# user's points and rank.
# get data, para--area(continent, country, city) time(week, month, all)


from flask import request, session, json
from flask import Blueprint, render_template, redirect
from src.DB.UserInfoDB import *
from src.DB.ParticipantDB import *
from src.DB.PerformanceDB import *
from src.DB.AppInfoDB import *
from src.API.DuolingoAPI import *

home = Blueprint('home',__name__)

@home.route("/GetRank", methods=["POST", 'GET'])
def get_rank():
    username = request.form['username']

    user_id = user_query_id_by_name(username)
    if user_id == -1:
        return json.dumps({"code": "False", 'msg': 'wrong username'}, ensure_ascii=False)

    rank = performance_get_rank(user_id)

    # print("rank   " + str(rank))
    if rank != -1:
        return json.dumps({"code": "True", 'msg': '', "rank": rank}, ensure_ascii=False)
    else:
        return json.dumps({"code": "False", 'msg': 'get rank fail'}, ensure_ascii=False)

@home.route("/GetPoint", methods=["POST", 'GET'])
def get_point():
    username = request.form['username']

    user_id = user_query_id_by_name(username)
    if user_id == -1:
        return json.dumps({"code": "False", 'msg': 'wrong username'}, ensure_ascii=False)

    point = performance_get_point(user_id)
    # print("point   " + str(point))
    if point != -1:
        return json.dumps({"code": "True", 'msg': '', "point": point}, ensure_ascii=False)
    else:
        return json.dumps({"code": "False", 'msg': 'get point fail'}, ensure_ascii=False)

@home.route("/GetRankPoint", methods=["POST",'GET'])
def get_rank_point():
    username = request.form['username']

    user_id = user_query_id_by_name(username)
    if user_id == -1:
        return json.dumps({"code": "False", 'msg': 'wrong username'}, ensure_ascii=False)

    point = performance_get_point(user_id)
    rank = performance_get_rank(user_id)
    if point != -1 and rank != -1:
        return json.dumps({"code": "True", 'msg': '', "point": point, 'rank': rank}, ensure_ascii=False)
    else:
        return json.dumps({"code": "False", 'msg': 'get rank and point fail'}, ensure_ascii=False)

@home.route("/GetLeaderBoard", methods=['POST', 'GET'])
def get_leaderboard():
    continent = request.form['continent']
    country = request.form['country']
    city = request.form['city']

    period = request.form['period']

    try:
        user_list = query_users_by_loc(continent, country, city)
        rank_list = []
        for user_id in user_list:
            user_name = query_user_name_by_id(user_id)
            if period == "Daily":
                point = performance_query_daily_by_id(user_id)
            elif period == "Weekly":
                point = performance_query_weekly_by_id(user_id)
            elif period == "Monthly":
                point = performance_query_monthly_by_id(user_id)
            else:
                point = performance_get_point(user_id)
            rank_list.append({'username': user_name, 'point': point})
            rank_list.sort(key=lambda user_info: user_info['point'], reverse=True)
        for i in range(len(rank_list)):
            rank_list[i]['rank'] = i + 1
        # print(rank_list)
        return json.dumps({"code": "True", 'msg': '', "leader_board_list": rank_list}, ensure_ascii=False)
    except:
        return json.dumps({"code": "False", 'msg': 'query fail'}, ensure_ascii=False)


