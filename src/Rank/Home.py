# -*- coding: utf-8 -*
# api of sub_page home
# user's points and rank.
# get data, para--area(continent, country, city) time(week, month, all)


from flask import request, session, json
from flask import Blueprint, render_template, redirect
from UserInfoDB import *
from ParticipantDB import *
from PerformanceDB import *
from AppInfoDB import *
from DuolingoAPI import *

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

@home.route("GetSelfInfo", methods=['POST', 'GET'])
def get_self_info():
    return None

@home.route("/GetVisitorLeaderBoard", methods=['POST', 'GET'])
def get_visitor_leaderboard():
    continent = request.form.get('continent', None)
    country = request.form.get('country', None)
    city = request.form.get('city', None)

    period = request.form.get('period', None)

    try:
        user_list = query_users_by_loc(continent, country, city)
        rank_list = []
        for user_id in user_list:
            user_info = query_userinfo_by_id(user_id)
            user_name = user_info[0]
            if period == "Daily":
                point = performance_query_daily_by_id(user_id)
                old_point = performance_query_pre_daily_by_id(user_id)
            elif period == "Weekly":
                point = performance_query_weekly_by_id(user_id)
                old_point = performance_query_pre_weekly_by_id(user_id)
            elif period == "Monthly":
                point = performance_query_monthly_by_id(user_id)
                old_point = performance_query_pre_monthly_by_id(user_id)
            else:
                point = performance_query_all_by_id(user_id)
                old_point = performance_query_pre_daily_by_id(user_id)
            rank_list.append({'username': user_name, 'continent': user_info[1], 'country': user_info[2], 'city': user_info[3], 'point': point, 'old_point': old_point})
        rank_list.sort(key=lambda user_info: user_info['old_point'], reverse = True)
        for old_rank in range(len(rank_list)):
            rank_list[old_rank]['old_rank'] = old_rank + 1

        rank_list.sort(key=lambda user_info: user_info['point'], reverse=True)
        for i in range(len(rank_list)):
            rank_list[i]['rank'] = i + 1
            tmp = rank_list[i]['rank'] - rank_list[i]['old_rank']
            if tmp < 0:
                rank_list[i]['status'] = '+' + str(abs(tmp))
            elif tmp > 0:
                rank_list[i]['status'] = '-' + str(abs(tmp))
            else:
                rank_list[i]['status'] = '--'

        # print(rank_list)


        return json.dumps({"code": "True", 'msg': '', "leader_board_list": rank_list}, ensure_ascii=False)
    except:
        return json.dumps({"code": "False", 'msg': 'query fail'}, ensure_ascii=False)

##获取排行榜信息
##continent, country, city, period, username.
##返回{code, msg, leader_board_list, self_info}
##leader_board_list:{username, continent, country, city, point, old_point, old_rank, rank, status}
@home.route("/GetLeaderBoard", methods=['POST', 'GET'])
def get_leaderboard():
    continent = request.form.get('continent', None)
    country = request.form.get('country', None)
    city = request.form.get('city', None)

    username = request.form.get('username', None)
    period = request.form.get('period', None)

    try:
        user_list = query_users_by_loc(continent, country, city)
        rank_list = []
        self_info = {}
        for user_id in user_list:
            user_info = query_userinfo_by_id(user_id)
            user_name = user_info[0]
            if period == "Daily":
                point = performance_query_daily_by_id(user_id)
                old_point = performance_query_pre_daily_by_id(user_id)
            elif period == "Weekly":
                point = performance_query_weekly_by_id(user_id)
                old_point = performance_query_pre_weekly_by_id(user_id)
            elif period == "Monthly":
                point = performance_query_monthly_by_id(user_id)
                old_point = performance_query_pre_monthly_by_id(user_id)
            else:
                point = performance_query_all_by_id(user_id)
                old_point = performance_query_pre_daily_by_id(user_id)
            rank_list.append({'username': user_name, 'continent': user_info[1], 'country': user_info[2], 'city': user_info[3], 'point': point, 'old_point': old_point})
        rank_list.sort(key=lambda user_info: user_info['old_point'], reverse = True)
        for old_rank in range(len(rank_list)):
            rank_list[old_rank]['old_rank'] = old_rank + 1

        rank_list.sort(key=lambda user_info: user_info['point'], reverse=True)
        for i in range(len(rank_list)):
            rank_list[i]['rank'] = i + 1
            tmp = rank_list[i]['rank'] - rank_list[i]['old_rank']
            if tmp < 0:
                rank_list[i]['status'] = '+' + str(abs(tmp))
            elif tmp > 0:
                rank_list[i]['status'] = '-' + str(abs(tmp))
            else:
                rank_list[i]['status'] = '--'
            if rank_list[i]['username'] == username:
                self_info = rank_list[i]

        # print(rank_list)


        return json.dumps({"code": "True", 'msg': '', "leader_board_list": rank_list, 'self_info': self_info}, ensure_ascii=False)
    except:
        return json.dumps({"code": "False", 'msg': 'query fail'}, ensure_ascii=False)


