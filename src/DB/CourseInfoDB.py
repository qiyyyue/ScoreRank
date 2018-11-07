# -*- coding: utf-8 -*
import datetime

import pymysql
import config_default


def course_insert(course_id, course_name):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    # SQL 插入语句
    sql = "INSERT INTO course_info(course_id, class_name) VALUES ('%d', '%s')" % (course_id, course_name)
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

def course_query_id_list():
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    course_id_list = []

    # SQL 插入语句
    sql = "SELECT course_id From course_info"
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        results = cursor.fetchall()
        for line in results:
            # print(line)
            course_id = line[0]
            course_id_list.append(course_id)

    except:
        # 发生错误时回滚
        db_conn.rollback()
    db_conn.close()
    return course_id_list

def course_query_info_by_id(course_id):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    teacher_id = None
    course_name = None

    # SQL 插入语句
    sql = "SELECT teacher_id, course_name From course_info Where course_id = '%d'" % (course_id)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        result = cursor.fetchone()
        teacher_id = result[0]
        course_name = result[1]

    except Exception as e:
        print(e)
        # 发生错误时回滚
        db_conn.rollback()
    db_conn.close()
    return teacher_id, course_name

def course_id_list_by_tc_id(teacher_id):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    course_id_list = []

    # SQL 插入语句
    sql = "SELECT course_id From course_info Where teacher_id = '%d'" % (teacher_id)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        results = cursor.fetchall()
        for line in results:
            # print(line)
            course_id = line[0]
            course_id_list.append(course_id)

    except:
        # 发生错误时回滚
        db_conn.rollback()
    db_conn.close()
    return course_id_list