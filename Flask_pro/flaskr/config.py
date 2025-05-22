import os

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, "instance", 'data.db')

# app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
SQLALCHEMY_DATABASE_URI = f"sqlite:///{db_path}"

# HOSTNAME = "localhost"
# PORT = 3306
# USERNAME = "root"
# PASSWORD = "root"
# DATABASE = "my_test"

# 连接数据库
# app.config['SQLALCHEMY_DATABASE_URI'] = \
#     f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4'

# 邮箱配置
MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = "cq62yjp@gmail.com"
MAIL_PASSWORD = "xydrrulwffaqpbeb"  # 邮箱的授权码
MAIL_DEFAULT_SENDER = "cq62yjp@gmail.com"