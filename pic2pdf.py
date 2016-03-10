# -*- coding: utf-8 -*-
 
import os
import sys
from PIL import Image
from reportlab.pdfgen import canvas

picList = []
picType = ['.jpg','.jpeg','.bmp','.png','.gif']

def conpdf(img):
	f_pdf = os.path.splitext(img)[0]+'.pdf'
	imgpath =  os.path.join(os.path.abspath('.'),img)
	pdfpath = os.path.join(os.path.abspath('.'),f_pdf)
	imgsize = Image.open(imgpath).size
	(w,h) =  imgsize
	c = canvas.Canvas(pdfpath, imgsize)
	c.drawImage(imgpath, 0, 0, w, h)
	c.save()
	print imgpath
	print pdfpath + '   ok!'
 
def getPicList():
	global picList
	path = os.path.abspath('.')
	for x in os.listdir(path):
		if os.path.isfile(x):
			if os.path.splitext(x)[1] in picType:
				picList.insert(1,x)
				
def main():
	getPicList()
	for img in picList:
		conpdf(img)
		
if __name__ == '__main__':
	main()
	raw_input()
