# -*- coding: utf-8 -*
import pymysql
import config_default

def duo_insert(username, password, points, level):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['duolingo_db']['host'], configs['duolingo_db']['user'],
                              configs['duolingo_db']['password'], configs['duolingo_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    # SQL 插入语句
    sql = "INSERT INTO duolingo_score(user_name, password, points, level) VALUES ('%s', '%s', '%d', '%d')" % (username, password, int(points), int(level))
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        db_conn.commit()
    except:
        # 发生错误时回滚
        db_conn.rollback()

    #
    re_duo_id = -1
    # SQL 查询语句
    sql = "SELECT * FROM duolingo_score WHERE user_name = '%s'" % (username)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        re_duo_id  = results[0][0]
    except:
        print("Error: unable to fetch data")
        return -1
    # 关闭数据库连接
    db_conn.close()

    return re_duo_id

def get_rank_by_duo_id(duo_id):
    configs = config_default.configs
    db_conn = pymysql.connect(configs['duolingo_db']['host'], configs['duolingo_db']['user'],
                              configs['duolingo_db']['password'], configs['duolingo_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    re_duo_rank = -1
    # SQL 查询语句
    sql = "SELECT * FROM duolingo_score WHERE duo_id = '%d'" % (duo_id)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        re_duo_rank = results[0][5]
    except:
        print("Error: unable to fetch data")
        return -1
    # 关闭数据库连接
    db_conn.close()

    return re_duo_rank

def get_duo_leader_board():
    configs = config_default.configs
    db_conn = pymysql.connect(configs['duolingo_db']['host'], configs['duolingo_db']['user'],
                              configs['duolingo_db']['password'], configs['duolingo_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    leader_board_list = []
    # SQL 查询语句
    sql = "SELECT * FROM duolingo_score"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for line in results:
            user_name = line[1]
            point = line[3]
            level = line[4]
            rank = line[5]
            leader_board_list.append({"username":user_name, "point":point, "level":level, "rank":rank})
    except:
        print("Error: unable to fetch data")
    finally:
        db_conn.close()
    # 关闭数据库连接

    return leader_board_list

def update_leader_board():
    configs = config_default.configs
    db_conn = pymysql.connect(configs['duolingo_db']['host'], configs['duolingo_db']['user'],
                              configs['duolingo_db']['password'], configs['duolingo_db']['database'])

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db_conn.cursor()

    rank_list = []
    # SQL 查询语句
    sql = "SELECT * FROM duolingo_score"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for line in results:
            rank_list.append((line[0], line[3]))
        rank_list.sort(key = lambda ele: ele[1])

    except:
        print("Error: unable to fetch data")
        return False

    for i in range(len(rank_list)):
        duo_id = rank_list[i][0]
        rank = i

        upd_sql = "UPDATE duolingo_score SET rank = '%d' WHERE duo_id = '%d'" % (rank, duo_id)
        try:
            # 执行SQL语句
            cursor.execute(upd_sql)
            # 提交到数据库执行
            db_conn.commit()
        except:
            # 发生错误时回滚
            db_conn.rollback()
            return False

    # 关闭数据库连接
    db_conn.close()
    return True





