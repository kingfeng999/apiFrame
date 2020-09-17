#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time    : 2020-09-11 4:53
# @Author  : qinzhifeng
# @FileName: test_payorder.py
# @Software: PyCharm
'''
订单支付测试用例
'''

import requests
from api.loginApi import MtxLogin
from api.orderApi import Order
from api.payOrderApi import PayOrder

class TestPayOrder:
    # 初始化操作
    def setup_class(self):
        self.session = requests.Session()   # 通过 session 对象实例化 session
        self.payorder_obj = PayOrder()      # 实例化支付接口
        MtxLogin().login_succeaa(self.session)       # 先调用登录成功的接口
        Order().order(self.session)                  # 再调用提交订单的接口---> 为了获取 jump_url

    # 支付
    def test_payorder(self):
        resp_pay = self.payorder_obj.pay_order(self.session)    # 请求支付接口
        # 断言：判断支付成功字样
        assert '支付成功' in resp_pay.text


