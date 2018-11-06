import json

import init_path
from StudentInfoDB import *
from PerformanceDB import *

def get_his_rank(username, period):
    stu_id = stu_query_id_by_name(username)
    if stu_id == -1:
        return json.dumps({"code": "False", 'msg': 'wrong username'}, ensure_ascii=False)

    print(stu_id)
    if period == 'Weekly':
        history_rank_list = performance_get_history_rank_by_id(stu_id)
    else:
        history_rank_list = performance_get_history_rank_by_id(stu_id)

    # print(history_rank_list)
    return json.dumps({"code": "True", 'msg': '', "history_rank_list": history_rank_list}, ensure_ascii=False)

def get_his_point(username, period):
    user_id = stu_query_id_by_name(username)
    if user_id == -1:
        return json.dumps({"code": "False", 'msg': 'wrong username'}, ensure_ascii=False)

    if period == 'Weekly':
        history_point_list = performance_get_history_point_by_id(user_id)
    else:
        history_point_list = performance_get_history_point_by_id(user_id)

    print(history_point_list)
    return json.dumps({"code": "True", 'msg': '', "history_point_list": history_point_list}, ensure_ascii=False)

def get_his_avg_point(username, period):

    stu_info = stu_query_info_by_username(username)
    # print(stu_info)
    avg_his_point_list = [0 for i in range(7)]
    try:
        stu_list = stu_query_stus_by_loc(stu_info[5], stu_info[6], stu_info[7])
        # print(stu_list)
        count = 0
        for stu_id in stu_list:
            tmp_his_point_list = performance_get_history_point_by_id(stu_id)
            for i in range(len(avg_his_point_list)):
                avg_his_point_list[i] += tmp_his_point_list[i]
            count += 1
        if count > 0:
            for i in range(len(avg_his_point_list)):
                avg_his_point_list[i] = int(avg_his_point_list[i] / count)
    except Exception as e:
        print(e)
        return json.dumps({"code": "False", 'msg': ''}, ensure_ascii=False)
        #print(e)

    return json.dumps({"code": "True", 'msg': '', "history_avg_point_list": avg_his_point_list}, ensure_ascii=False)

def get_vis_leaderboard(continent, country, city, period):
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
                old_point = performance_query_pre_daily_by_id(student_id)
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
        for item in rank_list:
            print(item)

        return json.dumps({"code": "True", 'msg': '', "leader_board_list": rank_list}, ensure_ascii=False)
    except:
        return json.dumps({"code": "False", 'msg': 'query fail'}, ensure_ascii=False)

def get_stu_leaderboard(continent, country, city, username, period):
    try:
        user_list = stu_query_stus_by_loc(continent, country, city)
        rank_list = []
        self_info = {}
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
                old_point = performance_query_pre_daily_by_id(student_id)
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

        #print(rank_list)
        for item in rank_list:
            print(item)
        print(self_info)

        return json.dumps({"code": "True", 'msg': '', "leader_board_list": rank_list, 'self_info': self_info}, ensure_ascii=False)
    except:
        return json.dumps({"code": "False", 'msg': 'query fail'}, ensure_ascii=False)

def stu_get_self_info(username):
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

def stu_change_name(username, new_username):
    if stu_change_username(username, new_username):
        return json.dumps({"code": "True"}, ensure_ascii=False)
    else:
        return json.dumps({"code": "False", 'msg': 'change username fail'}, ensure_ascii=False)


def stu_change_pw(username, password):
    if stu_change_password(username, password):
        return json.dumps({"code": "True"}, ensure_ascii=False)
    else:
        return json.dumps({"code": "False", 'msg': 'change password fail'}, ensure_ascii=False)

def link_duo(username, duo_username, duo_password):
    try:
        stu_id = stu_query_id_by_name(username)
        print(stu_id)
        if stu_id == -1:
            return json.dumps({"code": "False", 'msg': 'wrong username'}, ensure_ascii=False)

        duolingo_score = get_duolingo_score(duo_username, duo_password)
        print(duolingo_score)
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
        print(e)
        return json.dumps({"code": "False", 'msg': 'bind wrong'}, ensure_ascii=False)

    return json.dumps({"code": "True"}, ensure_ascii=False)
print(link_duo('Emma', 'qiyyyue', 'Lee.951012'))
