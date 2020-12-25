import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
# root = tk.Tk()
# monty = ttk.LabelFrame(root, text=' Monty Python') # 创建一个容器，其父容器为win
# monty.grid(column=0, row=0, padx=10, pady=10)
# scr = scrolledtext.ScrolledText(monty, width=30, height=5, wrap=tk.WORD)
# scr.grid(column=0, columnspan=3)
# root.mainloop()

root = tk.Tk()
root.grid()
app = ttk.Frame(root)
app.grid()

fram1 = tk.LabelFrame(app, text='1')
txt1 = tk.Text(fram1)
sl1 = Scrollbar(fram1)
sl1['command'] = txt1.yview
# sl1.grid(row=0, column=1,sticky=S + W  )
# txt1.grid(row=0, column=0,sticky=S + W  )
# fram1.grid(row=0, column=0, sticky=S + W )
sl1.grid(row=0, column=1, sticky=S + W + E + N)
txt1.grid(row=0, column=0, sticky=S + W + E + N)
fram1.grid(row=0, column=0, sticky=S + W + E + N)
mainloop()