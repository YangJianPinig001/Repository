from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

HOSTNAME = "localhost"
PORT = 3306
USERNAME = "root"
PASSWORD = "root"
DATABASE = "my_test"
# 连接数据库
# app.config['SQLALCHEMY_DATABASE_URI'] = \
#     f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)
# DATABASE = '/path/to/database.db'

# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = sqlite3.connect(DATABASE)
#     return db
#
#
# @app.teardown_appcontext
# def close_connection(exception):
#     db = getattr(g, '_database', None)
#     if db is not None:
#         db.close()


# with app.app_context():
#     with db.engine.connect() as conn:
#         from sqlalchemy import text
#         result = conn.execute(text("SELECT VERSION()"))
#         version = result.fetchone()
#         print(f"Database version: version{version}")


