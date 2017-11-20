#!/usr/bi/python
#_*_coding:utf-8_*_
import os
import time
import sys
print(sys.version)
if sys.version > '3':
    import webbrowser
    import tkinter as tk
    from tkinter import ttk
    from tkinter import filedialog
    from tkinter import messagebox
else:
    import webbrowser
    import Tkinter as tk
    import ttk
    import tkFileDialog as filedialog
    import tkMessageBox
    PY3 = False

import sessionpropertiesframe
'''通过调用xterm来实现shell终端'''
class TKSehllApp(tk.Tk):
    '''
    TKShell 主界面程序
        界面与逻辑分离
    '''
    def __init__(self, master=None,name="!"):
        '''初始化'''
        self.name = name
        #类的构造方法必须调用其父类的构造方法来进行基本的初始化。
        if sys.version > '3':
            super().__init__() # 有点相当于tk.Tk()
        else:
            tk.Tk()
        self.createWidgets()
        sessioncachlist = []
        print("【tkshell.py调试信息】TKSehllApplication = %r %s" %(self, id(self)))

    def createWidgets(self):
        self.title(self.name + "TKShell (free for everyone)")
        self.geometry('683x400')

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
        tabmenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='标签页(Tab)', menu=tabmenu)

        #6\Windows
        windowmenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='窗口(Window)', menu=windowmenu)

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
        #放置菜单栏
        self.config(menu=self.menubar)
        #构建标签页的frame
        self.TabStrip = ttk.Notebook(self)
        self.TabStrip.place(relx=0.005, rely=0.005, relwidth=0.990, relheight=0.990)
    def _help_about(self):
        messagebox.showinfo('about', 'Coder：BigV4 \n\n TKShell verion 1.0 \n\n Thank You！! !\n ')  # 弹出消息提示框

    def creatSessionFrame(self):
        print("creatSessionFrame")
    
        
    # 设置session参数并建立session更新窗口
    def _file_new(self):
        # 点击后弹窗   
        print("【tkshell.py调试信息】self = %s %r" %(id(self), self))
        settingFrame = sessionpropertiesframe.SessionPropertiesFrame(self, titlename="New Session")
        self.wait_window(settingFrame) # 这一句很重要！！！
        # 接收弹窗的数据
        res = settingFrame.sessionpropertiesinfo
        print("【tkshell.py调试信息】：res=%s" %res)
        if res is None: return
        # 设置参数和bash脚本
        #    1、没有填写Password
        if "SSH"==res["Protocol"]:
            try:
                file_object = open('./cach.shell', mode="wt")#以文本写方式打开，只能写文件
                file_object.write("#!/usr/bin/expect\n")
                file_object.close()
                file_object = open('./cach.shell', mode="a")#以追加方式打开
                file_object.write("\nset timout 3\n")
                file_object.write("send \"bash\\r\"\n")
                if "Password"==res["Method"]:
                    file_object.write("spawn ssh -p %s %s@%s -y\n" %(str(res["Port"]), res["UserName"], str(res["Host"]), ))
                elif "Public Key"==res["Method"]:
                    file_object.write("spawn ssh -p %s %s@%s -y\n" %(str(res["Port"]), res["UserName"], str(res["Host"]), ))
                elif "Keyboard Interactive"==res["Method"]:
                    file_object.write("spawn ssh -p %s %s@%s -y\n" %(str(res["Port"]), res["UserName"], str(res["Host"]), ))
                file_object.write("expect \"*password*\"\n")
                file_object.write("send \"%s\\r\"\n" %res["Password"])
                file_object.write("interact\n")
            except Exception as e:
                print("*"*50 + "\n[-]open(\'./cach.shell\')Error0 = %s\nfile=[tkshell.py]  function=[TKSehllApp_file_new()\n" %e +"*"*50)
            finally:
                 file_object.close()
                 
        elif "TELNET"==res["Protocol"]:
            try:
                file_object = open('./cach.shell', mode="wt")#以文本写方式打开，只能写文件
                file_object.write("#!/usr/bin/expect\n")
                file_object.close()
                file_object = open('./cach.shell', mode="a")#以追加方式打开
                file_object.write("\nset timout 3\n")
                file_object.write("send \"bash\\r\"\n")
                file_object.write("spawn telnet %s@%s %s\n" %(res["UserName"], str(res["Host"]), str(res["Port"]), ))
                file_object.write("expect \"*password*\"\n")
                file_object.write("send \"%s\\r\"\n" %res["Password"])
                file_object.write("interact\n")
            except Exception as e:
                print("*"*50 + "\n[-]open(\'./cach.shell\')Error1 = %s\nfile=[tkshell.py]  function=[TKSehllApp_file_new()\n" %e +"*"*50)
            finally:
                 file_object.close()

        elif "SFTP"==res["Protocol"]:
            try:
                file_object = open('./cach.shell', mode="wt")#以文本写方式打开，只能写文件
                file_object.write("#!/usr/bin/expect\n")
                file_object.close()
                file_object = open('./cach.shell', mode="a")#以追加方式打开
                file_object.write("\nset timout 3\n")
                file_object.write("send \"bash\\r\"\n")
                if "Password"==res["Method"]:
                    file_object.write("spawn sftp -P %s %s@%s -y\n" %(str(res["Port"]), res["UserName"], str(res["Host"]), ))
                elif "Public Key"==res["Method"]:
                    file_object.write("spawn sftp -P %s -i %s %s@%s -y\n" %(str(res["Port"]), res["UserName"], res["UserName"], str(res["Host"]), ))
                elif "Keyboard Interactive"==res["Method"]:
                    file_object.write("spawn sftp -P %s %s@%s -y\n" %(str(res["Port"]), res["UserName"], str(res["Host"]), ))
                file_object.write("expect \"*password*\"\n")
                file_object.write("send \"%s\\r\"\n" %res["Password"])
                file_object.write("interact\n")
            except Exception as e:
                print("*"*50 + "\n[-]open(\'./cach.shell\')Error2 = %s\nfile=[tkshell.py]  function=[TKSehllApp_file_new()\n" %e +"*"*50)
            finally:
                 file_object.close()
                 
        # 更新界面
        TabStrip_Tab1 = tk.Frame(self.TabStrip)
        self.TabStrip.add(TabStrip_Tab1, text=str(res["Name"]))
        tk.Button(TabStrip_Tab1, text="关闭(Close)").pack()
        shellFrame = tk.Frame(TabStrip_Tab1, height=364, width=683)
        shellFrame.pack()
        wid = shellFrame.winfo_id()
        os.system('xterm -into %d -geometry 683x50 -e ./cach.shell -sb &' % wid)
        


        
    def _about_Website(self):
        webbrowser.open("https://github.com/bigV4/tkshell")
        print(webbrowser.get())

    def _about_BBS(self):
        webbrowser.open("https://github.com/bigV4/tkshell/issues")
        print(webbrowser.get())
        
    def _do_job(self,message="!!!"):
        print("self._do_job  "+message)
        messagebox.showinfo('Not Completed', '此功能暂未完成，敬请期待！ \n\n This feature has not been completed！\n ')  # 弹出消息提示框

    def _create_sessiontab(self,session):
        
        print("_create_sessiontab %r" %session)
     
if __name__ == '__main__':
    # 实例化Application
    app = TKSehllApp()
    
    
    # 主消息循环:
    app.mainloop()

