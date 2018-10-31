# -*- coding: utf-8 -*
import os, sys
base_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(base_dir, 'src/API'))
sys.path.append(os.path.join(base_dir, 'src/DB'))
sys.path.append(os.path.join(base_dir, 'src/Rank'))
sys.path.append(os.path.join(base_dir, 'src/UserInfo'))
sys.path.append(os.path.join(base_dir, 'src/DataUpdate'))
sys.path.append(os.path.join(base_dir, 'configure'))
from flask import Flask
from flask import render_template
from Analysis import analysis
from user_info import user_info
from Home import home
from Setting import setting
from data_update import data_update
app = Flask(__name__)
app.secret_key='qiyyyue'

app.register_blueprint(user_info,url_prefix='/user_info')
app.register_blueprint(analysis, url_prefix='/analysis')
app.register_blueprint(home, url_prefix='/home')
app.register_blueprint(setting, url_prefix='/setting')
app.register_blueprint(data_update, url_prefix='/data_update')


@app.route('/', methods=['POST', 'GET'])
def root():
    return render_template('index.html')

@app.route('/index', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route("/student_home", methods=['GET', 'POST'])
def jump_student_home():
    return render_template("student_home.html")

@app.route("/student_analysis", methods=['GET', 'POST'])
def jump_student_analysis():
    return render_template("student_analysis.html")

@app.route("/student_user", methods=['GET', 'POST'])
def jump_student_user():
    return render_template("student_user.html")

@app.route("/teacher_home", methods=['GET', 'POST'])
def jump_teacher_home():
    return render_template("teacher_home.html")

@app.route("/teacher_analysis", methods=['GET', 'POST'])
def jump_teacher_analysis():
    return render_template("teacher_analysis.html")

@app.route("/teacher_user", methods=['GET', 'POST'])
def jump_teacher_user():
    return render_template("teacher_user.html")

@app.route("/visitor_home", methods=['GET', 'POST'])
def jump_visitor_home():
    return render_template("visitor_home.html")

if __name__ == '__main__':
    app.run()
