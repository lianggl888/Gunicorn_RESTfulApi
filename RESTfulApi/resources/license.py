#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : license.py
# @Author: lianggl
# @Time  : 2020/7/17 16:21

from flask_restful import Resource, request, marshal_with

from RESTfulApi.utils.fields.license import regfile_get_fields

from RESTfulApi.handler.license import get_regfile

class License(Resource):
    @marshal_with(regfile_get_fields)
    def get(self):
        regfile = get_regfile()
        return {
            'code': 20000,
            'data': regfile
        }
