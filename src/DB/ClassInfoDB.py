# -*- coding: utf-8 -*
import datetime

import pymysql
import config_default


def class_insert(class_id, teacher_id, user_id):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    # SQL 插入语句
    sql = "INSERT INTO class_info(class_id, teacher_id, user_id) VALUES ('%d', '%d', '%d')" % (class_id, teacher_id, user_id)
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
