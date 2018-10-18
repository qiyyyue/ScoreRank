import datetime

import pymysql
from configure import config_default


def participant_insert(user_id, app_id, app_user_name, app_user_password, app_user_sl, app_user_sp):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    insert_id = -1
    # SQL 插入语句
    sql = "INSERT INTO participant(user_id, app_id, app_user_name, app_user_password, app_user_sl, app_user_sp) VALUES ('%d', '%d', '%s', '%s', '%d', '%d')" % (user_id, app_id, app_user_name, app_user_password, app_user_sl, app_user_sp)
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

def participant_query_all():
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    re_list = []
    # SQL 插入语句
    sql = "SELECT * FROM participant"
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        results = cursor.fetchall()
        for line in results:
            user_id = line[1]
            app_id = line[2]
            app_user_name = line[3]
            app_user_password = line[4]
            app_user_sl = line[5]
            app_user_sp = line[6]
            re_list.append({"user_id": user_id, "app_id": app_id, "app_user_name": app_user_name, "app_user_password": app_user_password, "app_user_sl": app_user_sl, "app_user_sp": app_user_sp})
    except:
        # 发生错误时回滚
        db_conn.rollback()
    db_conn.close()
    return re_list

def participant_query_by_user_id(user_id):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    re_list = []
    # SQL 插入语句
    sql = "SELECT * FROM participant WHERE user_id = '%d'" % (user_id)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        results = cursor.fetchall()
        for line in results:
            user_id = line[1]
            app_id = line[2]
            app_user_name = line[3]
            app_user_password = line[4]
            app_user_sl = line[5]
            app_user_sp = line[6]
            re_list.append({"user_id": user_id, "app_id": app_id, "app_user_name": app_user_name,
                            "app_user_password": app_user_password, "app_user_sl": app_user_sl,
                            "app_user_sp": app_user_sp})
    except:
        # 发生错误时回滚
        db_conn.rollback()
    db_conn.close()
    return re_list

def participant_query_by_user_id_app_id(user_id, app_id):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    re_list = []
    # SQL 插入语句
    sql = "SELECT * FROM participant WHERE user_id = '%d', app_id = '%d'" % (user_id, app_id)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        results = cursor.fetchall()
        for line in results:
            user_id = line[1]
            app_id = line[2]
            app_user_name = line[3]
            app_user_password = line[4]
            app_user_sl = line[5]
            app_user_sp = line[6]
            re_list.append({"user_id": user_id, "app_id": app_id, "app_user_name": app_user_name,
                            "app_user_password": app_user_password, "app_user_sl": app_user_sl,
                            "app_user_sp": app_user_sp})
    except:
        # 发生错误时回滚
        db_conn.rollback()
    db_conn.close()
    return re_list