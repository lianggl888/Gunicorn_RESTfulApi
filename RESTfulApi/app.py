#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : app.py
# @Author: lianggl
# @Time  : 2020/7/17 14:35
from flask import Blueprint
from flask_restful import Api

from RESTfulApi.resources.license import License

errors = {
    'error' : {
        'error occurred'
    }
}

api_bp = Blueprint('api', __name__)
api = Api(api_bp, errors=errors)


api.add_resource(License, '/getRegfile')
