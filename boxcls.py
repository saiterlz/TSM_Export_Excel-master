#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.filedialog import askopenfilename
import hashlib
import time
LOG_LINE_NUM = 0
count1 = 0
count2 = 0

class GUI(Tk):
    def __init__(self,parent=None):
        super().__init__()

        self.r_value = IntVar()
        self.s_value = IntVar()
        self.set_init_window()

    # 设置窗口
    def set_init_window(self):
        self.title("TSM数据处理工具_v1.2")  # 窗口名
        # self.geometry('320x160+10+10')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.geometry('1068x681+10+10')
        # self["bg"] = "pink"                                    #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        # self.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高
        # 标签
        self.lab  = Label(self, text="File_Path")
        self.lab.grid(row=0, column=0)
        self.ent = Entry(self, width=40)
        self.ent.grid(row=0, column=1)
        self.lab = Label(self, text="类型")
        self.lab.grid(row=1, column=0)
        self.lab = Label(self, text="功能")
        self.lab.grid(row=2, column=0)
        self.init_data_label = Label(self, text="待处理数据")
        self.init_data_label.grid(row=3, column=0)
        self.result_data_label = Label(self, text="输出结果")
        self.result_data_label.grid(row=3, column=12)
        self.log_label = Label(self, text="日志")
        self.log_label.grid(row=12, column=0)
        self.log_test_label = Label(self, text="结果")
        self.log_test_label.grid(row=12, column=12)

        # 文本框
        self.init_data_Text = Text(self, width=67, height=20)  # 原始数据录入框
        self.init_data_Text.grid(row=4, column=0, rowspan=10, columnspan=10)
        self.result_data_Text = Text(self, width=70, height=20)  # 处理结果展示
        self.result_data_Text.grid(row=4, column=12, rowspan=10, columnspan=10)
        self.log_data_Text = Text(self, width=67, height=9)  # 日志框
        self.log_data_Text.grid(row=14, column=0, columnspan=10)
        self.log_test_Text = Text(self, width=70, height=9)  # 新增加框
        self.log_test_Text.grid(row=14, column=12, columnspan=10)
        # 按钮
        self.button1 = Button(self, text='Open', command=self.get_file_path)
        self.button1.grid(row=0, column=2)
        self.button2 = Button(self, text='submit', command=self.submit)
        self.button2.grid(row=0, column=3)
        self.str_trans_choice_1_button = Radiobutton(self, text='整体分析', variable=self.r_value, value=1,
                                                     command=self.choice_1_value)
        self.str_trans_choice_1_button.grid(row=1, column=1)
        self.str_trans_choice_2_button = Radiobutton(self, text='会长关注', variable=self.r_value, value=0,
                                                     command=self.choice_2_value)
        self.str_trans_choice_2_button.grid(row=1, column=2 )
        self.str_trans_choice_3_button = Checkbutton(self, text='写入EXCEL', command=self.myEvent1)
        self.str_trans_choice_3_button.grid(row=2,column=1)
        self.str_trans_choice_4_button = Checkbutton(self, text='进行标识', command=self.myEvent2)
        self.str_trans_choice_4_button.grid(row=2,  column=2)
        self.str_trans_to_md5_button = Button(self, text="处理数据", bg="lightblue", width=10,
                                              command=self.start_main)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=1, column=11)

    # 功能函数
    def start_main(self):
        main()
    def str_trans_to_md5(self):
        src = self.init_data_Text.get(1.0, END).strip().replace("\n", "").encode()
        # print("src =",src)
        if src:
            try:
                myMd5 = hashlib.md5()
                myMd5.update(src)
                myMd5_Digest = myMd5.hexdigest()
                # print(myMd5_Digest)
                # 输出到界面
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, myMd5_Digest)
                self.write_log_to_Text("INFO:str_trans_to_md5 success")
            except:
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, "字符串转MD5失败")
        else:
            self.write_log_to_Text("ERROR:str_trans_to_md5 failed")

    # 获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        return current_time

    # 日志动态打印
    def write_log_to_Text(self, logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) + " "  + str(logmsg) + "\n"  # 换行
        if LOG_LINE_NUM <= 7:
            self.log_data_Text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0, 2.0)
            self.log_data_Text.insert(END, logmsg_in)

    def choice_1_value(self):
        global ChoiceSheetName
        print(self.r_value.get())
        ChoiceSheetName=self.r_value.get()
        self.write_log_to_Text(self.r_value.get())

    def choice_2_value(self):
        global ChoiceSheetName
        print(self.r_value.get())
        self.write_log_to_Text(self.r_value.get())

    def get_file_path(self):  #获取文件路径
        self.ent.delete(0, END)  #先清空文件名框内的内容
        self.file_name = askopenfilename(filetypes=[('All Files', 'TradeSkillMaster.lua')])  # 弹出文件复选框，选择文件,可以指定文件类型以过滤
        self.ent.insert(END, self.file_name)  # 显示文件名，用insert方法把文件名添加进去

    def submit(self):  # 点击提交的时候获取button内回调函数的变量值，这里是文件路径
        # src = self.init_data_Text.get(1.0, END).strip().replace("\n", "").encode()
        self.file_path = self.ent.get().strip().replace("\n", "").encode()
        print(self.file_path)# 用组件Entry的get获取输入框内的字符串，其在组件被销毁前就被取到
        self.write_log_to_Text(self.file_path)
        # self.destory()  # 中断循环，即主程序跳出无限循环mainloop()，但是这里是销毁的Frame组件，因为self指的是Frame的派生
        # root.destroy()                  #同样是跳出mainloop(),但是这里销毁的是主窗口Tk(),默认情况下它是所有tkinter 组件的父容器

    def myEvent1(self):
        global count1
        global open_write_to_excel_button
        if count1 % 2 == 0:
            count1 += 1
            self.write_log_to_Text("写入EXCEL被选中")
            open_write_to_excel_button=1
        else:
            count1 += 1
            self.write_log_to_Text("写入EXCEL语文被取消")
            open_write_to_excel_button=0

    def myEvent2(self):
        global count2
        global compare_button
        if count2 % 2 == 0:
            count2 += 1
            compare_button=1
            self.write_log_to_Text("进行标识被选中")
        else:
            count2 += 1
            compare_button=0
            self.write_log_to_Text("进行标识被取消")
