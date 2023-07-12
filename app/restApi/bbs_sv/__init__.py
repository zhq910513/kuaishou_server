#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @author:Acadsoc
# @file:__init__.py.py
# @time:2021/07/30
# @desc:

from flask import Blueprint

bbs_sv_bp = Blueprint('ks_server', __name__, url_prefix='/ks_server')

from .data_view import *