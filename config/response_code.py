# coding:utf-8
from collections import namedtuple

BaseReponse = namedtuple('Reponse', ['code', 'msg'])


class Reponse(object):
    """返回值
    用户类：1000
    通用类：9000
    """
    UNOPEN = BaseReponse('1009', '系统维护，暂不开放!')

    # 用户

    SUCCESS_USER = BaseReponse('0000', u'成功')
    SESSIONERR = BaseReponse('1000', u"用户未登录")
    LOGINERR = BaseReponse('1001', u"用户登录失败")
    PARAMERR_USER = BaseReponse('1002', u"参数错误")
    USERERR = BaseReponse('1003', u"用户不存在或未激活")
    ROLEERR = BaseReponse('1004', u"用户身份错误")
    PWDERR = BaseReponse('1005', u"密码错误")
    PARAM_FORMAT_ERROR_USER = BaseReponse('1006', '参数格式错误')
    PARAM_MISS_USER = BaseReponse('10007', '参数缺失')
    SUCCESS_MSG_captcha = BaseReponse('1008', u"短息发送成功")
    PERMISSOIN_ERROR = BaseReponse('1009', u"权限不足")
    DATAEXIST_USER = BaseReponse('1101', u"用户已存在")
    REQUESTS_METHOD = BaseReponse('1102', u"请求方法有问题")

    # 爬虫任务管理
    TASK_SUCCESS = BaseReponse('2000', u"任务创建成功")
    TASK_ERROR = BaseReponse('2001', u"任务创建失败")
    TASK_SCHEDULER_SUCCEESS = BaseReponse('2002', u"任务调度成功")
    TASK_SCHEDULER_ERROR = BaseReponse('2003', u"任务调度失败")
    TASK_STATUS_ERROR = BaseReponse('2004', u"任务状态修改失败")
    TASK_KEYWORD_ERROR = BaseReponse('2005', u"任务关键字添加失败")
    TASK_ANNLYSIS_ERROR = BaseReponse('2006', u"当前任务分析错误")
    TASK_REMOVE_ERROR = BaseReponse('2007', u"当前任务删除失败")
    TASK_SPIDER_ERROR = BaseReponse('2008', u"当前的调度爬虫服务器异常")
    TASK_SPIDER_NO_RUN = BaseReponse('2009', u"当前调用的爬虫未启动，请前去启动")

    # 数据分析
    ANALYSIS_PERMISSION_ERROR = BaseReponse('3000', u"当前用户没有修改的权限")
    ANALYSIS_ADD_USER_ERROR = BaseReponse('3001', u"添加分析人员失败")

    # 通用
    SUCCESS = BaseReponse('9999', u"成功")
    PARAM_MISS = BaseReponse('9000', '参数缺失')
    UNLAGEL = BaseReponse('9001', '请求不合法')
    FILE_BIG = BaseReponse('9002', '仅支持3M以下文件')
    OVERTIME = BaseReponse('9005', '请求超时')
    IMG_FORMAT = BaseReponse('9003', '图片格式不支持')
    COMMON_ERROR = BaseReponse('9004', '网络异常')
    PARAM_ERROR = BaseReponse('9006', '参数错误')
    PARAM_TIME_ERROR = BaseReponse('9606', '时间参数错误')
    VERIFY_CODE_ERROR = BaseReponse('9007', '验证码错误')
    SMS_TYPE_ERROR = BaseReponse('9008', '短信类型不支持')
    PARAM_FORMAT_ERROR = BaseReponse('9009', '参数格式错误')
    DBERR = BaseReponse('9101', u"数据库错误")
    NODATA = BaseReponse('9102', u"无数据")
    DATAEXIST = BaseReponse('9103', u"数据已存在")
    DATAERR = BaseReponse('9104', u"数据错误")
    IPERR = BaseReponse('9202', u"IP受限")
    THIRDERR = BaseReponse('9301', u"第三方系统错误")
    IOERR = BaseReponse('9302', u"文件读写错误")
    NOTFOUND = BaseReponse('9404', u"请求路径不存在")
    SERVERERR = BaseReponse('9500', u"服务器内部错误")
    UNKOWNERR = BaseReponse('9501', u"未知错误")
    TASK_ERROR_KEYWORD = BaseReponse('9504', u"任务正在进行")
    PARAM_FILE_ERROR = BaseReponse('9505', '上传文件类型错误')
    TIME_LIMIT = BaseReponse('9701', '未达到发布任务间隔时间')
    ES_ERROR = BaseReponse('9804', '未达到发布任务间隔时间')
    TITLEERROR = BaseReponse('9805', '名称重复')
    REPLYERROR = BaseReponse('9805', '24小时内只能回复一次')
    TASKLIMIT = BaseReponse('9805', '请于十五分钟后执行')
    REGISTER = BaseReponse('9806', '已注册')
    MSGERROR = BaseReponse('9807', '发送失败')
    NOTSUPPORT = BaseReponse('9808', '不支持操作')
    NOTDELETE = BaseReponse('9809', '此信息下有对应内容，不能删除')
