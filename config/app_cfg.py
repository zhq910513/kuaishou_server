import logging

class Config(object):
    """项目配置信息 (父类配置)"""
    DEBUG = False


class ProductionConfig(Config):
    """生产环境的项目配置"""
    DEBUG = False
    # 线上模式的日志级别：WARNING
    LOG_LEVEL = logging.WARNING


class DevelopmentConfig(Config):
    """测试环境的项目配置"""
    DEBUG = False
    # 线上模式的日志级别：WARNING
    LOG_LEVEL = logging.DEBUG


# 给外界暴露一个使用配置类的接口
config_dict = {
    "production": ProductionConfig,
    # "development": DevelopmentConfig
}
