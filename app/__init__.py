# coding:utf-8
import logging
from logging.handlers import TimedRotatingFileHandler

from flask import Flask

from config.app_cfg import config_dict
from config.response_code import Reponse
from app.utils.resp_tool import ApiTool

def setup_log(config_name):
    """记录日志的配置"""
    # 根据传入配置字符串获取不同配置
    configClass = config_dict[config_name]

    # 设置日志的记录等级
    logging.basicConfig(level=configClass.LOG_LEVEL)  # 调试debug级

    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = TimedRotatingFileHandler(
        filename='logs/log.log',
        when='D',
        interval=1,
        backupCount=7,
        encoding='utf-8'
    )

    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    # DEBUG manage.py  18 123
    formatter = logging.Formatter(
        "%(asctime)s|%(processName)s|%(threadName)s|%(levelname)s|%(filename)s:%(lineno)d|%(funcName)s|%(message)s")

    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)

    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)


def create_app(config_name):
    # 0.记录日志
    setup_log(config_name)

    app = Flask(__name__)

    from flask_compress import Compress
    compress = Compress()
    compress.init_app(app)

    configClass = config_dict[config_name]

    # 将配置类注册到app上 根据不同配置类，赋予了不同模式的app
    app.config.from_object(configClass)

    # # 捕获404异常，页面统一处理
    @app.errorhandler(404)
    def error_handler(err):
        return ApiTool.return_response(Reponse.NOTFOUND)

    @app.errorhandler(500)
    def error_handler(err):
        # 3.渲染模板
        app.logger.error(err)
        return ApiTool.return_response(Reponse.SERVERERR)

    # 注册蓝图
    from app.restApi.bbs_sv import bbs_sv_bp
    app.register_blueprint(bbs_sv_bp)

    return app
