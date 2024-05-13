#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/27 8:43
# Author    : zhou
# @File     : send_email_base.py
# @Software : PyCharm
#用于建立SMTP连接
import smtplib
#邮件需要专门的MIME格式
from email.mime.text import MIMEText
#plain指普通文本格式邮件内容
msg = MIMEText('啦啦啦','plain','utf-8')
#发件人
msg ['From']='2804164471@qq.com'
#收件人
msg['To']='2804164471@qq.com'
#邮件的标题
msg['Subject']='big胆'

smtp = smtplib.SMTP_SSL('smtp.qq.com')
smtp.login('2804164471@qq.com','uejulmxllwtmdfee')
smtp.sendmail('2804164471@qq.com','2804164471@qq.com',msg.as_string())
smtp.quit()











