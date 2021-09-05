# coding: utf-8
# @Time: 2021/9/5 18:11
# @Author: Bing
# @File: 039_jsonpath
# @Project: basic
import jsonpath
import json

obj = json.load(open('039_jsonpath.json', 'r', encoding='utf-8'))
# 获取所有名字
showname_list = jsonpath.jsonpath(obj, '$..showName')
print(showname_list)

actor_list=jsonpath.jsonpath(obj,"$..leadingRole")
print(actor_list)