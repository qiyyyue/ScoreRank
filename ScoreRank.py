# -*- coding: utf-8 -*
import os, sys
base_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(base_dir, 'src/API'))
sys.path.append(os.path.join(base_dir, 'src/DB'))
sys.path.append(os.path.join(base_dir, 'src/WebFunc/LogReg'))
sys.path.append(os.path.join(base_dir, 'src/WebFunc/StudentFunc'))
sys.path.append(os.path.join(base_dir, 'src/WebFunc/TeacherFunc'))
sys.path.append(os.path.join(base_dir, 'src/DataUpdate'))
sys.path.append(os.path.join(base_dir, 'configure'))
from flask import Flask
from flask import render_template
from LogReg import log_reg_bp
from StuAnalysis import stu_analysis_bp
from StuHome import stu_home_bp
from StuSetting import stu_setting_bp
from TcHome import tc_home_bp
from TcAnalysis import tc_analysis_bp
from TcSetting import tc_setting_bp
from data_update import data_update
app = Flask(__name__)
app.secret_key='qiyyyue'

app.register_blueprint(log_reg_bp, url_prefix='/log_reg')
app.register_blueprint(stu_analysis_bp, url_prefix='/stu_analysis')
app.register_blueprint(stu_home_bp, url_prefix='/stu_home')
app.register_blueprint(stu_setting_bp, url_prefix='/stu_setting')
app.register_blueprint(tc_home_bp, url_prefix='/tc_home')
app.register_blueprint(tc_analysis_bp, url_prefix='/tc_analysis')
app.register_blueprint(tc_setting_bp, url_prefix='/tc_setting')
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
