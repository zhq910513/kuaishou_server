#!/usr/bin/python

import logging

from flask import request
# Flask模块
from pymongo import MongoClient
# 返回信息模块
from pymongo.errors import DuplicateKeyError

from app.utils.resp_tool import ApiTool
from config.response_code import Reponse
from . import bbs_sv_bp

client = MongoClient('mongodb://readWrite:readWrite123456@127.0.0.1:27017/ks')
keys_coll = client['ks']['keys']
phone_coll = client['ks']['phones']
author_list_coll = client['ks']['author_list']
author_profile_coll = client['ks']['author_profile']


def hash_key(keyword):
    try:
        sum_str = 0
        for i in str(keyword):
            sum_str += ord(i)
        return int(sum_str % 20)
    except:
        return 0


# 关键词信息
@bbs_sv_bp.route("/keys", methods=["GET", "PUT"])
def keys_info():
    """ 获取关键词信息 """
    if request.method == "GET":
        try:
            keys = []
            request_data = request.args
            phone_num = int(request_data.get("phone_num"))
            for _info in keys_coll.find({'status': None}):
                hash_num = hash_key(_info["keyword"])
                if hash_num == phone_num:
                    keys.append(_info)
                if len(keys) == 20:
                    break
            return ApiTool.return_response(Reponse.SUCCESS, data=keys)
        except Exception as e:
            logging.exception(e)
            return ApiTool.return_response(Reponse.SERVERERR, data=None)

    """ 修改关键词信息 """
    if request.method == "PUT":
        try:
            request_data = request.json
            keys_coll.update_one({'hash_key': request_data.get('hash_key')}, {'$set': request_data}, upsert=True)
            return ApiTool.return_response(Reponse.SUCCESS)
        except Exception as e:
            logging.exception(e)
            return ApiTool.return_response(Reponse.SERVERERR)


# 手机信息
@bbs_sv_bp.route("/phones", methods=["GET", "PUT"])
def phones_info():
    """ 获取手机账号信息 """
    if request.method == "GET":
        try:
            request_data = request.args
            phone = int(request_data.get("phone", 0))
            phone_info = phone_coll.find_one({'phone': phone})
            try:
                del phone_info['_id']
            except:
                pass
            return ApiTool.return_response(Reponse.SUCCESS, data=phone_info)
        except Exception as e:
            logging.exception(e)
            return ApiTool.return_response(Reponse.SERVERERR, data=None)

    """ 修改手机账号信息 """
    if request.method == "PUT":
        try:
            request_data = request.json
            phone_coll.update_one({'phone': request_data.get('phone')}, {'$set': request_data}, upsert=True)
            return ApiTool.return_response(Reponse.SUCCESS)
        except Exception as e:
            logging.exception(e)
            return ApiTool.return_response(Reponse.SERVERERR)


# 用户列表信息
@bbs_sv_bp.route("/author_list", methods=["POST"])
def author_list_info():
    """ 新增用户列表信息 """
    if request.method == "POST":
        try:
            request_data = request.json
            data_list = request_data.get('data_list')
            if data_list:
                for usr in data_list:
                    try:
                        author_list_coll.update_one({'user_id': usr['user_id']}, {'$set': usr}, upsert=True)
                    except:
                        pass
            return ApiTool.return_response(Reponse.SUCCESS)
        except Exception as error:
            return ApiTool.return_response(error)


# 用户个人信息
@bbs_sv_bp.route("/author_profile", methods=["POST"])
def author_profile_info():
    if request.method == "POST":
        try:
            usr = request.json
            author_profile_coll.insert_one(usr)
            return ApiTool.return_response(Reponse.SUCCESS)
        except DuplicateKeyError:
            return ApiTool.return_response(Reponse.SUCCESS, data='DuplicateKey')
        except Exception as error:
            return ApiTool.return_response(error)
