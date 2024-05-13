#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/5/7 8:52
# Author    : zhou
# @File     : test_user_reg.py
# @Software : PyCharm
from test.case.basecase import Basecase
from lib.db1 import *
import json

class test_user_reg(Basecase):
    def test_user_reg_ok(self):
        case_data = self.get_case_data("reg_ok")
        username = json.loads(case_data["args"])["userName"]

        if check_user(username):
            del_user(username)
        self.send_request(case_data)
        self.assertTrue(check_user(username))
        del_user(username)

    def test_reg_err(self):
        case_data = self.get_case_data("reg_err")
        name = json.loads(case_data["args"])["userName"]

        if not check_user(name):
            add_user(name,"123456")

        self.assertTrue(check_user(name))
        self.send_request(case_data)


