# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 09:06:02 2018

@author: lenovo
"""

import urllib.request as r
city_pinyin=input("请输入城市拼音:")
address='http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
info=r.urlopen(address.format(city_pinyin)).read().decode('utf-8','ignore')
print(info)

import json
data=json.loads(info)

print("欢迎使用全球天气app")
print("1.查看当前城市未来五天天气 2.查看其他城市天气 3.保存")
menu=input("请输入菜单：")
if menu=="1":
    print("1.查看当前城市未来五天天气")
    print("当前城市为:"+city_pinyin)
    print("6月3日的天气为:"+str(data["list"][3]['weather'][0]['description'])+";最高温度为:"+str(data["list"][3]["main"]["temp_max"])+";最低温度为:"+str(data["list"][3]["main"]["temp_min"]))

    print("6月4日的天气为:"+str(data["list"][11]['weather'][0]['description'])+";最高温度为:"+str(data["list"][11]["main"]["temp_max"])+";最低温度为:"+str(data["list"][11]["main"]["temp_min"]))
    
    print("6月5日的天气为:"+str(data["list"][19]['weather'][0]['description'])+";最高温度为:"+str(data["list"][19]["main"]["temp"])+";最低温度为:"+str(data["list"][19]["main"]["temp_min"]))
    
    print("6月6日的天气为:"+str(data["list"][27]['weather'][0]['description'])+";最高温度为:"+str(data["list"][27]["main"]["temp"])+";最低温度为:"+str(data["list"][27]["main"]["temp_min"]))

    print("6月7日的天气为:"+str(data["list"][35]['weather'][0]['description'])+";最高温度为:"+str(data["list"][35]["main"]["temp"])+";最低温度为:"+str(data["list"][35]["main"]["temp_min"]))
    
if menu=="2":
    print("2.查看其他城市天气")
if menu=="3":
    print("3.保存")