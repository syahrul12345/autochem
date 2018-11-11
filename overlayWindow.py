import tkinter as tk
from tkinter import *
from tkinter import filedialog

import OverlaySample

def getFileLocation(data):
	#should be a SMP file, it will either obtain data from the corresponding XLXS(if it exists) OR
	#create a new XLSX file with the prepackeged mic module by micromeritics(feature still testing, and possibly impossible)
	fileLocation = filedialog.askopenfilename(initialdir = "/",title = "Select file")
	data.fileLocation = fileLocation
	

def initialize(data):
	# put this in a try clause in case no sample was selected to overlay
	try:
		overlaysampleData = OverlaySample.getDataFromExcel(data.fileLocation)
		data.sample2 = overlaysampleData
	except FileNotFoundError:
		createNoFilePopup()


	
def createNoFilePopup():
	popupwin = tk.Toplevel()
	popupwin.title('Error !')
	
	l = tk.Label(popupwin,justify=tk.LEFT,padx=20,text='No sample overlay file is selected!')
	l.grid(row=0)
	
	popupbutton = tk.Button(popupwin,text="OK",command = popupwin.destroy)
	popupbutton.grid(row=1,column=0)



def createWindow(data):
	root = tk.Tk()
	root.title('Select Overlay')
	tk.Label(root,text='Select sample file to overlay:',justify=tk.CENTER,padx=20).grid(row=0)
	tk.Button(root,text="Location",justify=tk.CENTER,padx=20,width=25,command=lambda: getFileLocation(data)).grid(row=1)
	frame= tk.Frame(root)
	frame.grid(row=2)
	tk.Button(frame,text="OK" ,command = lambda: initialize(data)).pack(side=tk.LEFT)
	tk.Button(frame,text="Cancel", command=root.destroy).pack(side=tk.LEFT)
	root.mainloop()