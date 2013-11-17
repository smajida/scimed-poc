# Author: Henrique Silvestre Souza

import cv2
import numpy as np
import scipy
from matplotlib import pyplot as plt
from scipy import ndimage
import os

def image_detect(file):
	# 255 white
	# 0 black

	# for filename in os.listdir('images'):
	# img = cv2.imread('images/'+filename,0)
	img = file
	new_img = cv2.resize(img,(600,700))

	x,y = img.shape

	filtered_img = scipy.misc.imfilter(img,'blur')


	i = 0
	while i < int(x * 0.01):
		filtered_img = scipy.misc.imfilter(filtered_img,'blur')
		# print i
		i += 1

	equalizated_img = cv2.equalizeHist(filtered_img)

	ret,thresh2 = cv2.threshold(equalizated_img,127,255,cv2.THRESH_BINARY_INV)

	label, qtd = ndimage.label(thresh2)

	i = 0
	while i < x:
		for b in thresh2[i]:
			if b == 0:
				break
			thresh2[i][np.where(thresh2[i] == b)[0][0]] = 0
		i += 1

	i = 0
	while i < len(thresh2):
		for b in thresh2[i][::-1]:
			if b == 0:
				break
			thresh2[i][::-1][np.where(thresh2[i][::-1] == b)[0][0]] = 0
		i += 1

	print filename + "- (X:%i,Y:%i)" % ndimage.measurements.center_of_mass(thresh2, label)
	print qtd

	# plt.imshow(thresh2, cmap=plt.cm.gray)
	# plt.show()

title = 'X-Ray Hipodisease Detect'

# Import Pmw from this directory tree.

import sys, Tkinter
sys.modules['tkinter'] = Tkinter

import Tkinter
import Pmw

class Demo:
    def __init__(self, parent):

	# Create and pack the MenuBar.
	menuBar = Pmw.MenuBar(parent,
		hull_relief = 'raised',
		hull_borderwidth = 1)

	menuBar.pack(fill = 'x')
	self.menuBar = menuBar

	# Add some buttons to the MenuBar.
    # here menu buttons file , edit and help are added to the menubar. menu
    # items open,close,save,print are added to file menu and menu items
	#cut,copy,paste are added to the edit menu.
 
	menuBar.addmenu('File','none')
	menuBar.addmenuitem('File','command',
		command = PrintOne('Action: open'),
		label = 'open')
	menuBar.addmenuitem('File', 'command',

		command = PrintOne('Action: close'),
		label = 'Close')
	menuBar.addmenuitem('File','command',
        command = PrintOne('Action:save'),
        label = 'save')
	menuBar.addmenuitem('File','command',
        command = PrintOne('Action:print'),
        label = 'print')

	menuBar.addmenuitem('File', 'separator')
	menuBar.addmenuitem('File', 'command',
		command = PrintOne('Action: exit'),
		label = 'Exit')

	menuBar.addmenu('Edit','none')
	menuBar.addmenuitem('Edit', 'command', 
		command = PrintOne('Action: cut'),
		label = 'cut')
	menuBar.addmenuitem('Edit', 'command',
        command = PrintOne('Action: copy'),
        label = 'copy')
	menuBar.addmenuitem('Edit', 'command',
        command = PrintOne('Action: paste'),
        label = 'paste')

	menuBar.addmenu('Help','none', side = 'right')
	menuBar.addmenuitem('Help', 'command',
		command = PrintOne('Action: about'),
		label = 'About...')

	# Create and pack the main part of the window.
	self.mainPart = Tkinter.Label(parent,
		text = 'This is the\nmain part of\nthe window',
		background = 'black',
		foreground = 'white',
		padx = 60,
		pady = 60)
	self.mainPart.pack(fill='both',expand=1)
	
class PrintOne:
	def __init__(self,text):
		self.text=text
   
	def __call__(self):
		print self.text

######################################################################

# Create demo in root window for testing.
if __name__ == '__main__':
    root = Tkinter.Tk()
    Pmw.initialise(root)
    root.title(title)

    exitButton = Tkinter.Button(root, text = 'Exit', command =
root.destroy)
    exitButton.pack(side = 'bottom')
    widget = Demo(root)
    root.mainloop()
