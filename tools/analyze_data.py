#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time    : 2020-09-05 19:21
# @Author  : qinzhifeng
# @FileName: analyze_data.py
# @Software: PyCharm
import yaml
import config
def analyze_data(filename, key):
    '''
    解析 yml 文件，得到一个列表嵌套字典的数据格式
    :param filename: login_data.yml
    :param key: test_login
    :return: 列表嵌套字典的数据格式
    '''
    with open(config.DIR_NAME + '/data/%s.yml' %filename, 'r', encoding='utf-8') as f:
        print(f'工程目录的路径是：{config.DIR_NAME}')
        data_list = list()
        # 读取 yaml 文件
        yaml_data = yaml.load(f, Loader=yaml.FullLoader)
        # print(f'yaml 的值是：{yaml_data}')
        # 获取 key 对应所有的值
        pre_value = yaml_data.get(key)
        li = pre_value.values()
        # print(f'li的值是：{li}')
        # 解析获取值的数据
        # for value in li:
        #     print(value)
        data_list.extend(li)
        return data_list
        # 构造数据 --- 列表套字典，[{},{},{}]

if __name__ == '__main__':
    data_list = analyze_data('login_data', 'test_login')
    print(data_list)