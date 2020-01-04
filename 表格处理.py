#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

import openpyxl as xl

# 加载表格文件
wb = xl.load_workbook('cj.xlsx')

# 获取表的页码
sheets = wb.get_sheet_names()

# 获取第一页内容
sheet = wb[sheets[0]]

# 获取某个格
cell = sheet["b3"]
print(cell.value)  # 获取这个值

# 第一页的所以行
# rows = sheet.rows
# print(rows)



# i = 2
# print(
#   "d{}".format(1),
#   sheet[f"d{i}"].value
# )


# 写表格头部信息
sheet["g{}".format(1)].value = '总分'
sheet["h{}".format(1)].value = '平均分'
# 遍历每行
for row_index in range(2, sheet.max_row+1):
    # 取出当前行列的value ,着两种写法一致
    div = sheet["d{}".format(row_index)].value
    eiv = sheet[f"e{row_index}"].value
    fiv = sheet[f"f{row_index}"].value
    # 写人
    sheet["g{}".format(row_index)].value = div + eiv + fiv
    sheet["h{}".format(row_index)].value = (div + eiv + fiv)//3


# 另存一个文件出来
wb.save('cjs.xlsx')
