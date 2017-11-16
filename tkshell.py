#!/usr/bi/python
#_*_ coding : utf-8 _*_
#使用python3.x版本
import os
import webbrowser
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import sessionpropertiesframe

class TKSehllApplication(tk.Tk):
    '''
    TKShell 主界面程序
        界面与逻辑分离
    '''
    def __init__(self, master=None,name="!"):
        '''初始化'''
        self.name = name
        #类的构造方法必须调用其父类的构造方法来进行基本的初始化。
        super().__init__() # 有点相当于tk.Tk()
        self.createWidgets()

    def createWidgets(self):
        self.title(self.name + 'TKShell (free for everyone)')
        self.geometry('600x400')

        #self.menubar创建菜单栏
        self.menubar = tk.Menu(self)
        #1\Filemenu 创建“filemenu”下拉菜单
        filemenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='文件(File)', menu=filemenu)# 将“filemenu”菜单加到菜单栏“self.menubar”
        filemenu.add_command(label='New\t\tAlt+N', command=self._file_new)
        filemenu.add_command(label='Open\t\tAlt+O', command=self._do_job)
        filemenu.add_separator()#line
        filemenu.add_command(label='Disconnect\t\tAlt+O', command=self._do_job)
        filemenu.add_command(label='Disconnect All\t\tAlt+C', command=self._do_job)
        filemenu.add_command(label='Reconnect', command=self._do_job)
        filemenu.add_command(label='Reconnect All', command=self._do_job)
        filemenu.add_separator()#line
        filemenu.add_command(label='Save As\t\tCtrl+C', command=self._do_job)
        filemenu.add_command(label='Import', command=self._do_job)
        filemenu.add_command(label='Export', command=self._do_job)
        filemenu.add_separator()#line
        filemenu.add_command(label='Print\t\tCtrl+P', command=self._do_job)
        filemenu.add_command(label='Print Preview', command=self._do_job)
        filemenu.add_command(label='Page Settings', command=self._do_job)
        filemenu.add_separator()#line

        #1\Filemenu-->1\1\Trasport
        trasportmenu = tk.Menu(filemenu)
        filemenu.add_cascade(label='Trasport', menu=trasportmenu, underline=0)
        trasportmenu.add_command(label="Trasport AS ASCII", command=self._do_job)
        trasportmenu.add_separator()#line

        #1\Filemenu-->1\1\Trasport-->1\1\1\XMODEM
        XMODEMmenu = tk.Menu(trasportmenu)
        trasportmenu.add_cascade(label='XMODEM', menu=XMODEMmenu, underline=0)
        XMODEMmenu.add_command(label="Use XMODEM Sent", command=self._do_job)
        XMODEMmenu.add_command(label="Use XMODEM Receive", command=self._do_job)

        #1\Filemenu-->1\1\Trasport-->1\1\2\YMODEM
        YMODEMmenu = tk.Menu(trasportmenu)
        trasportmenu.add_cascade(label='YMODEM', menu=YMODEMmenu, underline=0)
        YMODEMmenu.add_command(label="Use YMODEM Sent", command=self._do_job)
        YMODEMmenu.add_command(label="Use YMODEM Receive", command=self._do_job)

        #1\Filemenu-->1\1\Trasport-->1\1\3\ZMODEM
        ZMODEMmenu = tk.Menu(trasportmenu)
        trasportmenu.add_cascade(label='ZMODEM', menu=ZMODEMmenu, underline=0)
        ZMODEMmenu.add_command(label="Use ZMODEM Sent", command=self._do_job)
        ZMODEMmenu.add_command(label="Use ZMODEM Receive", command=self._do_job)

        trasportmenu.add_command(label="Send the Cancellation Code", command=self._do_job)

        #1\Filemenu-->1\2\Log
        logmenu = tk.Menu(filemenu)
        filemenu.add_cascade(label='Log', menu=logmenu, underline=0)
        logmenu.add_command(label="Start", command=self._do_job)
        logmenu.add_command(label="Stop", command=self._do_job)
        logmenu.add_separator()#line
        logmenu.add_command(label="Pause", command=self._do_job)
        logmenu.add_command(label="Continue", command=self._do_job)
        logmenu.add_separator()#line
        logmenu.add_command(label="Open Log File", command=self._do_job)
        logmenu.add_command(label="Open Folder", command=self._do_job)

        filemenu.add_separator()#line
        filemenu.add_command(label='ShuXing', command=self._do_job)
        filemenu.add_separator()#line
        filemenu.add_command(label='Exit', command=self.quit)

        #2\Editmubu
        editmenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='编辑(Edit)', menu=editmenu)
        editmenu.add_command(label='Copy', command=self._do_job)
        editmenu.add_command(label='Copy as RTF Format', command=self._do_job)
        editmenu.add_command(label='Paste', command=self._do_job)
        editmenu.add_command(label='Paste the Selection', command=self._do_job)
        editmenu.add_separator()#line
        editmenu.add_command(label='Select All', command=self._do_job)
        editmenu.add_command(label='Select Screen', command=self._do_job)
        editmenu.add_separator()#line
        editmenu.add_command(label='Find', command=self._do_job)
        editmenu.add_separator()#line

        #2\Editmubu-->2\1\Notes
        notesmenu = tk.Menu(editmenu)
        editmenu.add_cascade(label='Notes', menu=notesmenu, underline=0)
        notesmenu.add_command(label="Selected Area", command=self._do_job)
        notesmenu.add_command(label="All", command=self._do_job)
        notesmenu.add_command(label="Current Screen", command=self._do_job)

        editmenu.add_separator()#line
        editmenu.add_command(label='Reset the Cursor', command=self._do_job)
        editmenu.add_command(label='Reset the Terminal', command=self._do_job)
        editmenu.add_command(label='Clean the Screen', command=self._do_job)

        #3\View
        viewmenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='查看(View)', menu=viewmenu)

        #4\Tools
        toolsmenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='工具(Tools)', menu=toolsmenu)

        #5\Bookpage
        bookpagemenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='标签页(Bookpage)', menu=bookpagemenu)

        #6\Windows
        windowsmenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='窗口(Windows)', menu=windowsmenu)

        #6\Help
        helpmenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='帮助(Help)', menu=helpmenu)
        helpmenu.add_command(label='TKShell Help', command=self._do_job)
        helpmenu.add_separator()#line
        helpmenu.add_command(label='Visit the Website', command=self._about_Website)
        helpmenu.add_command(label='Visit the BBS', command=self._about_BBS)
        helpmenu.add_separator()#line
        helpmenu.add_command(label='Checking Update', command=self._do_job)
        helpmenu.add_separator()#line
        helpmenu.add_command(label='About TKShell', command=self._help_about)

        self.config(menu=self.menubar)
    
    def _help_about(self):
        messagebox.showinfo('about', 'Coder：BigV4 \n\n TKShell verion 1.0 \n\n Thank You！! !\n ')  # 弹出消息提示框

    def _file_new(self):
        sessionpropertiesframe.SessionPropertiesFrame()

    def _about_Website(self):
        webbrowser.open("https://github.com/bigV4/tkshell")
        print(webbrowser.get())

    def _about_BBS(self):
        webbrowser.open("https://github.com/bigV4/tkshell/issues")
        print(webbrowser.get())
        
    def _do_job(self,message="!!!"):
        print("self._do_job  "+message)
        
if __name__ == '__main__':
    # 实例化Application
    app = TKSehllApplication()
    
    
    # 主消息循环:
    app.mainloop()

