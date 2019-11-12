# -*- coding: UTF-8 -*-


ls = [1,2,3,4]
la = ['a','b','c','d']

# print(len(ls))
# print(ls[-2])  #这个是js没有的负数索引

# 切片
# print(ls[1:])  # 最后一个参数不写直接切到末尾
# print(ls[1:-1])  # 支持负索引

# 追加
la.extend(ls) #么有返回值，直接追加到la下
print(la)



# 圆组 生命后不能被修改

cla = ('a', 'b', 'c', 'd')

print(cla,cla[1])
