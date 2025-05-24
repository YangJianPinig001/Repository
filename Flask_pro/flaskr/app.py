from flask_migrate import Migrate
from flask import Flask
from . import config
from .exts import db, mail
from .blueprints.auth import bp as auth_bp
from .blueprints.user_bp import bp as user_bp
from .blueprints.article_bp import bp as article_bp
from .blueprints.mail_bp import bp as mail_bp


app = Flask(__name__)
# 自动绑定配置文件
app.config.from_object(config)
# 先创建了db，在绑定app
db.init_app(app)
# 迁移插件
migrate = Migrate(app, db)
# 初始化 Flask-Mail
mail.init_app(app)

# 注册蓝图
app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)
app.register_blueprint(article_bp)
app.register_blueprint(mail_bp)




