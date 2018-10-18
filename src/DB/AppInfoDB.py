import datetime

import pymysql
from configure import config_default


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
