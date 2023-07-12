# coding:utf-8
from flask import jsonify


class ApiTool(object):
    @staticmethod
    def parameters_intact_verify(*args):
        """参数完整验证"""
        return all(args)

    @staticmethod
    def return_response(label, data=None):
        """结果"""
        return jsonify({
            'code': label.code,
            'msg': label.msg,
            'data': data if data else []
        })

    # @staticmethod
    # def return_make_response(label, data=None, cookie=None, max_age=constants.ACCESS_EXPIRES):
    #     """结果"""
    #     resp_data = {
    #         'code': label.code,
    #         'msg': label.msg,
    #         'data': data if data else []
    #     }
    #     response = make_response(json.dumps(resp_data))
    #     response.set_cookie("accessToken", cookie, max_age=max_age, httponly=True)
    #     return response

    @staticmethod
    def return_custom_response(code, msg, data=None):
        return jsonify({
            'code': code,
            'msg': msg,
            'data': data if data else []
        })
