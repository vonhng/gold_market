#!/usr/bin/python
# -*- coding: utf-8 -*-
import json, urllib
#from urllib import urlencode
 
#----------------------------------
# 黄金数据调用示例代码 － 聚合数据
# 在线接口文档：http://www.juhe.cn/docs/29
#----------------------------------
def main():
    #配置申请的APPKey
    appkey = '9fh43dge7dgf3f697g:3:hf;557cf:4f'
 
    #1.上海黄金交易所
    request1(appkey,"GET")
 
    #2.上海期货交易所
    #request2(appkey,"GET")
 
    #3.银行账户黄金
    #request3(appkey,"GET")

#上海黄金交易所
def request1(appkey, m="GET"):
    url = "http://web.juhe.cn:8080/finance/gold/shgold"
    params = {
        "key" : appkey, #APP Key
        "v" : "1", #JSON格式版本(0或1)默认为0
 
    }
    #params = urlencode(params)
    if m =="GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)
 
    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            #成功请求
            print(res["result"])
        else:
            print("%s:%s" % (res["error_code"],res["reason"]))
    else:
        print("request api error")
