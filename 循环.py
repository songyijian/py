# -*- coding: UTF-8 -*-

# while在...期间 | loop环


dicts = {
  'name':'ooo',
  'ags':10,
  'obj':2222
}

items = dicts.items()
i = 0
while i < len(items):
  print(str(items[i]) +" | "+ items[i][0] + ":" + str(items[i][1]))
  i = i+1

print('>对字典完成了一次遍历')