#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/26 16:19
# Author    : zhou
# @File     : case_log.py
# @Software : PyCharm
import json
from config.config import *

def log_case_info(case_name,url,args,exp,r):
    if isinstance(args,dict):
        args = json.dumps(args,ensure_ascii=False)
    logging.info("测试用例:{}".format('test_reg_err'))
    logging.info("url:{}".format(url))
    logging.info("请求参数:{}".format(args))
    logging.info("期望结果:{}".format(exp))
    logging.info("实际结果:{}".format(r))


