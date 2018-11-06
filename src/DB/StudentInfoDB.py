# -*- coding: utf-8 -*
import pymysql
import config_default


def stu_register(username, password):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    insert_id = -1
    # SQL 插入语句
    sql = "INSERT INTO student_info(user_name, password) VALUES ('%s', '%s')" % (username, password)
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

def stu_login(username, password):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    # SQL 查询语句
    sql = "SELECT * FROM student_info WHERE user_name = '%s' AND password = '%s'" % (username, password)
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

def stu_change_username(username, new_username):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()
    sql = "UPDATE student_info SET user_name = '%s' WHERE user_name = '%s'" % (new_username, username)

    try:
        cursor.execute(sql)
        db_conn.commit()
    except Exception as e:
        return False

    db_conn.close()
    return True


def stu_change_password(user_name, new_password):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()
    sql = "UPDATE student_info SET password = '%s' WHERE user_name = '%s'" % (new_password, user_name)

    try:
        cursor.execute(sql)
        db_conn.commit()
    except Exception as e:
        return False

    db_conn.close()
    return True

def stu_query_id_by_name(user_name):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    stu_id = -1
    # SQL 查询语句
    sql = "SELECT * FROM student_info WHERE user_name = '%s'" % (user_name)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        result = cursor.fetchone()
        if result:
            stu_id = result[0]
    except:
        print("Error: unable to fetch data")

    # 关闭数据库连接
    db_conn.close()
    return stu_id

def stu_query_user_name_by_id(student_id):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    user_name = None
    # SQL 查询语句
    sql = "SELECT user_name FROM user_info WHERE student_id = '%d'" % (student_id)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        result = cursor.fetchone()
        if result:
            user_name = result[0]
    except:
        print("Error: unable to fetch data")

    # 关闭数据库连接
    db_conn.close()
    return user_name

def stu_query_info_by_id(stu_id):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    user_name = None
    # SQL 查询语句
    sql = "SELECT user_name, continent, country, city FROM student_info WHERE student_id = '%d'" % (stu_id)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        result = cursor.fetchone()
        if result:
            user_info = result
    except:
        print("Error: unable to fetch data")
        return None

    # 关闭数据库连接
    db_conn.close()
    return user_info

def stu_query_info_by_username(usernmae):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    # user_name = None
    stu_info = None
    # SQL 查询语句
    sql = "SELECT user_name, student_name, birthday, student_number, CI, continent, country, city FROM student_info WHERE user_name = '%s'" % (usernmae)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        result = cursor.fetchone()
        if result:
            stu_info = result
    except:
        print("Error: unable to fetch data")
        return None

    # 关闭数据库连接
    db_conn.close()
    return stu_info

def stu_query_stus_by_loc(continent = None, country = None, city = None):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    sql = ""
    student_id_list = []
    #查询所有用户
    if continent == None or continent == "All" or continent == "all":
        sql = "SELECT student_id from student_info"
    elif country == None or country == "All" or continent == "all":
        sql = "SELECT student_id from student_info WHERE continent = '%s'" % (continent)
    elif city == None or city == "All" or continent == "all":
        sql = "SELECT student_id from student_info WHERE continent= '%s' and country = '%s'" % (continent, country)
    else:
        sql = "SELECT student_id from student_info WHERE continent = '%s' and country = '%s' and city = '%s'" % (continent, country, city)

    # print(sql)

    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        results = cursor.fetchall()
        # print(results)
        for line in results:
            #print(line)
            student_id = line[0]
            student_id_list.append(student_id)
    except:
        # 发生错误时回滚
        db_conn.rollback()
    db_conn.close()
    return student_id_list