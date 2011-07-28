from sikuli.Sikuli import *

class googleSearchImages():

	imgDict = {}
	
	def __init__(self):
		self.imgDict = {}
		self.addImage("googleIcon","googleIcon.png")
		self.addImage("googleBar","googleTextbox.png")
		self.addImage("googleSearchButton","googleSearch.png")
		
	def addImage(self, name, img):
		self.imgDict[name] = img
		
	def getImage(self, name):
		return self.imgDict[name]

#y = googleSearchImages()
#click(y.getImage("googleSearchButton"))