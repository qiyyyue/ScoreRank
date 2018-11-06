# -*- coding: utf-8 -*
import pymysql
import config_default


def tc_register(username, password):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    insert_id = -1
    # SQL 插入语句
    sql = "INSERT INTO teacher_info(user_name, password) VALUES ('%s', '%s')" % (username, password)
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

def tc_login(username, password):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    # SQL 查询语句
    sql = "SELECT * FROM teacher_info WHERE user_name = '%s' AND password = '%s'" % (username, password)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        if len(results) == 0:
            return False
    except:
        print("Error: unable to fetch data")
        return False

    # 关闭数据库连接
    db_conn.close()
    return True

def tc_change_username(username, new_username):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()
    sql = "UPDATE teacher_info SET user_name = '%s' WHERE user_name = '%s'" % (new_username, username)

    try:
        cursor.execute(sql)
        db_conn.commit()
    except Exception as e:
        return False

    db_conn.close()
    return True


def tc_change_password(user_name, new_password):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()
    sql = "UPDATE teacher_info SET password = '%s' WHERE user_name = '%s'" % (new_password, user_name)

    try:
        cursor.execute(sql)
        db_conn.commit()
    except Exception as e:
        return False

    db_conn.close()
    return True