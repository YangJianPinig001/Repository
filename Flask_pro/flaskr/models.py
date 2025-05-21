import uuid
from sqlalchemy.dialects.postgresql import UUID

from db import db


class User(db.Model):
    __tablename__ = 'user'
    # id为uuid类型，主键
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    login_name = db.Column(db.String(20), unique=True, nullable=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=True)
    unit_code = db.Column(db.String(20), nullable=False)
    unit_name = db.Column(db.String(20), nullable=False)
    deleted = db.Column(db.Boolean, default=False)

    def soft_delete(self):
        """标记为逻辑删除"""
        self.deleted = True
        db.session.commit()

    def restore(self):
        """恢复逻辑删除的记录"""
        self.deleted = False
        db.session.commit()

    def __repr__(self):
        return f"<User {self.id} {self.login_name} {self.name} {self.unit_code} {self.unit_name} {self.deleted}>"


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    # 定义外键，关联到User表的id字段
    author_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    # backref会在User表中创建一个articles属性，表示该用户的所有文章
    author = db.relationship('User', backref='articles')
    # update_by update_time create_by create_time 四个字段
    update_by = db.Column(db.String(36), nullable=True)
    update_time = db.Column(db.DateTime, nullable=True)
    create_by = db.Column(db.String(36), nullable=True)
    create_time = db.Column(db.DateTime, nullable=True)