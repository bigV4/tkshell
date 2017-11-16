#!/usr/bi/python
#_*_ coding : utf-8 _*_
#使用python3.x版本

import os, sys
import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

class SessionPropertiesFrame(tk.Tk):
    '''
    TKShell 新建一个会话界面程序
        界面与逻辑分离
    '''
    def __init__(self, master=None,name="!"):
        '''初始化'''
        self.name = name
        self.sessionPATH = {}
        #类的构造方法必须调用其父类的构造方法来进行基本的初始化。
        super().__init__() # 有点相当于tk.Tk()
        self.createWidgets()

    def createWidgets(self):
        self.title('(%s) New session properties' %self.name)
        self.geometry('700x400')
        # 先定义  4个TabStrip1标签页，用来放置
        
        TabStrip1 = ttk.Notebook(self)
        TabStrip1.place(relx=0.010, rely=0.010, relwidth=0.980, relheight=0.980)
 
        TabStrip1__Tab1 = tk.Frame(TabStrip1)
        TabStrip1.add(TabStrip1__Tab1, text='连接')
        TabStrip1__Tab2 = tk.Frame(TabStrip1)
        TabStrip1.add(TabStrip1__Tab2, text='终端')
        TabStrip1__Tab3 = tk.Frame(TabStrip1)
        TabStrip1.add(TabStrip1__Tab3, text='外观')
        TabStrip1__Tab4 = tk.Frame(TabStrip1)
        TabStrip1.add(TabStrip1__Tab4, text='高级')
        TabStrip1__Tab5 = tk.Frame(TabStrip1)
        TabStrip1.add(TabStrip1__Tab5, text='传输')

        TabStrip1_1 = ttk.Notebook(TabStrip1__Tab1)
        TabStrip1_1.place(relx=0.010, rely=0.010, relwidth=0.980, relheight=0.980)
        
        TabStrip1_1__Tab1 = tk.Frame(TabStrip1_1)
        TabStrip1_1.add(TabStrip1_1__Tab1, text='连接')
        TabStrip1_1__Tab2 = tk.Frame(TabStrip1_1)
        TabStrip1_1.add(TabStrip1_1__Tab2, text='连接>用户身份验证')
        TabStrip1_1__Tab3 = tk.Frame(TabStrip1_1)
        TabStrip1_1.add(TabStrip1_1__Tab3, text='连接>SSH')
        TabStrip1_1__Tab4 = tk.Frame(TabStrip1_1)
        TabStrip1_1.add(TabStrip1_1__Tab4, text='连接>TELNET')
        TabStrip1_1__Tab5 = tk.Frame(TabStrip1_1)
        TabStrip1_1.add(TabStrip1_1__Tab5, text='连接>RLOGIN')
        TabStrip1_1__Tab5 = tk.Frame(TabStrip1_1)
        TabStrip1_1.add(TabStrip1_1__Tab5, text='连接>SERIAL')
        TabStrip1_1__Tab6 = tk.Frame(TabStrip1_1)
        TabStrip1_1.add(TabStrip1_1__Tab6, text='连接>代理')
        TabStrip1_1__Tab7 = tk.Frame(TabStrip1_1)
        TabStrip1_1.add(TabStrip1_1__Tab7, text='连接>保持活动状态')
        
        TabStrip1 = ttk.Notebook(self)
        # 先定义常规、重新连接、TCP、登录验证4个Frame，用来放置下面的部件
        nameframe = tk.Label(TabStrip1_1__Tab1, text='连接(Connect):')
        commonframe = tk.Frame(TabStrip1_1__Tab1)
        reconnectframe = tk.Frame(TabStrip1_1__Tab1)
        tcpframe = tk.Frame(TabStrip1_1__Tab1)
        authenticationframe = tk.Frame(TabStrip1_1__Tab2)
        #放置4个Frame
        commonframe.pack(side=tk.TOP)
        reconnectframe.pack(side=tk.TOP)
        tcpframe.pack(side=tk.TOP)
        authenticationframe.pack(side=tk.TOP)

        # 常规commonframe的部件
        # -- 前三个直接用 tk 的 widgets，第四个下拉列表 tk 没有，ttk 才有，比较麻烦
        namelabel = tk.Label(commonframe, text='(Name):')
        nameentry = tk.Entry(commonframe)
        protocollabel = ttk.Label(commonframe, text='(Protocol):')
        protocolcombobox = ttk.Combobox(commonframe)
        hostlabel = tk.Label(commonframe, text='(Host):')
        hostentry = tk.Entry(commonframe)
        portlabel = tk.Label(commonframe, text='(Port):')
        portentry = tk.Entry(commonframe)
        descriptionlabel = tk.Label(commonframe, text='(Description):')
        descriptionentry = tk.Entry(commonframe)
        # -- commonframe的部件放置位置
        namelabel.grid(row=0, column=0)
        nameentry.grid(row=0, column=1)
        protocollabel.grid(row=1, column=0)
        protocolcombobox.grid(row=1, column=1)
        hostlabel.grid(row=2, column=0)
        hostentry.grid(row=2, column=1)
        portlabel.grid(row=3, column=0)
        portentry.grid(row=3, column=1)
        descriptionlabel.grid(row=4, column=0)
        descriptionentry.grid(row=4, column=1)
        
if __name__ == '__main__':
    # 实例化Application
    app = SessionPropertiesFrame()
    
    
    # 主消息循环:
    app.mainloop()
