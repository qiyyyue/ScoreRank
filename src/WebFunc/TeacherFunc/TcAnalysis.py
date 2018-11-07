# -*- coding: utf-8 -*
# api of sub_page teacher analysis


from flask import request, session, json
from flask import Blueprint, render_template, redirect
from StudentInfoDB import *
from TeacherInfoDB import *
from CourseInfoDB import *
from ClassInfoDB import *
from ParticipantDB import *
from PerformanceDB import *
from AppInfoDB import *
from DuolingoAPI import *

tc_analysis_bp = Blueprint('tc_analysis_bp',__name__)







@tc_analysis_bp.route("/GetTcClassLeaderBoard", methods=['POST', 'GET'])
def get_teacher_class_leaderboard():
    period = request.form.get('period', None)

    course_list = course_query_id_list()
    try:
        rank_list = []
        for course_id in course_list:
            stu_list = class_query_stu_list_course_id(course_id)
            teacher_id, course_name = course_query_info_by_id(course_id)
            teacher_name = tc_query_name_by_id(teacher_id)
            tmp_point = 0
            tmp_old_point = 0
            for student_id in stu_list:
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
                tmp_point += point
                tmp_old_point += old_point
            avg_point = (int)(tmp_point / len(stu_list))
            old_avg_point = (int)(tmp_old_point / len(stu_list))
            rank_list.append({'class_name': course_name, 'teacher_name': teacher_name, 'avg_point': avg_point, 'old_avg_point': old_avg_point})
        rank_list.sort(key=lambda class_info: class_info['old_avg_point'], reverse=True)
        for old_rank in range(len(rank_list)):
            rank_list[old_rank]['old_rank'] = old_rank + 1
        rank_list.sort(key=lambda class_info: class_info['avg_point'], reverse=True)
        for i in range(len(rank_list)):
            rank_list[i]['rank'] = i + 1
            tmp = rank_list[i]['rank'] - rank_list[i]['old_rank']
            if tmp < 0:
                rank_list[i]['status'] = '+' + str(abs(tmp))
            elif tmp > 0:
                rank_list[i]['status'] = '-' + str(abs(tmp))
            else:
                rank_list[i]['status'] = '--'
        #print(rank_list)
        return json.dumps({"code": "True", 'msg': '', "leader_board_list": rank_list}, ensure_ascii=False)
    except:
        return json.dumps({"code": "False", 'msg': 'query fail'}, ensure_ascii=False)