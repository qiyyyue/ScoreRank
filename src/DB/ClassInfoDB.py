# -*- coding: utf-8 -*
import datetime

import pymysql
import config_default


def class_insert(course_id, student_id, teacher_id):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    # SQL 插入语句
    sql = "INSERT INTO class_info(course_id, student_id, teacher_id) VALUES ('%d', '%d', '%d')" % (course_id, student_id, teacher_id)
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

def class_query_stu_list_course_id(course_id):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    student_id_list = []

    # SQL 插入语句
    sql = "SELECT student_id From class_info where course_id = '%d'" % (course_id)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        results = cursor.fetchall()
        for line in results:
            #print(line)
            student_id = line[0]
            student_id_list.append(student_id)

    except:
        # 发生错误时回滚
        db_conn.rollback()
    db_conn.close()
    return student_id_list

