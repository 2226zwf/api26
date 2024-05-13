#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/15 16:28
# Author    : zhou
# @File     : 带参数的get请求-tpshop.py
# @Software : PyCharm
import requests

# 方法一：
# url = "http://192.168.55.55/Home/Goods/search.html?q=%E6%89%8B%E6%9C%BA"

# 方法二：
url = "http://192.168.55.55/Home/Goods/search.html"

pama = {
    "q":"%E6%89%8B%E6%9C%BA"
}

r = requests.get(url,params=pama)
print(r.text)



