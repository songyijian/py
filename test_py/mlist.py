#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

# 模块 module
# pyhon path




var = '模块var'

array = [1,2,3,4]


def func():
  print('我是： func')


class Item:
  def __init__(self,name):
    # super().__init__()
    self.name = name

  def getName(self):
    return f'Item 的 name {self.name}'
