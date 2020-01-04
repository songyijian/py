#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

# 模块 module
# pyhon path

# 导入
# import mlist
# print (
#     mlist.var,
#     mlist.func(),
#     mlist.array
# )


# 解构
# from mlist import var, func,array ,Item
# 解构所以属性
# from mlist import *

# print (
#     var,
#     func(),
#     str(array)
# )


# a = Item('导出的类')
# print(
#     # a.name,
#     a.getName()
# )






# 解构重命名
# from mlist import var as v
# print(v)


# 目录下的包引用
# 包(文件夹)下面必须有__init__.py才回被识别
import test.s as s
print("success", s.let)

