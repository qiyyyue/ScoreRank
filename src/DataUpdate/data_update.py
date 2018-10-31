# -*- coding: utf-8 -*
# api of data_update
# system manager to update data daily
import random

from flask import request, session, json
from flask import Blueprint, render_template, redirect
from UserInfoDB import *
from ParticipantDB import *
from PerformanceDB import *
from AppInfoDB import *
from DuolingoAPI import *

data_update = Blueprint('data_update',__name__)

data_update.route('/UpdateDataDaily', methods=['POST', 'GET'])
def update_data_daily():
    user_list = query_users_by_loc()
    for user_id in user_list:
        if not performance_check_today_point_by_id(user_id):
            continue
        yestoday_point = performance_get_yestoday_point(user_id)
        duo_info = participant_query_duo_info_by_user_id(user_id)
        if duo_info == None:
            tmp_point = random.randint(0, 100)
            new_point = yestoday_point + tmp_point
            performance_insert_daily_point(user_id, 1, new_point, new_point/100 + 1, tmp_point)
            continue
        duo_score = get_duolingo_score(duo_info[0], duo_info[1])
        point = duo_score['points']
        level = int(yestoday_point/100) + 1
        performance_insert_daily_point(user_id, 1, point, level, point - yestoday_point)


data_update.route('/UpdateDataTillNow', methods=['POST', 'GET'])
def update_data_till_now():
    user_list = query_users_by_loc()
    for user_id in user_list:
        performance_update_score_till_now(user_id)
