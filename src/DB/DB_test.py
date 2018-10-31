# -*- coding: utf-8 -*
import datetime

import init_source_file
from src.DB.UserInfoDB import *
from src.DB.PerformanceDB import *
from flask import request, session, json
from flask import Blueprint, render_template, redirect
# from UserInfoDB import *
# from ParticipantDB import *
# from PerformanceDB import *
# from AppInfoDB import *
# from DuolingoAPI import *
# user_info_update("qiyyyue", new_email="qiyyyue@gmail.com", new_class=1, new_location="UK#ABDN", new_timezone="UK")
# performance_ins(2, 1, 2, 20)
# #print(datetime.datetime.now().strftime('%Y-%m-%d'))

def get_leader_board_All_daily():
    #try:
    user_list = query_users_by_loc()

    re_list = []
    for user_id in user_list:
        user_name = query_user_name_by_id(user_id)
        point = performance_query_weekly_by_id(user_id)
        re_list.append({'username': user_name, 'point': point})
    re_list.sort(key=lambda user_info: user_info['point'],reverse=True)
    for i in range(len(re_list)):
        re_list[i]['rank'] = i + 1
    return re_list

def test_get_point():
    user_id = 4
    point = performance_get_point(user_id)
    rank = performance_get_rank(user_id)
    print(point, rank)

def test_get_history_rank():
    user_id = 4
    print(performance_get_history_rank_by_id(user_id))

def test_get_history_point():
    user_id = 4
    print(performance_get_history_point_by_id(user_id))
# test_get_point()

def test_query_userinfo():
    userinfo = query_userinfo_by_username('jack_new')
    for var in userinfo:
        print(str(var))

def test_query_all_point():
    print(performance_query_all_by_id(4))
    print(performance_query_pre_all_by_id(4))

def test_update_data():
    user_id = 3
    user_list = query_users_by_loc()
    for user_id in user_list:
        performance_update_score_till_now(user_id)

test_update_data()
# test_get_history_point()
# test_get_history_rank()
# test_query_userinfo()
# user_list = query_users_by_loc(country="Scotland")
# re_list = []
# for user_id in user_list:
#     user_name = query_user_name_by_id(user_id)
#     point = performance_query_daily_by_id(user_id)
#     re_list.append({'username': user_name, 'point': point})
# re_list.sort(key=lambda user_info: user_info['point'],reverse=True)
# print(re_list)