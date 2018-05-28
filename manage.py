from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis

class Config(object):
    """配置文件的加载"""

    DEBUG = True#开启调试模式

    #配置MySQL数据库的链接信息
    SQLALCHEMY_DATABASE_URI = "MysqL://root:mysql@127.0.0.1:3306/information_29"
    #不去追踪数据库的修改，节省开销
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #配置redis数据库:因为redis模块不是flask的扩展信息
    REDIS_HOST = "127.0.0.1"
    REDIS_POST = 6379

app = Flask(__name__)

#获取配置信息
app.config.from_object(Config)

#创建链接MySQL数据库的对象
db = SQLAlchemy(app)

#创建连接到redis数据库的的对象
redis_store = StrictRedis(host=Config.REDIS_HOST,post= Config.REDIS_POST)
@app.route("/")
def index():

    #测试redis数据库
    redis_store.set("name","zl")

    return "index"

if __name__ == '__main__':
    app.run(debug =True)