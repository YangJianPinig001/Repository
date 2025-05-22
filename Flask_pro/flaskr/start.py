import uuid

from db import app, db
from models import User, Article


@app.route('/user/update')
def hello():
    user = User.query.get("681f55e8-1a6e-47fa-96c2-52272da46927")
    user.password = "2222222"
    db.session.commit()
    return user.login_name


@app.route('/user/query/<string:name>')
def get_user(name):
    user = User.query.filter_by(name=name).filter_by(deleted=False).first()
    if user:
        return f"用户信息：{user.login_name}"
    else:
        return "用户不存在"


@app.route('/user/list')
def get_user_list():
    users = User.query.filter_by(deleted=False).all()
    user_list = []
    for user in users:
        user_list.append(user.login_name)
    return f"用户列表：{user_list}"


@app.route('/user/add')
def user_add():
    user = User(login_name="老四", name="老子", password="123456", unit_code="001", unit_name="测试单位")
    db.session.add(user)
    db.session.commit()
    return "用户创建成功"


@app.route('/user/delete')
def user_delete():
    user = User.query.get("c54fbac3aa604e74aaec8e893a08a990")
    # 逻辑删除
    user.soft_delete()
    return "用户删除成功"


@app.route('/article/add')
def article_add():

    user = User.query.get("681f55e8-1a6e-47fa-96c2-52272da46927")
    if not user:
        print("查询结果", user)
        return "User not found. Cannot add articles.", 404
    article1 = Article(title="标题1", content="内容1", author=user)
    article2 = Article(title="标题2", content="内容2", author=user)
    db.session.add_all([article1, article2])
    db.session.commit()
    return "发表成功"


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000, host="0.0.0.0")
