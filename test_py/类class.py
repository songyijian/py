#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

# 类 class
# new 实体|实例 instance


# class Tfn:
#     pass
#     print(1)
# initfn = Tfn()
# initfn.name = 'it'
# print(initfn.name)


# 构造函数 self只是一个
# class Tfn:
#   # 默认执行__init__（构造函数）第一个参数永远是self = this
#   def __init__(self, *args, **json):
#     print(args)
#     print(json)
#     # self = self
#     self.name = args[0]
#     self.age = args[1]
#     self.sex = args[2]
#     # return self

# p = Tfn('song', 18, 'man', a='xxxx')
# print(f'my: {p.name} - {p.age} - {p.sex}')


# class Tfn:
#     def __init__(self, *args, **json):
#         self.__name = args[0]  # 这个属性外面不能访问
#         self.age = args[1]
#         self.sex = args[2]

#     def get_name(self):
#         return f'名字：{self.__name}'


# p = Tfn('song', 18, 'man', a='xxxx')
# # print(f'my: {p.__name} - {p.age} - {p.sex}')
# print(f'my: {p.get_name()} - {p.age} - {p.sex}')


class Item:
    def __init__(self, *args):
        print('Item 的构造函数，初始化就会被调用，首参永远是self = this')
        self.name = args[0]["name"]
        self.__age = args[0]["age"]  # 私有属性

    def getname(self):
        print('Item 的类函数，首参永远是self')
        print(f'我是item的 {self.name} , 现在已经 {self.__age}')


i = Item({"name": '小花', "age": 18})
i.getname()  # 我是item的 小花
print(i.name)  # 小花
print(i.age, i.__age)  # 私有属性不能被访问



