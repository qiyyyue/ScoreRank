import os, sys

base_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(base_dir, 'src/API'))
sys.path.append(os.path.join(base_dir, 'src/DB'))
sys.path.append(os.path.join(base_dir, 'src/DataUpdate'))
sys.path.append(os.path.join(base_dir, 'configure'))
sys.path.append(os.path.join(base_dir, 'src/WebFunc/LogReg'))
sys.path.append(os.path.join(base_dir, 'src/WebFunc/StudentFunc'))
sys.path.append(os.path.join(base_dir, 'src/WebFunc/TeacherFunc'))