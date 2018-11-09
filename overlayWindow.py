import tkinter as tk
from tkinter import *
from tkinter import filedialog

fileLocation = ''
def getFileLocation():
	global fileLocation
	fileLocation = filedialog.askopenfilename(initialdir = "/",title = "Select file")
	print(fileLocation)

def initialize():
	if len(fileLocation) == 0:
		print('No file selected')
	else:
		print('file selected!')

def createWindow():
	root = tk.Tk()
	root.title('Select Overlay')
	tk.Label(root,text='Select sample file to overlay:',justify=tk.CENTER,padx=20).grid(row=0)
	tk.Button(root,text="Location",justify=tk.CENTER,padx=20,width=25,command=getFileLocation).grid(row=1)
	frame= tk.Frame(root)
	frame.grid(row=2)
	tk.Button(frame,text="OK" ,command = initialize).pack(side=tk.LEFT)
	tk.Button(frame,text="Cancel", command=root.destroy).pack(side=tk.LEFT)

	root.mainloop()