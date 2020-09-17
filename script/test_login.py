#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time    : 2020-09-02 2:34
# @Author  : qinzhifeng
# @FileName: test_login.py
# @Software: PyCharm
'''
登录测试用例
'''
import pytest
import requests
import allure
from api.loginApi import MtxLogin
from tools.analyze_data import analyze_data

class TestLogin():
    # 前置条件
    def setup_class(self):
        self.session = requests.Session()  # 通过 session 对象实例化 session
        # 实例化登录接口的对象
        self.login_obj = MtxLogin()

    # 登录成功测试用例
    def test_login_success(self):
        resp_login = self.login_obj.login_succeaa(self.session)
        assert resp_login.json().get('msg') == "登录成功"

    # 参数化，用 yml 文件去保存我们的测试数据
    # data_list = [{},{},{}]  args == for dict in data_list（返回字典）
    @pytest.mark.parametrize('args', analyze_data('login_data', 'test_login'))
    @allure.title('登录异常，测试数据是：{args}')
    def test_login_error(self,args):
        data = {'accounts': args['accounts'], 'pwd': args['pwd']}
        resp_login = self.login_obj.login(self.session, data=data)
        assert resp_login.json().get('msg') == args['exp']