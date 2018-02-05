#!/usr/bin/env python

try:
	from tkinter import *
else:
	from Tkinter import *
import time

root=Tk()
root.attributes("-fullscreen",False)
root.configure(background='black')
root.geometry("700x100")
time_tester = ''

#local time variables
local_time_title = Label(root, font=("arial", 20, 'bold'),fg='red', bg='black')
local_time_title.pack()
local_time = Label(root, font=('arial', 50, 'bold'),fg='red',bg='black')
local_time.pack()

def dragontime():
	gobal time_tester
	local_time_var = time.strftime('%H:%M:%S')
	zulu_time_var = time.strftime('%H:%M:%S', time.gmtime())
	if local_time_var != local_time_var:
		time_tester = local_time_var
		#add localtime to GUI
		local_time.config(text=local_time_var + '    '+ zulu_time_var)
		local_time_title.config(text='(LOCAL)' + '\t\t' + '(ZULU)')
		local_time_title.config(text=('{: <20}{: >20}').format('(LOCAL)','(ZULU)'))
	local_time.after(20,dragontime)
dragontime()
root.mainloop()
