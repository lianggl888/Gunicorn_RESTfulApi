#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : run.py
# @Author: lianggl
# @Time  : 2020/7/17 14:29

from flask import Flask, g, got_request_exception
# 此项目不需要使用数据库
# from RESTfulApi.models import register_database
import logging
import time
from flask_cors import CORS
import os.path

from RESTfulApi.app import api_bp

def log_exception(sender, exception, **extra):
    sender.logger.error('Got exception during processing: %s', exception)

def create_app(**config):
    '''
    创建并初始化一个Flask App
    :param config:
    :return:
    '''
    app = Flask(__name__)
    got_request_exception.connect(log_exception, app)
    cors = CORS(app, resources={r"/*":{"origins":"*"}})

    register_config(app, config)
    register_logging(app)
    # register_database(app)
    register_routes(app)
    return app

def register_config(app, config):
    if config.get('debug') is True:
        app.debug = True

    #此处为读取数据库的配置
    # from config import default
    # app.config.from_object(default)

def register_logging(app):
    #日志
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    logFileName = time.strftime("%Y-%m-%d", time.localtime()) + '.log'

    my_path = os.path.abspath(os.path.dirname(__file__))

    handler = logging.FileHandler(my_path+"/flaskLog/"+logFileName)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

def register_routes(app):
    app.register_blueprint(api_bp, url_prefix='/api')

if __name__ == '__main__':
    create_app(debug=True).run(host='0.0.0.0',port=9999)
