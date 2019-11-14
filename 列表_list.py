#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

# 列表 list

ls = [1, 2, 3, 4]
la = ['a', 'b', 'c', 'd']

# print(type(ls))  # <type 'list'>

print(ls)
ls2 = ls.copy()
# ls2[0] = 100
print(ls)
print(ls2)
print("2")


# 引用类型
# print(ls)
# ls2 = ls
# ls2[0] = 100
# print(ls)
# print(ls2)


# print(len(ls))
# print(ls[-2])  #这个是js没有的负数索引

# 切片
# print(ls[1:])  # 最后一个参数不写直接切到末尾
# print(ls[1:-1])  # 支持负索引

# 追加
# la.extend(ls) #么有返回值，直接追加到la下
# print(la)
