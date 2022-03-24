from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:123456@localhost:3306/poke'
# app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://flask_api:lhs123@39.108.105.52:3306/flask_api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
#设置这一项是每次请求结束后都会自动提交数据库中的变动
app.config["SECRET_KEY"] = "jjjskssss"

db = SQLAlchemy(app)   # 实例化的数据库

CORS(app, resources=r'/*')    #解决 flask跨域问题



# # 用户表
# class User(db.Model):
#     __tablename__ = "user"
#     id = db.Column(db.Integer, primary_key=True)    # 主键
#     username = db.Column(db.String(64), nullable=False, unique=True)    # 用户名
#     password = db.Column(db.String(64))    # 密码
#     score = db.Column(db.String(8))    # 分数
#     sex = db.Column(db.String(64))    # 性别
#     age = db.Column(db.String(8))    # 年龄
#     picture = db.Column(db.String(255))



# 宝可梦表
class Poke(db.Model):
    __tablename__ = "poke"
    id = db.Column(db.Integer, primary_key=True)    #
    zh = db.Column(db.String(255))    #
    jp = db.Column(db.String(255))    #
    en = db.Column(db.String(255))    #
    attribution1 = db.Column(db.String(64))    #
    attribution1 = db.Column(db.String(64))    #
    feature1 = db.Column(db.String(64))
    feature2 = db.Column(db.String(64))
    feature3 = db.Column(db.String(64))
    HP = db.Column(db.Integer)
    attack = db.Column(db.Integer)
    defence = db.Column(db.Integer)
    attack2 = db.Column(db.Integer)
    defence2 = db.Column(db.Integer)
    pace = db.Column(db.Integer)
    temper = db.Column(db.String(255))
    event = db.Column(db.String(255))


# 图表
class Pie(db.Model):
    __tablename__ = "pie"
    id = db.Column(db.Integer, primary_key=True)  # 主键
    value = db.Column(db.String(255))
    name = db.Column(db.String(255))


if __name__ == '__main__':
    db.create_all()
    # db.drop_all()
