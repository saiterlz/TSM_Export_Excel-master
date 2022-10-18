# -*- coding: utf-8 -*-
# @Time    : 2021/3/2 8:55
# @Author  : Saiterlz from lanzhou
# @Email   : kinekok@163.com
# @File    : txt_file_to_DICT.py
# @Software: PyCharm

import os
import time

id_name_files = "D:\\mystudy\\TSM_Export_Excel-master\\nameB.txt"
star=time.clock()
with open(id_name_files, 'r', encoding='utf-8') as f:
    dic = []
    for line in f.readlines():
        line = line.strip('\n')  # 去掉换行符\n
        b = line.split(':')  # 将每一行以空格为分隔符转换成列表
        dic.append(b)
dic = dict(dic)
end=time.clock()
print('使用时间:',end-star)
print(dic)
print(dic['7192'])
keys='7192'
print(dic[keys])

ItemNames = {}
star=time.clock()
with open(id_name_files, 'r', encoding='utf8') as id_f:
    id_ret = id_f.readlines()
    # print(id_ret)
    for i in id_ret:
        arrStr = i.splitlines()
        # print(arrStr)
        if len(arrStr) > 0:
            for v in arrStr:
                # print(v)
                strI = v.split(":")
                # print(type(strI))
                arrI = strI
                # print(arrI)
                if len(arrI) == 2:
                    ItemNames[arrI[0]] = arrI[1]
        id_ret = id_f.readline()
end=time.clock()
print('使用时间:',end-star)
