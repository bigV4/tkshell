from tkinter import *
import os

root = Tk()
termf = Frame(root, height=384, width=683)

termf.pack(fill=BOTH, expand=YES)
wid = termf.winfo_id()
os.system('xterm -into %d -geometry 680x50 -e ./cach.shell -sb &' % wid)
#os.system('xterm -into %d -sb &' % wid)
root.mainloop()
