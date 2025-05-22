from ..models import User
from flask import Blueprint
from ..exts import db


bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/update')
def hello():
    user = User.query.get("681f55e8-1a6e-47fa-96c2-52272da46927")
    user.password = "2222222"
    db.session.commit()
    return user.login_name


@bp.route('/query/<string:name>')
def get_user(name):
    user = User.query.filter_by(name=name).filter_by(deleted=False).first()
    if user:
        return f"用户信息：{user.login_name}"
    else:
        return "用户不存在"


@bp.route('/list')
def get_user_list():
    users = User.query.filter_by(deleted=False).all()
    user_list = []
    for user in users:
        user_list.append(user.login_name)
    return f"用户列表：{user_list}"


@bp.route('/add')
def user_add():
    user = User(login_name="老四", name="老子", password="123456", unit_code="001", unit_name="测试单位")
    db.session.add(user)
    db.session.commit()
    return "用户创建成功"


@bp.route('/delete')
def user_delete():
    user = User.query.get("c54fbac3aa604e74aaec8e893a08a990")
    # 逻辑删除
    user.soft_delete()
    return "用户删除成功"