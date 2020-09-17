#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time    : 2020-09-02 2:13
# @Author  : qinzhifeng
# @FileName: loginApi.py
# @Software: PyCharm

''' 登录请求 api 封装，主要放接口的请求方法
ip = 'http://192.168.0.13'
    headers = {'X-Requested-With': 'XMLHttpRequest'}
    # 参数化装饰器第一种写法
    @pytest.mark.parametrize('accouts,pwd,exp', data_list, ids=ids)
    def test_login(self, accouts, pwd, exp):
        url_login = self.ip + '/mtx/index.php?s=/index/user/login.html'
'''
from config import IP, HEADERS

class MtxLogin():
    def __init__(self):
        self.url = IP + '/mtx/index.php?s=/index/user/login.html'

    # 封装登录的方法  --- 目的：为了给登录的所有测试场景调用(包括异常场景)
    def login(self, session, data):
        resp_login = session.post(self.url, data=data, headers=HEADERS)
        return resp_login

    # 封装登录成功的方法，使用固定的帐号登录 --- 目的：为了提供给支付和提交订单等接口调用，保证业务正常
    def login_succeaa(self, session):
        '''
        发起登录成功的请求
        :param session:
        :return:
        '''
        data = {'accounts':'yaoyao1','pwd':'yaoyao1'}
        resp_login = session.post(self.url, data=data, headers=HEADERS)
        return resp_login

