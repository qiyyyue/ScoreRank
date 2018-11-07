# -*- coding: utf-8 -*
# api of sub_page teacher home
# students' points and rank.
# get data, para--area(continent, country, city) time(week, month, all)


from flask import request, session, json
from flask import Blueprint, render_template, redirect
from StudentInfoDB import *
from TeacherInfoDB import *
from ParticipantDB import *
from PerformanceDB import *
from AppInfoDB import *
from DuolingoAPI import *

tc_home_bp = Blueprint('tc_home_bp',__name__)

@tc_home_bp.route("/GetTcLeaderBoard", methods=['POST', 'GET'])
def get_teacher_leaderboard():
    continent = request.form.get('continent', None)
    country = request.form.get('country', None)
    city = request.form.get('city', None)

    period = request.form.get('period', None)

    try:
        user_list = stu_query_stus_by_loc(continent, country, city)
        rank_list = []
        for student_id in user_list:
            user_info = stu_query_info_by_id(student_id)
            user_name = user_info[0]
            if period == "Daily":
                point = performance_query_daily_by_id(student_id)
                old_point = performance_query_pre_daily_by_id(student_id)
            elif period == "Weekly":
                point = performance_query_weekly_by_id(student_id)
                old_point = performance_query_pre_weekly_by_id(student_id)
            elif period == "Monthly":
                point = performance_query_monthly_by_id(student_id)
                old_point = performance_query_pre_monthly_by_id(student_id)
            else:
                point = performance_query_all_by_id(student_id)
                old_point = performance_query_pre_all_by_id(student_id)
            rank_list.append({'username': user_name, 'continent': user_info[1], 'country': user_info[2], 'city': user_info[3], 'point': point, 'old_point': old_point})
        rank_list.sort(key=lambda stu_info: stu_info['old_point'], reverse = True)
        for old_rank in range(len(rank_list)):
            rank_list[old_rank]['old_rank'] = old_rank + 1

        rank_list.sort(key=lambda stu_info: stu_info['point'], reverse=True)
        for i in range(len(rank_list)):
            rank_list[i]['rank'] = i + 1
            tmp = rank_list[i]['rank'] - rank_list[i]['old_rank']
            if tmp < 0:
                rank_list[i]['status'] = '+' + str(abs(tmp))
            elif tmp > 0:
                rank_list[i]['status'] = '-' + str(abs(tmp))
            else:
                rank_list[i]['status'] = '--'

        return json.dumps({"code": "True", 'msg': '', "leader_board_list": rank_list}, ensure_ascii=False)
    except:
        return json.dumps({"code": "False", 'msg': 'query fail'}, ensure_ascii=False)

