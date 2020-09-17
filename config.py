#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time    : 2020-09-02 2:19
# @Author  : qinzhifeng
# @FileName: config.py
# @Software: PyCharm
import os
HEADERS = {'X-Requested-With': 'XMLHttpRequest'}
IP = 'http://192.168.0.13'
# 动态生成绝对路径，可以在工程目录下任意路径执行 pytest 命令 --- 目的：解决 Terminal 用命令行执行文件路径报错的问题
ABS_PATH = os.path.abspath(__file__)
DIR_NAME = os.path.dirname(ABS_PATH)
JUMP_URL = None