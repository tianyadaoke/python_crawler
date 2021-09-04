# coding: utf-8
# @Time: 2021/9/3 13:21
# @Author: Bing
# @File: 014_dict
# @Project: basic
person={'name':'五千','age':15}
print(person['name'])
print(person.get('age'))
person['住址']='杭州'
print(person)
del person['age']
print(person)

for key in person.keys():
    print(key)
for value in person.values():
    print(value)
for  key,value in person.items():
    print(key,value)