from test_models import db, app, Poke, Pie
from flask import jsonify, request, session, render_template
from datetime import datetime
import os
import random
from werkzeug.utils import secure_filename


# 显示用户
@app.route("/findAll", methods=["GET"])
def findAll():

    pokeList = []
    poke = Poke.query.all()
    for i in poke:
        data = {"id": i.id,
                "中文名": i.zh,
                "日文名": i.jp,
                "属性1": i.attribution1,
                "属性2": i.attribution1,
                "特性1": i.feature1,
                "特性2": i.feature2,
                "特性3": i.feature3,
                "HP": i.HP,
                "攻击": i.attack,
                "防御": i.defence,
                "特攻": i.attack2,
                "特防": i.defence2,
                "速度": i.pace,
                }
        print("data：", data)
        pokeList.append(data)

    return jsonify(error_code=0, msg="查询成功", data=pokeList)



# 图表数据
@app.route("/findPie", methods=["GET"])
def findPie():

    pieList = []
    pie = Pie.query.filter(Pie.id==1).first()
    for i in pie:
        data = {
                "HP": i.HP,
                "攻击": i.attack,
                "防御": i.defence,
                "特攻": i.attack2,
                "特防": i.defence2,
                "速度": i.pace,
                }
        print("data：", data)
        pieList.append(data)

    return jsonify(error_code=0, msg="查询成功", data=pieList)


if __name__ == '__main__':
    app.run(port=9090, host='localhost')