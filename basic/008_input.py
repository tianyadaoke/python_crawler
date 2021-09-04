# coding: utf-8
# @Time: 2021/9/3 12:46
# @Author: Bing
# @File: 008_input
# @Project: basic
card = input('请输入你的卡号')
print('我的卡号是%s' % card)
if int(card) > 100:
    print('你的卡号大于100')
else:
    print('你的卡号小于100')
