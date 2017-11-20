#!/usr/bi/python
#-*-coding:utf-8 -*-
# 使用python3.x版本

import os, sys
import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from tkinter import messagebox

class SessionPropertiesFrame(tk.Toplevel):
    '''
    TKShell 的会话设置界面程序
        界面与逻辑分离
    '''
    def __init__(self, parent, master=None, titlename="!"):
        '''初始化'''
        super().__init__() # 有点相当于tk.Tk()
        self.parent = parent
        self.titlename = titlename
        self.sessionpropertiesinfo = {"Name":"New Connect"
                                      ,"Protocol":"SSH"
                                      ,"Host":"127.0.0.1"
                                      ,"Port":"22"
                                      ,"Description":""
                                      ,"Reconnect":"0"
                                      ,"IntervalSecond":""
                                      ,"LimitMinute":""
                                      ,"TCPOptions":""
                                      ,"Method":""
                                      ,"UserName":"root"
                                      ,"Password":"toor"
                                      ,"UserKey":"None"
                                      ,"Passphrase":""}
        self.Reconnect_var = tk.IntVar()
        self.TCPOptions_var = tk.IntVar()
        self.parent.withdraw()# 隐藏父窗口
        #print("self.TKSehllApplication_obj = %r %s" %(self.TKSehllApplication_obj, id(self.TKSehllApplication_obj)))
        #类的构造方法必须调用其父类的构造方法来进行基本的初始化。
        self.createWidgets()

    def createWidgets(self):
        self.title('(%s) Properties' %self.titlename)
        self.geometry('725x500')
        # -先定义 连接、终端、外观、高级、传输5个TabStrip1标签页，用来放置
        TabStrip1 = ttk.Notebook(self)
        TabStrip1.place(relx=0.005, rely=0.005, relwidth=0.990, relheight=0.920)
        tk.Button(self, text="    确定(OK)   ",command=self.OKOKOK).place(relx=0.700, rely=0.960, anchor="c")
        tk.Button(self, text="取消(Cancel)",command=self.NOTOK).place(relx=0.900, rely=0.960, anchor="c")
        
        # -先定义 连接、终端、外观、高级、传输5个TabStrip1__Tab标签页，用来放置
        TabStrip1__Tab1 = tk.Frame(TabStrip1)
        TabStrip1.add(TabStrip1__Tab1, text='连接(Connect)')
        TabStrip1__Tab2 = tk.Frame(TabStrip1)
        TabStrip1.add(TabStrip1__Tab2, text='终端(Terminal)')
        TabStrip1__Tab3 = tk.Frame(TabStrip1)
        TabStrip1.add(TabStrip1__Tab3, text='外观(Exterior)')
        TabStrip1__Tab4 = tk.Frame(TabStrip1)
        TabStrip1.add(TabStrip1__Tab4, text='高级(Advanced)')
        TabStrip1__Tab5 = tk.Frame(TabStrip1)
        TabStrip1.add(TabStrip1__Tab5, text='传输(Transmission)')
        # --定义 连接、用户身份验证、SSH、TTELNET、RLOGIN、SERIAL、代理、保持活动状态、8个TabStrip1_1标签页，用来放置
        TabStrip1_1 = ttk.Notebook(TabStrip1__Tab1)
        TabStrip1_1.place(relx=0.005, rely=0.005, relwidth=0.990, relheight=0.990)
        TabStrip1_1__Tab1 = tk.Frame(TabStrip1_1)
        TabStrip1_1.add(TabStrip1_1__Tab1, text='连接(Connect)')
        TabStrip1_1__Tab2 = tk.Frame(TabStrip1_1)
        TabStrip1_1.add(TabStrip1_1__Tab2, text='用户身份验证(Authentication)')
        TabStrip1_1__Tab3 = tk.Frame(TabStrip1_1)
        TabStrip1_1.add(TabStrip1_1__Tab3, text='SSH')
        TabStrip1_1__Tab4 = tk.Frame(TabStrip1_1)
        TabStrip1_1.add(TabStrip1_1__Tab4, text='TTELNET')
        TabStrip1_1__Tab5 = tk.Frame(TabStrip1_1)
        TabStrip1_1.add(TabStrip1_1__Tab5, text='RLOGIN')
        TabStrip1_1__Tab5 = tk.Frame(TabStrip1_1)
        TabStrip1_1.add(TabStrip1_1__Tab5, text='SERIAL')
        TabStrip1_1__Tab6 = tk.Frame(TabStrip1_1)
        TabStrip1_1.add(TabStrip1_1__Tab6, text='代理(Proxy)')
        TabStrip1_1__Tab7 = tk.Frame(TabStrip1_1)
        TabStrip1_1.add(TabStrip1_1__Tab7, text='保持活动状态(Keep alive)')
        # --定义  、 、 、 、 、 、 、 、 标签页，用来放置
        
        # 定义Frame，用来放置下面的部件
        
        connectframe = tk.Frame(TabStrip1_1__Tab1)
        authenticationframe = tk.Frame(TabStrip1_1__Tab2)
        #放置 个Frame
        connectframe.pack(side=tk.TOP)
        authenticationframe.pack(side=tk.TOP)

        # --TabStrip1_1__Tab1 连接connectframe的部件
        self.nameentry = tk.Entry(connectframe)
        self.protocolcombobox = ttk.Combobox(connectframe, state='readonly')# 前三个直接用 tk 的 widgets，第四个下拉列表 tk 没有，ttk 才有，比较麻烦
        self.protocolcombobox['values'] = ("TELNET", "RLOGIN", "SSH", "SFTP", "SERIAL")     # 设置协议(Protocol)下拉列表的值
        self.protocolcombobox.current(2)    # 设置下拉列表默认显示的值，0为 methodcombobox['values'] 的下标值
        self.hostentry = tk.Entry(connectframe)
        self.hostentry.focus()     # 当程序运行时,光标默认会出现在该文本框中
        self.portspinbox= tk.Spinbox(connectframe, from_=0, to=65535) #Spinbox是从标准Tkinter 控件Entry中演变而来的，可以用来从一系列的值中选择合适的值。
        self.portspinbox.insert(10, "22")# 默认值
        self.descriptionentry = tk.Entry(connectframe)
        self.reconnectcheckbutton = tk.Checkbutton(connectframe, text='连接异常关闭时自动重新连接(Automatically reconnect when connection is abnormal)',
                                                   command=self.reconnect_echo, variable=self.Reconnect_var)
        self.intervalsecondspinbox= tk.Spinbox(connectframe, from_=0, to=60)
        self.limitminutespinbox= tk.Spinbox(connectframe, from_=0, to=60)
        self.tcpoptionscheckbutton = tk.Checkbutton(connectframe, text='使用Nagle算法(Use Nagle algorithm)'
                                                    ,command=self.tcpoptions_echo, variable=self.TCPOptions_var)
        # -- connectframe的部件放置位置
        tk.Label(connectframe, bg="#CACEEB", text="连接(Connect)\n"+"-"*220).grid(row=0, columnspan=5, sticky="nw")
        tk.Label(connectframe, text="\n>常规(Common)"+"-"*210).grid(rowspan=1, columnspan=5, sticky="nw")
        tk.Label(connectframe, text='名称(Name):').grid(row=3, column=0, sticky="nw")
        self.nameentry.grid(row=3, column=1, sticky="nw")
        tk.Label(connectframe, text='协议(Protocol):').grid(row=4, column=0, sticky="nw")
        self.protocolcombobox.grid(row=4, column=1, sticky="nw")
        tk.Label(connectframe, text='主机(Host):').grid(row=5, column=0, sticky="nw")
        self.hostentry.grid(row=5, column=1, sticky="nw")
        tk.Label(connectframe, text='端口(Port):').grid(row=6, column=0, sticky="nw")
        self.portspinbox.grid(row=6, column=1, sticky="nw")
        tk.Label(connectframe, text='说明(Description):').grid(row=7, column=0, sticky="nw")
        self.descriptionentry.grid(row=7, column=1, sticky="nw")
        tk.Label(connectframe, text="\n>重新连接(Reconnect)"+"-"*203).grid(rowspan=1, columnspan=5, sticky="nw")
        self.reconnectcheckbutton.grid(row=9, column=0, columnspan=3, sticky="nw")
        tk.Label(connectframe, text='间隔/秒(Interval/Second):').grid(row=10, column=0, sticky="nw")
        self.intervalsecondspinbox.grid(row=10, column=1, sticky="nw")
        tk.Label(connectframe, text='限制/分钟(Limit/Minute):').grid(row=11, column=0, sticky="nw")
        self.limitminutespinbox.grid(row=11, column=1, sticky="nw")
        tk.Label(connectframe, text="\n>TCP 选项(TCP option)"+"-"*203).grid(rowspan=1, columnspan=5, sticky="nw")
        self.tcpoptionscheckbutton.grid(row=13, column=0, columnspan=3, sticky="nw")

        # --TabStrip1_1__Tab2 用户身份验证authenticationframe的部件
        self.methodcombobox = ttk.Combobox(authenticationframe, state='readonly')
        self.methodcombobox['values'] = ("Password", "Public Key", "Keyboard Interactive", "GSSAPI")     # 设置下拉列表的值
        self.methodcombobox.current(0)    # 设置下拉列表默认显示的值，0为 methodcombobox['values'] 的下标值
        self.methodsetupbutton = tk.Button(authenticationframe, text="设置(Setting)")
        self.usernameentry = tk.Entry(authenticationframe)
        self.passwordentry = tk.Entry(authenticationframe)
        self.userkeycombobox = ttk.Combobox(authenticationframe)
        self.keybrowsebutton = tk.Button(authenticationframe, text="浏览(Browse)...")
        self.passphreseentry = tk.Entry(authenticationframe)
        # -- connectframe的部件放置位置
        tk.Label(authenticationframe, bg="#CACEEB", text="连接>>用户身份验证  (Connect>>Authentication)\n"+"-"*220).grid(row=0, rowspan=2, columnspan=5, sticky="nw")
        tk.Label(authenticationframe, text="请选择身份验证方法和其他参数。Please select an authentication method and other parameters.").grid(row=2, columnspan=5, sticky="nw")
        tk.Label(authenticationframe, text="会话属性中此部分是为了登陆过程更便捷而提供的。This part of the session properties is provided for the convenience of the login process.").grid(row=3, columnspan=5, sticky="nw")
        tk.Label(authenticationframe, text="如果需要安全性很高状态的话建议您空出此字段。It is recommended that you leave this field empty if you need a high level of security.\n").grid(row=4, columnspan=5, sticky="nw")
        tk.Label(authenticationframe, text="方法(Method):").grid(row=6,column=0, sticky="nw")
        self.methodcombobox.grid(row=6,column=1,columnspan=2, sticky="nw")
        self.methodsetupbutton.grid(row=6,column=3, sticky="nw")
        tk.Label(authenticationframe, text="用户名(User Name):").grid(row=7,column=0, sticky="nw")
        self.usernameentry.grid(row=7,column=1,columnspan=2, sticky="nw")
        tk.Label(authenticationframe, text="密码(Password):").grid(row=8,column=0, sticky="nw")
        self.passwordentry.grid(row=8,column=1,columnspan=2, sticky="nw")
        tk.Label(authenticationframe, text="用户密钥(User key):").grid(row=9,column=0, sticky="nw")
        self.userkeycombobox.grid(row=9,column=1,columnspan=2, sticky="nw")
        self.keybrowsebutton.grid(row=9,column=3,columnspan=2, sticky="nw")
        tk.Label(authenticationframe, text="密码(Passphrase):").grid(row=10,column=0, sticky="nw")
        self.passphreseentry.grid(row=10,column=1, sticky="nw")
        tk.Label(authenticationframe, text="\n注释：公钥和Keyboard Interactive仅在SSH、SFTP协议中可用").grid(row=11, column=0, columnspan=5, sticky="nw")
        tk.Label(authenticationframe, text="Note: Public keys and Keyboard Interactive are only available in the SSH, SFTP protocols").grid(row=13, column=0, columnspan=5, sticky="nw")

    def NOTOK(self):
        self.parent.deiconify()# 显示父窗口
        self.destroy() # 销毁窗口
    def OKOKOK(self):
        self.sessionpropertiesinfo["Name"]= Name = self.nameentry.get()
        self.sessionpropertiesinfo["Protocol"]= Protocol = self.protocolcombobox.get()
        self.sessionpropertiesinfo["Host"]= Host = self.hostentry.get()
        if "0"==self.portspinbox.get()[:1]:
            self.sessionpropertiesinfo["Port"]= Port = self.portspinbox.get()[1:]
        else:
            self.sessionpropertiesinfo["Port"]= Port = self.portspinbox.get()
        self.sessionpropertiesinfo["Description"]= Description = self.descriptionentry.get()
        self.sessionpropertiesinfo["Reconnect"]= Reconnect = self.Reconnect_var.get()
        self.sessionpropertiesinfo["IntervalSecond"]= IntervalSecond = self.intervalsecondspinbox.get()
        self.sessionpropertiesinfo["LimitMinute"]= LimitMinute = self.limitminutespinbox.get()
        self.sessionpropertiesinfo["TCPOptions"]= TCPOptions = self.TCPOptions_var.get()
        self.sessionpropertiesinfo["Method"]= Method = self.methodcombobox.get()
        self.sessionpropertiesinfo["UserName"]= UserName = self.usernameentry.get()
        self.sessionpropertiesinfo["Password"]= Password = self.passwordentry.get()
        self.sessionpropertiesinfo["UserKey"]= UserKey = self.userkeycombobox.get()
        self.sessionpropertiesinfo["Passphrase"]= Passphrase = self.passphreseentry.get()
        print("【sessionpropertiesframe.py调试信息】：self.sessionpropertiesinfo=%s" %self.sessionpropertiesinfo)
        if ""==Name or ""==Host or ""== UserName:
            messagebox.showinfo('Not Yet', '[名称]与[主机]与[用户名]不得为空！ \n\n Host and Name and UserName need to be specified!\n ')  # 弹出消息提示框
        else:
            print("【sessionpropertiesframe.py调试信息】self = %s %r" %(id(self), self))
            self.NOTOK()
            
    def tcpoptions_echo(self):
        print("TCPOptions = %s" %self.TCPOptions_var.get())
        
    def reconnect_echo(self):
        print("Reconnect = %s" %self.Reconnect_var.get())
