#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/5/6 17:05
# Author    : zhou
# @File     : test_user_login.py
# @Software : PyCharm
from test.case.basecase import Basecase

class test_user_login(Basecase):
    def test_login_success(self):
        """leve1:测试用户登录成功"""
        case_data=self.get_case_data("login_ok")
        self.send_request(case_data)
    def test_login_err1(self):
        #leve2:测试登录失败
        case_data = self.get_case_data("login_err1")
        self.send_request(case_data)
















