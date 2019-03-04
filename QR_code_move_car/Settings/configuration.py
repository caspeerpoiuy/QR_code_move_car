import flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config):
    my_config = {
        "dev": Dev_Env,
        "pro": Pro_Env

    }
    this_config = my_config.get(config)
    print(this_config)
    app = Flask(__name__)
    app.config.from_object(this_config)
    db.init_app(app)
    return app


class Config(object):
    SECRET_KEY = 'b2ELCml6Sq4o831hpZWYIN7x5A5W3uSKV8VIpeg5aTnlnYmgZ3X6BDUOPwyJo8ggQXCcO3oNY6xdnrRDuh0TQA=='
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123@127.0.0.1:3306/qr_code_move_car"
    # SQLALCHEMY_DATABASE_URI = "mysql+pymsql://root:123@127.0.0.1:3306/qr_code_move_car"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    print("migrate")
    # send message configuration
    appid = 1400188694  # SDK AppID是1400开头

    # 短信应用SDK AppKey
    appkey = "8b961b4ae58d0381f70777ae77314de2"

    # 需要发送短信的手机号码
    phone_numbers = ["13021990159"]

    # 短信模板ID，需要在短信应用中申请
    template_id = 7839  # NOTE: 这里的模板ID`7839`只是一个示例，真实的模板ID需要在短信控制台中申请
    # templateId 7839 对应的内容是"您的验证码是: {1}"
    # 签名
    sms_sign = "腾讯云"  # NOTE: 这里的签名"腾讯云"只是一个示例，真实的签名需要在短信控制台中申请，另外签名参数使用的是`签名内容`，而不是`签名ID


class Dev_Env(Config):
    debug = True


class Pro_Env(Config):
    pass