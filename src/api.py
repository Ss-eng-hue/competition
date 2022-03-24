# -*- coding: utf-8 -*-
# @Time    : 3/24/2022 12:02 PM
# @Author  : taltalasuka
# @File    : api.py
# @Software: PyCharm

import pymysql

from matplotlib import pyplot as plt


connection = pymysql.connect(host='localhost',
                             user='root',
                             password='1234',
                             database='民宿客房管理系统',
                             charset='utf8')
cursor = connection.cursor()  # 创建游标

class api:
     # todo 数据统计 报表 客房预订 推荐
    def show_statistic(self):
        pass
    def show_table(self):
        pass
    def show_reserve(self):
        pass
    def show_recommend(self):
        pass