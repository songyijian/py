#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

# 文件操作 file


try:
  # 打开
  txt = open('file.txt', mode='r')
  # 读取
  content = txt.read()

  print(content)
  # 关闭
  txt.close()

  
  pass
except () as identifier:
  pass
else:
  pass
