import datetime

import pymysql
from configure import config_default


def performance_insert(user_id, app_id):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    insert_id = -1
    # SQL 插入语句
    sql = "INSERT INTO performance(user_id, app_id) VALUES ('%d', '%d')" % (user_id, app_id)
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

def performance_update(performance_id, current_level, current_point):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    # SQL 插入语句
    sql = "UPDATE performance SET current_level = '%d', current_point = '%d' WHERE performance_id = '%d'" % (current_level, current_point, performance_id)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        db_conn.commit()
    except:
        # 发生错误时回滚
        db_conn.rollback()
        return False
    db_conn.close()
    return True

def performance_ins(user_id, app_id, current_level, current_point):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()
    insert_id = -1
    # SQL 插入语句
    sql = "INSERT INTO performance(user_id, app_id, date_time, current_level, current_point) VALUES ('%d', '%d', str_to_date('%s','%%Y-%%m-%%d'),'%d', '%d')" % (user_id, app_id, datetime.datetime.now().strftime('%Y-%m-%d'), current_level, current_point)
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

def performance_get_rank(user_id):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    rank = -1
    # SQL 插入语句
    sql = "SELECT user_id, max(current_point) as sum_point FROM performance GROUP BY user_id ORDER BY sum_point DESC"
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        results = cursor.fetchall()
        #print(results)
        i = 1
        for line in results:
            if user_id == line[0]:
                rank = i
            i += 1
    except:
        # 发生错误时回滚
        db_conn.rollback()
    db_conn.close()
    return rank

def performance_get_point(user_id):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    point = -1
    # SQL 插入语句
    sql = "SELECT max(current_point) FROM performance WHERE user_id = '%d'" % (user_id)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        result = cursor.fetchone()
        #print(result)
        point = result[0]
    except:
        # 发生错误时回滚
        db_conn.rollback()
    db_conn.close()
    return point

def performance_get_rank_point(user_id):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    rank = -1
    point = -1
    # SQL 插入语句
    sql = "SELECT user_id, max(current_point) as sum_point FROM performance GROUP BY user_id ORDER BY sum_point DESC"
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        results = cursor.fetchall()
        #print(results)
        i = 1
        for line in results:
            if user_id == line[0]:
                rank = i
                point = line[1]
            i += 1
    except:
        # 发生错误时回滚
        db_conn.rollback()
    db_conn.close()
    return rank, point

def performance_get_all_rank():
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    re_list = []
    # SQL 插入语句
    sql = "SELECT * FROM performance ORDER BY current_point DESC"
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        results = cursor.fetchall()
        #print(results)
        i = 1
        for line in results:
            user_id = line[1]
            app_id = line[2]
            current_level = line[4]
            current_point = line[5]
            re_list.append({"user_id": user_id, "app_id": app_id,"current_level": current_level,
                            "current_point": current_point, "rank": i})
            i += 1
    except Exception as e:
        # 发生错误时回滚
        db_conn.rollback()
    db_conn.close()
    return re_list

def performance_query_all():
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    re_list = []
    # SQL 插入语句
    sql = "SELECT * FROM performance"
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        results = cursor.fetchall()
        for line in results:
            user_id = line[1]
            app_id = line[2]
            datetime = line[3]
            current_level = line[4]
            current_point = line[5]
            re_list.append({"user_id": user_id, "app_id": app_id, "datetime": datetime,
                            "current_level": current_level, "current_point": current_point})
    except:
        # 发生错误时回滚
        db_conn.rollback()
    db_conn.close()
    return re_list

def performance_query_daily():
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

def performance_query_daily_by_id(user_id):
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

def performance_get_history_point_by_id(user_id, days = 7):
    start_time = datetime.datetime.now() + datetime.timedelta(days=0 - days)
    # start_time = datetime.date(year=datetime.date.today().year, month=7, day=1)

    re_list = []
    for i in range(0, days):
        tmp_day = start_time + datetime.timedelta(days=i)
        tmp_point = performance_get_current_point_id_day(user_id, tmp_day)
        re_list.append(tmp_point)
    return re_list

def performance_get_current_point_id_day(user_id, day):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    sql = "SELECT current_point FROM performance WHERE date_time = str_to_date('%s','%%Y-%%m-%%d') AND user_id = '%d'" % (day.strftime('%Y-%m-%d'), user_id)
    try:
        cursor.execute(sql)
        result = cursor.fetchone()
        if result == None:
            return 0
        return result[0]
    except Exception as e:
        print(e)
        db_conn.rollback()
    db_conn.close()
    return 0


def performance_get_history_rank_by_id(user_id, days = 7):

    start_time = datetime.datetime.now() + datetime.timedelta(days=0-days)
    # start_time = datetime.date(year=datetime.date.today().year, month=7, day=1)

    re_list = []
    for i in range(0, days):
        tmp_day = start_time + datetime.timedelta(days=i)
        tmp_rank = performance_get_rank_id_day(user_id, tmp_day)
        re_list.append(tmp_rank)
    return re_list

def performance_get_rank_id_day(user_id, day):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    sql = "SELECT * FROM performance WHERE date_time = str_to_date('%s','%%Y-%%m-%%d') ORDER BY current_point" % (day.strftime('%Y-%m-%d'))
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        # print(results)
        tmp_rank = 1
        for line in results:
            if line[1] != user_id:
                tmp_rank += 1
            else:
                return tmp_rank
    except Exception as e:
        print(e)
        db_conn.rollback()
    db_conn.close()
    return 0
