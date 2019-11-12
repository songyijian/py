# -*- coding: UTF-8 -*-

#字典 dict

dict = {
  "name":1,
  "f":True,
  "obj":{
    "c":'xxxxxxx',
    "f":3
  }
}
# 获取val
# print(dict["obj"]['c'])
# print(dict.get('obj').get('c')) #js没用这个方法


# 字典-引用类型
# print(dict)
# dic2 = dict
# dic2['f'] = False
# print(dict)
# print(dic2)



# 判断类型 type 
# print(type(dict))  # <type 'dict'>

# 转字符串 str
# print(type(str(dict)))  # <type 'str'>

# 对象长度
# print(len(dict))  # 3



# 删除指定键 del
# del dict['name']  # 删除指定key值  # js delete dict['name']
# print(dict)



# 原型连方法 =============
# 删除字典内所有元素 .clear()
# dict.clear()
# print(dict)


# 浅拷贝 .copy()
# dic2 = dict.copy()
# print(dict)
# dic2["f"] = False
# print(dict)
# print(dic2)


# 用列表做为key生成一个字典 .fromkeys()
# seq = ('name', 'age', 'sex')
# dicts ={}
# dicts = dicts.fromkeys(seq)
# print( str(dicts))


# 获取key，值不在返回default值	radiansdict.get(key, default=None)
# print(dict.get("name",100))
# print(dict.get("x", 100)) #没找到返回 100=默认值


# 字典内是否存在这个 键
# print('name' in dict)


# 返回列表，[(ley,val),()]
# print(dict.items())
# [('obj', {'c': 'xxxxxxx', 'f': 3}), ('name', 1), ('f', True)]


# 返回 keys list
# print(dict.keys())


# 返回 values list
# print(dict.values())


# 删除字典给定键 key ,返回删除的值，key为空返回默认值
# dict.pop("name", 'oooooo')
# print(dict)


# 删除最后一个key-val
# dict.popitem()
# print(dict)

