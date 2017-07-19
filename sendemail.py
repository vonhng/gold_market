#! /usr/bin/env python
# -*- encoding:utf-8 -*-
# @Filename:sendemail
# @Time : 2017/7/18-21:04
# @Author: Administrator
from gold import dl
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr

# 邮箱的第三方服务
mail_host = 'smtp.qq.com'
mail_user = '615873982@qq.com'
mail_pass = '***'

# '''我们编写了一个函数_format_addr()来格式化一个邮件地址。注意不能简单地传入name <addr@example.com>，
#     因为如果包含中文，需要通过Header对象进行编码。
#     msg['To']接收的是字符串而不是list，如果有多个邮件地址，用,分隔即可。'''
# def _format_addr(s):
#     name, addr = parseaddr(s)
#     return formataddr((Header(name, 'utf-8').encode(), addr))
# msg['From'] = _format_addr('冯乾勇<%s>' %sender)
# msg['To'] = _format_addr('收件人<%s>' %reciver)

sender = "615873982@qq.com" #发送者
reciver = ['13777403889@163.com'] #接受者地址，可以使多人

# ↓三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
msg = MIMEText(str(dl),'plain','utf-8')
msg['From'] = '风飞扬'
msg['To'] = ''.join(reciver)

subject = '黄金交易信息'
msg['subject'] = Header(subject,'utf-8').encode()

try:
    smtpobj = smtplib.SMTP_SSL(mail_host,465)
    smtpobj.set_debuglevel(1)
    #smtpobj.connect()
    smtpobj.login(mail_user,mail_pass)
    smtpobj.sendmail(sender,reciver,msg.as_string())
    smtpobj.quit()
    print('邮件发送成功')
except smtplib.SMTPException as e:
    print("发送失败",e)


