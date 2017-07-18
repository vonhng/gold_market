#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import requests
from bs4 import BeautifulSoup

#----------------------------------
# 黄金数据调用示例代码 － 聚合数据
# 在线接口文档：http://www.juhe.cn/docs/29
#----------------------------------

appkey = "9fh43dge7dgf3f697g:3:hf;557cf:4f"
url = "http://web.juhe.cn:8080/finance/gold/shgold"
params = dict(key=appkey, v="1")
#def get_json(url,params):
try:
    r = requests.get(url,params=params)
    r.raise_for_status()
    data = r.json()
    print(data)
except:
    print("Error")

print(data['result'][0]['Au(T+D)'])

