from flask import Flask
from flask import render_template
from src.Rank.LeaderBoard import leader_board
from src.UserInfo.user_info import user_info
from src.Rank.Home import home
from src.Rank.Setting import setting
app = Flask(__name__)
app.secret_key='qiyyyue'

app.register_blueprint(user_info,url_prefix='/user_info')
app.register_blueprint(leader_board, url_prefix='/leader_board')
app.register_blueprint(home, url_prefix='/home')
app.register_blueprint(setting, url_prefix='/setting')


@app.route('/', methods=['POST', 'GET'])
def hello_world():
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

@app.route("/visitor_home", methods=['GET', 'POST'])
def jump_visitor_home():
    return render_template("visitor_home.html")

if __name__ == '__main__':
    app.run(debug=True)
