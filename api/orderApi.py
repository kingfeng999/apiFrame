#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time    : 2020-09-11 2:21
# @Author  : qinzhifeng
# @FileName: orderApi.py
# @Software: PyCharm
'''
提交订单 api 封装，主要放接口的请求方法
'''

import config
from tools.logger import GetLog

log = GetLog().get_logger()
# 提交订单的接口
class Order():
    def __init__(self):
        self.url = config.IP + '/mtx/index.php?s=/index/buy/add.html'

    # 提交订单
    def order(self,session):
        data = {
            'goods_id':1,
            'stock':2,
            'buy_type':'goods',
            'address_id':600,
            'payment_id':1,
            'spec':''
        }
        resp_order = session.post(self.url, data=data, headers=config.HEADERS)
        # 提取数据做数据关联 -->生成数据,数据放在公共区域,赋值给 config.py 的 JUMP_URL 字段
        config.JUMP_URL = resp_order.json().get('data').get('jump_url')
        log.info(f'提交订单提取的JUMP_URL的值是：{config.JUMP_URL}')
        return resp_order

