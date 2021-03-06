# -*- coding: utf-8 -*
import datetime

import pymysql
import config_default


def app_insert(app_id, app_name):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    # SQL 插入语句
    sql = "INSERT INTO app_info(app_id, app_name, reg_date) VALUES ('%d', '%s', '%s')" % (app_id, app_name, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
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

def app_change_weigh(app_id, weight):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    #print(type(weight))
    # SQL 插入语句
    sql = "Update app_info Set weight = '%d' Where app_id = '%d'" % (weight, app_id)
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

def app_get_weight(app_id):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    weight = -1
    #print(type(weight))
    # SQL 插入语句
    sql = "Select weight From app_info Where app_id = '%d'" % (app_id)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        result = cursor.fetchone()
        weight = result[0]
    except:
        # 发生错误时回滚
        db_conn.rollback()
    db_conn.close()
    return weight