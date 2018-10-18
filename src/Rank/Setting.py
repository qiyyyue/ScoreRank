# api of sub_page setting
# user's setting

from flask import request, session, json
from flask import Blueprint, render_template, redirect
from src.DB.UserInfoDB import *
from src.DB.ParticipantDB import *
from src.DB.PerformanceDB import *
from src.DB.AppInfoDB import *
from src.API.DuolingoAPI import *

setting = Blueprint('setting',__name__)