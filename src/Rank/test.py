from src.DB.UserInfoDB import *
from src.DB.ParticipantDB import *
from src.DB.PerformanceDB import *
from src.DB.AppInfoDB import *
from src.API.DuolingoAPI import *

leader_board_list = performance_get_all_rank()
print(leader_board_list)