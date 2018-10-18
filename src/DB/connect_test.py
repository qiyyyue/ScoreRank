#!/usr/bin/python3
import sys
from configure import config_default

import pymysql

# 打开数据库连接
configs = config_default.configs

print(configs['db']['host'])
print(configs['db']['user'])

# db = pymysql.connect(configs['db']['host'], "root", "123456", "scorerank")
#
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
#
# # SQL 插入语句
# sql = "INSERT INTO user_info(user_name, password, email) VALUES ('%s', '%s', '%s')" % ('qiyyyue', '123456', 'qiyyyue@gmail.com')
# try:
#    # 执行sql语句
#    cursor.execute(sql)
#    # 执行sql语句
#    db.commit()
# except:
#    # 发生错误时回滚
#    db.rollback()
#
# # 关闭数据库连接
# db.close()