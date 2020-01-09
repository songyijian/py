#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

# 函数

# 函数关键字 def

# def fn(s):
#   print(s)

# fn('我是一个函数')



# *ags 接收剩下的变量
# def tfn(a,*b):
#   print(a,b)

# tfn(1,2,3,4)


# *ags 接收剩下的变量
# def tfn(a,*b):
#   print(tfn.ags)

# tfn(1,2,3,4)


# ages 函数内部修改传入参数: 简单类型不会被改变 | 


# 简单类型不会被改变
# def tfn(a):
#   a = 100
#   print(a)

# a = 1
# tfn(a)
# print(a)


# 引用类型会修改外部对象
def tfn(a):
  a['x'] = 100 
  print(a)

a = {'x':1}
tfn(a)
print(a)
