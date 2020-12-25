# -*- coding: utf-8 -*-
# @Time    : 2020/12/25 9:10
# @Author  : Saiterlz from lanzhou
# @Email   : kinekok@163.com
# @File    : test_radiobutton2.py
# @Software: PyCharm
import tkinter as tk

master = tk.Tk()

v = tk.IntVar()
v.set(2)

tk.Radiobutton(master, text="One", variable=v, value=1).pack(anchor="w")
tk.Radiobutton(master, text="Two", variable=v, value=2).pack(anchor="w")
tk.Radiobutton(master, text="Three", variable=v, value=3).pack(anchor="w")

master.mainloop()