# coding: utf-8
# @Time: 2021/9/3 13:05
# @Author: Bing
# @File: 010_list
# @Project: basic
food_list = ['蘑菇', '香菜', '稀饭']
food_list.append('小鸡')
print(food_list)

food_list = ['蘑菇', '香菜', '稀饭']
food_list.insert(1,'小鸡')
print(food_list)

food_list_a = ['蘑菇', '香菜', '稀饭']
food_list_b = ['aaa','bbb']
food_list_a.extend(food_list_b)
print(food_list_a)

print('-------------------')
city_list=['北京','上海','shenzhen','洗按','杭州']
city_list[2]='深圳'
print(city_list)
city=input('输入城市')
if city in city_list:
    print('在')
else:
    print('不在')
