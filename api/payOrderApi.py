#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time    : 2020-09-11 3:57
# @Author  : qinzhifeng
# @FileName: payOrderApi.py
# @Software: PyCharm
'''
订单支付 api 封装，主要放接口的请求方法
'''

from tools.logger import GetLog
import config

log = GetLog().get_logger()
class PayOrder:
    def __init__(self):
        '''
        这个支付接口是重定向接口，302 的 url 是从提交订单的接口里面获取 jump_url
        '''
        # 消费数据
        self.url = config.JUMP_URL
        log.info(f'支付接口的url是:{self.url}')

    # 支付
    def pay_order(self,session):
        # 对 302 接口进行处理，不让其重定向，需要加 allow_redirects = False，默认是 True
        resp = session.get(self.url, allow_redirects=False)
        resp_pay = session.get(resp.headers['location'])
        return resp_pay