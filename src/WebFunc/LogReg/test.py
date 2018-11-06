import json

import init_path
from StudentInfoDB import *
from TeacherInfoDB import *

def login(user_name, password):
    if stu_login(user_name, password):
        return json.dumps({"code": "True", "user_role": 1}, ensure_ascii=False)
    elif tc_login(user_name, password):
        return json.dumps({"code": "True", "user_role": 0}, ensure_ascii=False)
    else:
        return json.dumps({"code": "False"}, ensure_ascii=False)


print(login("teacher1", "123456"))