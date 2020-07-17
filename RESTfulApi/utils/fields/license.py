#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : license.py
# @Author: lianggl
# @Time  : 2020/7/17 16:26
from flask_restful import fields

regfile_get_fields = {
    'code': fields.Integer,
    'data': fields.String
}
