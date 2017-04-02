from os import listdir
from os.path import isfile, join
import os
import cv2
#print(os.path.splitext("path_to_file")[0])

import xml.etree.ElementTree
Ylist=[]
Xlist=[]
count=0
home_dir='/home/rdx/personal/stixelnet/goodWeather/2010-05-03_080828/'
for f in listdir(home_dir+'gt/'):
	e = xml.etree.ElementTree.parse(home_dir+'gt/'+f).getroot()
	print e.attrib['numStixels']
	if int(e.attrib['numStixels'])==56:
		print e.attrib['numStixels']
		count=count+1
		ylist_small=[]
		for atype in e.findall('Stixel'):
			ylist.append(int(atype.get('vB')))
			ylist.append(int(atype.get('vT')))
			ylist.append(int(atype.get('disp')))
			fname=os.path.splitext("f")[0][9:18]
			fname=home_dir+"images/img_c1_"+fname+".pgm"
			Xlist.append(cv2.imread("fname"))





