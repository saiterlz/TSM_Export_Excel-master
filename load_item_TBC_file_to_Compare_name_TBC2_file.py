# -*- coding: utf-8 -*-
# @Time    : 2021/6/15 15:49
# @Author  : Saiterlz from lanzhou
# @Email   : kinekok@163.com
# @File    : load_item_TBC_file_to_Compare_name_TBC2_file.py
# @Software: PyCharm

file_2 = "item_TBC.txt"
file_1 = "nameTBC2.txt"

with open(file_1,mode='r',encoding='utf-8') as f:
    for i in f.readlines():
        # print(str(i))
        i=str(i).split(':')
        with open(file_2 ,mode='r',encoding='utf-8') as h:
            for o in h.readlines():
                o=str(o).rstrip(',').split('=')

                temp=o[1]
                # print(type(temp))
                o[1] = temp.replace('"','')
                o[1]=o[1].strip().replace(',','')
                import re
                o[1]=re.sub('[\s]','',o[1])
                # print(o[1])
                # print(i[0],o[0])
                # print(o)
                if str(i[0]) == str(o[0]):
                    if str(i[1]) != str(o[1]):
                        print(i[1], o[1])
                        print('这两个文件中的ID相同.')
                        s=input('请确认是否继续')
                        break
                    else:
                        continue