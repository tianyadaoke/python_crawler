# coding: utf-8
# @Time: 2021/9/3 13:39
# @Author: Bing
# @File: 017_json
# @Project: basic
# 无法写入
# fp=open('test.txt','w')
# name_list=['张三','李四','王五']
# fp.write(name_list)
# fp.close()

# fp=open('test.txt','w')
# name_list=['张三','李四','王五']
# import json
# names = json.dumps(name_list)
# print(names)
# fp.write(names)
# fp.close()

# fp = open('test.txt', 'w')
# name_list = ['zs', 'ls', 'ww']
# import json
# json.dump(name_list, fp)
# fp.close()

# fp = open('test.txt', 'r')
# content = fp.read()
# print(content)
# print(type(content))
# import json
# result = json.loads(content)
# print(result)
# print(type(result))

fp = open('test.txt', 'r')
import json
result = json.load(fp)
print(result)