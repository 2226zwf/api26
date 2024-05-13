#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/19 16:04
# Author    : zhou
# @File     : db.py
# @Software : PyCharm
import pymysql
# 获取连接方法
def conn():
    con = pymysql.connect(host='127.0.0.1',
    port=3306,
    user='root',
    password='root',
    db='p2p',
    charset='utf8mb4')#如果查询有中午，需要指定测试集编码
    return con
# 封装数据库查询操作
def query_db(sql):
    con = conn()
    #创建游标
    cursor = con.cursor()
    #利用游标执行sql
    cursor.execute(sql)
    #获取执行结果
    result = cursor.fetchone()
    #关闭游标
    cursor.close()
    #关闭连接
    con.close()

# 封装更改数据库操作
def change_db(sql):
    con = conn()
    cursor = con.cursor()
    try:
        cursor.execute(sql)
        #如果成功 就提交
        con.commit()
    except:
        #如果失败 就回滚
        con.rollback()
    finally:
        cursor.close()
        con.close()

def check_product(num):
    rel = query_db("select * from product where proName = '{}'".format(num))
    #三目运算符
    return True if rel else False

def add_product(num,name,limit,ann):
    change_db("INSERT INTO product(proNum,proName,proLimit,annualized) VALUES ('{}','{}','{}','{}')".format(num,name,limit,ann))

def del_product(num):
    change_db("delete from product where proName='{}'".format(num))

if __name__ == '__main__':
    pass











