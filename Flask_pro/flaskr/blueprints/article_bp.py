from ..models import User, Article
from flask import Blueprint

from ..exts import db

bp = Blueprint('article', __name__, url_prefix='/article')

@bp.route('/add')
def article_add():
    user = User.query.first()
    if not user:
        print("查询结果", user)
        return "User not found. Cannot add articles.", 404
    article1 = Article(title="标题1", content="内容1", author=user)
    article2 = Article(title="标题2", content="内容2", author=user)
    db.session.add_all([article1, article2]) # 批量添加
    db.session.commit()
    return "发表成功"


