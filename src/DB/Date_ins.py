# -*- coding: utf-8 -*
import random
import datetime
import pymysql
#import config_default
from configure import config_default


def stu_info_ins(username, pwd, student_name, continent, country, city, stu_number, birthday, CI):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    insert_id = -1
    # SQL 插入语句
    sql = "INSERT INTO student_info(user_name, password, student_name, country, city, continent, student_number, birthday, CI) " \
          "VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', str_to_date('%s','%%Y-%%m-%%d'), '%s')" \
          % (username, pwd, student_name, country, city, continent, stu_number, birthday, CI)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        insert_id = db_conn.insert_id()
        db_conn.commit()
    except:
        # 发生错误时回滚
        db_conn.rollback()
        return -1
    db_conn.close()
    return insert_id

def tc_info_ins(username, pwd, teacher_name, continent, country, city, teacher_number, birthday, CI):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    insert_id = -1
    # SQL 插入语句
    sql = "INSERT INTO teacher_info(user_name, password, teacher_name, country, city, continent, teacher_number, birthday, CI) " \
          "VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', str_to_date('%s','%%Y-%%m-%%d'), '%s')" \
          % (username, pwd, teacher_name, country, city, continent, teacher_number, birthday, CI)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        insert_id = db_conn.insert_id()
        db_conn.commit()
    except:
        # 发生错误时回滚
        db_conn.rollback()
        return -1
    db_conn.close()
    return insert_id

def user_info_ins(username, pwd, name, class_id, continent, country, city, timezone, stu_id, birthday, CI):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    insert_id = -1
    # SQL 插入语句
    sql = "INSERT INTO user_info(user_name, password, class_id, country, city, timezone, name, continent, student_id, birthday, CI) " \
          "VALUES ('%s', '%s', '%d', '%s', '%s', '%s', '%s', '%s', '%s', str_to_date('%s','%%Y-%%m-%%d'), '%s')" \
          % (username, pwd, class_id, country, city, timezone, name, continent, stu_id, birthday, CI)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        insert_id = db_conn.insert_id()
        db_conn.commit()
    except:
        # 发生错误时回滚
        db_conn.rollback()
        return -1
    db_conn.close()
    return insert_id

def per_ins(stu_id, date, point, daily_point):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()
    insert_id = -1
    # SQL 插入语句
    sql = "INSERT INTO performance(student_id, app_id, date_time, current_level, current_point, daily_point) VALUES " \
          "('%d', '%d', str_to_date('%s','%%Y-%%m-%%d'),'%d', '%d', '%d')" % (stu_id, 1, date, point/100 + 1, point, daily_point)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        insert_id = db_conn.insert_id()
        db_conn.commit()
    except:
        # 发生错误时回滚
        db_conn.rollback()
        return -1
    db_conn.close()
    return insert_id

def make_data(stu_id):
    current_point = 0
    current_date = datetime.datetime.now() + datetime.timedelta(days=-30)
    for i in range(31):
        tmp_point = random.randint(0, 100)
        current_point += tmp_point
        per_ins(stu_id, current_date.strftime('%Y-%m-%d'), current_point, tmp_point)
        #print(current_date.strftime('%Y-%m-%d'), current_point)
        current_date += datetime.timedelta(days=1)

def query_per_daily():
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    start_time = datetime.datetime.now()
    re_list = []
    # SQL 插入语句
    sql = "SELECT user_id, SUM(daily_point) FROM performance WHERE date_time >= str_to_date('%s','%%Y-%%m-%%d') GROUP BY user_id" % (start_time.strftime('%Y-%m-%d'))
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        results = cursor.fetchall()
        for line in results:
            #print(line)
            user_id = line[0]
            current_point = int(line[1])
            re_list.append({"user_id": user_id, "current_point": current_point})
    except:
        # 发生错误时回滚
        db_conn.rollback()
    db_conn.close()
    return re_list

def query_per_daily_by_id(user_id):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    start_time = datetime.datetime.now()
    # SQL 插入语句
    sql = "SELECT SUM(daily_point) FROM performance WHERE date_time >= str_to_date('%s','%%Y-%%m-%%d') and user_id = '%d'" % (start_time.strftime('%Y-%m-%d'), user_id)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        results = cursor.fetchall()
        for line in results:
            #print(line)
            daily_point = int(line[0])
            return daily_point
    except:
        # 发生错误时回滚
        db_conn.rollback()
    db_conn.close()
    return 0

def query_users_by_loc(country = None, city = None):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    sql = ""
    user_id_list = []
    #查询所有用户
    if country == None:
        sql = "SELECT user_id from user_info"
    elif city == None:
        sql = "SELECT user_id from user_info WHERE country = '%s'" % (country)
    else:
        sql = "SELECT user_id from user_info WHERE country = '%s' and city = '%s'" % (country, city)

    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        results = cursor.fetchall()
        for line in results:
            #print(line)
            user_id = line[0]
            user_id_list.append(user_id)
    except:
        # 发生错误时回滚
        db_conn.rollback()
    db_conn.close()
    return user_id_list

def performance_query_weekly():
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    start_time = datetime.datetime.now()
    while start_time.weekday() != 0:
        start_time += datetime.timedelta(days=-1)
    re_list = []
    # SQL 插入语句
    sql = "SELECT user_id, SUM(daily_point) FROM performance WHERE date_time >= str_to_date('%s','%%Y-%%m-%%d') GROUP BY user_id" % (start_time.strftime('%Y-%m-%d'))
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        results = cursor.fetchall()
        for line in results:
            #print(line)
            user_id = line[0]
            current_point = int(line[1])
            re_list.append({"user_id": user_id, "current_point": current_point})
    except:
        # 发生错误时回滚
        db_conn.rollback()
    db_conn.close()
    return re_list

def performance_query_weekly_by_id(user_id):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    start_time = datetime.datetime.now()
    while start_time.weekday() != 0:
        start_time += datetime.timedelta(days=-1)
    # SQL 插入语句
    sql = "SELECT SUM(daily_point) FROM performance WHERE date_time >= str_to_date('%s','%%Y-%%m-%%d') and user_id = '%d'" % (start_time.strftime('%Y-%m-%d'), user_id)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        results = cursor.fetchall()
        for line in results:
            #print(line)
            daily_point = int(line[0])
            return daily_point
    except:
        # 发生错误时回滚
        db_conn.rollback()
    db_conn.close()
    return 0

def performance_query_monthly():
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    #start_time = datetime.datetime.now()
    start_time = datetime.date(year=datetime.date.today().year, month=datetime.date.today().month, day=1)
    re_list = []
    # SQL 插入语句
    sql = "SELECT user_id, SUM(daily_point) FROM performance WHERE date_time >= str_to_date('%s','%%Y-%%m-%%d') GROUP BY user_id" % (start_time.strftime('%Y-%m-%d'))
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        results = cursor.fetchall()
        for line in results:
            #print(line)
            user_id = line[0]
            current_point = int(line[1])
            re_list.append({"user_id": user_id, "current_point": current_point})
    except:
        # 发生错误时回滚
        db_conn.rollback()
    db_conn.close()
    return re_list

def performance_query_monthly_by_id(user_id):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    start_time = datetime.date(year=datetime.date.today().year, month=datetime.date.today().month, day=1)
    # SQL 插入语句
    sql = "SELECT SUM(daily_point) FROM performance WHERE date_time >= str_to_date('%s','%%Y-%%m-%%d') and user_id = '%d'" % (start_time.strftime('%Y-%m-%d'), user_id)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        results = cursor.fetchall()
        for line in results:
            #print(line)
            daily_point = int(line[0])
            return daily_point
    except:
        # 发生错误时回滚
        db_conn.rollback()
    db_conn.close()
    return 0

#(username, pwd, student_name, continent, country, city, stu_number, birthday, CI):
#(username, pwd, name, class_id, continent, country, city, timezone, stu_id, birthday, CI):
# name_list = ['Edith', 'Emma', 'Jessie', 'Abby', 'Anne', 'Bella', 'Colin', 'Amy', 'Sarah', 'Kate', 'Ashley', 'Larissa']
# name_list = ['teacher1', 'teacher2']
# i = 1001
# for name in name_list:
#     tc_info_ins(name, '123456', name, 'Europe', 'UK', 'Aberdeen', "tc" + str(i), '1995-10-01',
#                   'The Confucius Institute of the University of Aberdeen')
#     i += 1
# for i in range(1, 13):
#     make_data(i)

# make_data(8)
#print(query_users_by_loc(country='Scotland', city='Edinburgh'))
# for user_id in query_users_by_loc("Scotland", ):
#     print(user_id, performance_query_monthly_by_id(user_id))
# start_time = datetime.datetime.now()
# while start_time.day != 1:
#     print(str(start_time.day), start_time.strftime("%y-%m-%d"))
#     start_time += datetime.timedelta(days=-1)
# print(start_time.day, start_time.strftime("%y-%m-%d"))
# first_day = datetime.date(year=datetime.date.today().year, month=datetime.date.today().month, day=1)
# print(first_day)