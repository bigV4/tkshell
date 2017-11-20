#_*_coding:utf-8_*_
try:#python2
    import Tkinter as tk
    #建议按照python3的名字进行import
except ImportError:#python3
    import tkinter as tk
    
import os
import sys
if sys.version > '3':
    PY3 = True
else:
    PY3 = False
print("PY3 = %s" %PY3)
root = tk.Tk()
termf = tk.Frame(root, height=384, width=683)

termf.pack(fill="both", expand="yes")
wid = termf.winfo_id()
os.system('xterm -into %d -geometry 680x50 -e ./backup.shell -sb &' % wid)
root.mainloop()
