#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time    : 2020-09-11 2:29
# @Author  : qinzhifeng
# @FileName: test_order.py
# @Software: PyCharm
'''
提交订单测试用例
'''
import allure
import requests
from api.orderApi import Order
from api.loginApi import MtxLogin

class TestOrder:
    # 前置条件，初始化
    def setup_class(self):
        self.session = requests.Session()   # 通过 session 对象实例化 session
        self.order_obj = Order()            # 实例化订单接口的对象
        MtxLogin().login_succeaa(self.session)  # 调用登录成功的接口

    # 提交订单
    @allure.story('提交订单接口的测试')
    @allure.title('提交订单接口的测试用例')
    def test_order(self):
        '''
        依赖于登录：api 级别的，请求级别，完全独立
        :return:
        '''
        resp_order = self.order_obj.order(self.session)
        assert resp_order.json().get('msg') == '提交成功'


