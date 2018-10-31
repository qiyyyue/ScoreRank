# -*- coding: utf-8 -*
import pymysql
import config_default


def user_register(username, password):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    insert_id = -1
    # SQL 插入语句
    sql = "INSERT INTO user_info(user_name, password) VALUES ('%s', '%s')" % (username, password)
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

def user_login(username, password):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    # SQL 查询语句
    sql = "SELECT * FROM user_info WHERE user_name = '%s' AND password = '%s'" % (username, password)
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

def user_query_role(username):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    user_role = -1

    # SQL 查询语句
    sql = "SELECT user_role FROM user_info WHERE user_name = '%s'" % (username)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        result = cursor.fetchone()
        if result != None:
            user_role = result[0]
    except:
        print("Error: unable to fetch data")
        #return False

    # 关闭数据库连接
    db_conn.close()
    return user_role

def user_info_update(username, new_username = None, new_password = None, new_email = None, new_country = None, new_city = None, new_timezone = None, new_class = None):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    # SQL 查询语句
    sql = "UPDATE user_info SET "
    if new_username and new_username != '#':
        sql += "user_name = '%s', "%(new_username)
    if new_password and new_password != '#':
        sql += "password = '%s', " % (new_password)
    if new_email and new_email != '#':
        sql += "email = '%s', " % (new_email)
    if new_country and new_city and new_country != '#' and new_city != '#':
        sql += "location = '%s', " % (new_country + "#" + new_city)
    if new_timezone and new_timezone != '#':
        sql += "timezone = '%s', " % (new_timezone)
    if new_class and new_class != '#':
        sql += "class_id = '%d', " % (new_class)
    sql = sql[:-2]
    sql += " WHERE user_name = '%s'" % (username)
    #print(sql)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        db_conn.commit()
    except Exception as e:
        print(e)
        return False

    # 关闭数据库连接
    db_conn.close()
    return True

def user_change_username(username, new_username):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()
    sql = "UPDATE user_info SET user_name = '%s' WHERE user_name = '%s'" % (new_username, username)

    try:
        cursor.execute(sql)
        db_conn.commit()
    except Exception as e:
        return False

    db_conn.close()
    return True


def user_change_password(user_name, new_password):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()
    sql = "UPDATE user_info SET password = '%s' WHERE user_name = '%s'" % (new_password, user_name)

    try:
        cursor.execute(sql)
        db_conn.commit()
    except Exception as e:
        return False

    db_conn.close()
    return True

def user_query_id_by_name(user_name):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    user_id = -1
    # SQL 查询语句
    sql = "SELECT * FROM user_info WHERE user_name = '%s'" % (user_name)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        result = cursor.fetchone()
        if result:
            user_id = result[0]
    except:
        print("Error: unable to fetch data")

    # 关闭数据库连接
    db_conn.close()
    return user_id

def query_user_name_by_id(user_id):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    user_name = None
    # SQL 查询语句
    sql = "SELECT user_name FROM user_info WHERE user_id = '%d'" % (user_id)
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

def query_userinfo_by_id(user_id):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    user_name = None
    # SQL 查询语句
    sql = "SELECT user_name, continent, country, city FROM user_info WHERE user_id = '%d'" % (user_id)
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

def query_userinfo_by_username(usernmae):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    user_name = None
    # SQL 查询语句
    sql = "SELECT user_name, student_id, birthday, class_id, CI, continent, country, city FROM user_info WHERE user_name = '%s'" % (usernmae)
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

def query_users_by_loc(continent = None, country = None, city = None):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['scorerank_db']['host'], configs['scorerank_db']['user'],
                              configs['scorerank_db']['password'], configs['scorerank_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    sql = ""
    user_id_list = []
    #查询所有用户
    if continent == None or continent == "All" or continent == "all":
        sql = "SELECT user_id from user_info WHERE user_role = 1"
    elif country == None or country == "All" or continent == "all":
        sql = "SELECT user_id from user_info WHERE user_role = 1 and continent = '%s'" % (continent)
    elif city == None or city == "All" or continent == "all":
        sql = "SELECT user_id from user_info WHERE user_role = 1 and continent= '%s' and country = '%s'" % (continent, country)
    else:
        sql = "SELECT user_id from user_info WHERE user_role = 1 and continent = '%s' and country = '%s' and city = '%s'" % (continent, country, city)

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

