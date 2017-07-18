#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import requests
import time
from bs4 import BeautifulSoup
#start = time.clock()
#----------------------------------
# 黄金数据调用示例代码 － 聚合数据
# 在线接口文档：http://www.juhe.cn/docs/29
#----------------------------------
dl = {} #装遴选的结果
appkey = "***"
url = "http://web.juhe.cn:8080/finance/gold/shgold"
params = dict(key=appkey, v="1")
#def get_json(url,params):
try:
    r = requests.get(url,params=params)
    r.raise_for_status()
    data = r.json()
    #print(data)
except:
    print("Error")
# 遍历输出结果
d = data['result'][0]['Au(T+D)']
# for i in len(dict_data):
# for key,value in d.items():
#     print(key,':',value)
dl['获取时间']=d['time']
dl['类型'] = '黄金T+D'
dl['当前价格'] = d['latestpri']
dl['总手'] = d['totalvol']
print(dl)

#print(data['result'][0]['Au(T+D)'])
#end = time.clock()
#print("程序用时：%.2f秒" %(end-start))
