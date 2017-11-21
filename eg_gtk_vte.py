#!/usr/bin/env python
#_*_coding:utf-8_*_
#python2.*
import sys
print("You need to use the python2.* to run this script!!!")
try :
	import gtk
except :
	print("You need to install the python gtk bindings")
	sys.exit(1)

try :
	import vte
except :
	error = gtk.MessageDialog(None, gtk.DIALOG_MODAL, gtk.MESSAGE_ERROR, gtk.BUTTONS_OK, 'You need to install python bindings for libvte')
	error.run()
	sys.exit(1)

if  __name__ == '__main__' :
	v = vte.Terminal()
	v.connect("child-exited", lambda term: gtk.main_quit())
	v.fork_command()
	window = gtk.Window()
	window.add(v)
	window.connect('delete-event', lambda window, event: gtk.main_quit())
	window.show_all()
	gtk.main()
