# coding: utf-8
# @Time: 2021/9/3 12:59
# @Author: Bing
# @File: 010_string
# @Project: basic
s = 'chinai'
print(len(s))
print(s.find('i'))
print(s.startswith('c'))
print(s.count('i'))
print(s.replace('i', 'w'))

s1 = '1@2@3@1'
print(s1.split('@'))
s2 = '   1  2   2   '
print(s2.strip())
s3 = 'a'
s4 = 'bbbbbbbb'
print(s3.join(s4))


