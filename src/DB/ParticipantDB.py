# -*- coding: utf-8 -*
import datetime

import pymysql
import config_default


def participant_clear_by_id(student_id):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    sql = "DELETE FROM participant WHERE student_id = '%d'" % (student_id)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        db_conn.commit()
    except:
        # 发生错误时回滚
        db_conn.rollback()
        return False
    return True


def participant_insert(student_id, app_id, app_user_name, app_user_password, app_user_sl, app_user_sp):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    insert_id = -1
    # SQL 插入语句
    sql = "INSERT INTO participant(student_id, app_id, app_user_name, app_user_password, app_user_sl, app_user_sp) VALUES ('%d', '%d', '%s', '%s', '%d', '%d')" % (student_id, app_id, app_user_name, app_user_password, app_user_sl, app_user_sp)
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
            student_id = line[1]
            app_id = line[2]
            app_user_name = line[3]
            app_user_password = line[4]
            app_user_sl = line[5]
            app_user_sp = line[6]
            re_list.append({"student_id": student_id, "app_id": app_id, "app_user_name": app_user_name, "app_user_password": app_user_password, "app_user_sl": app_user_sl, "app_user_sp": app_user_sp})
    except:
        # 发生错误时回滚
        db_conn.rollback()
    db_conn.close()
    return re_list

def participant_query_duo_info_by_id(student_id):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    re_list = []
    # SQL 插入语句
    sql = "SELECT app_user_name, app_user_password FROM participant WHERE student_id = '%d' AND app_id = '%d'" % (student_id, 1)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        result = cursor.fetchone()
        if result == None:
            return None
        return result
    except:
        # 发生错误时回滚
        db_conn.rollback()
    db_conn.close()
    return None

def participant_query_by_id(student_id):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    re_list = []
    # SQL 插入语句
    sql = "SELECT * FROM participant WHERE student_id = '%d'" % (student_id)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        results = cursor.fetchall()
        for line in results:
            student_id = line[1]
            app_id = line[2]
            app_user_name = line[3]
            app_user_password = line[4]
            app_user_sl = line[5]
            app_user_sp = line[6]
            re_list.append({"student_id": student_id, "app_id": app_id, "app_user_name": app_user_name,
                            "app_user_password": app_user_password, "app_user_sl": app_user_sl,
                            "app_user_sp": app_user_sp})
    except:
        # 发生错误时回滚
        db_conn.rollback()
    db_conn.close()
    return re_list

def participant_query_by_id_app_id(student_id, app_id):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    re_list = []
    # SQL 插入语句
    sql = "SELECT * FROM participant WHERE student_id = '%d', app_id = '%d'" % (student_id, app_id)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        results = cursor.fetchall()
        for line in results:
            student_id = line[1]
            app_id = line[2]
            app_user_name = line[3]
            app_user_password = line[4]
            app_user_sl = line[5]
            app_user_sp = line[6]
            re_list.append({"student_id": student_id, "app_id": app_id, "app_user_name": app_user_name,
                            "app_user_password": app_user_password, "app_user_sl": app_user_sl,
                            "app_user_sp": app_user_sp})
    except:
        # 发生错误时回滚
        db_conn.rollback()
    db_conn.close()
    return re_list