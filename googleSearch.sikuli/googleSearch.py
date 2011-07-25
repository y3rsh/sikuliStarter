from sikuli.Sikuli import *
from util import *
from googleSearchImages import *

class googleSearch:

	myUtil = util()
	myImages = googleSearchImages()

	def openGoogle(self):
		self.myUtil.openFirefox()
		self.myUtil.inputUrl("http://www.google.com/")
		wait(4)

	def selectSearchBox(self):
		click(self.myImages.getImage("googleBar"))

	def pasteToSearchBox(self,search):
		paste(search)

	def typeInSearchBox(self,term):
		type(term)

	def searchGoogle(self):
		#click(self.myImages.getImage("googleSearchButton"))
		type(Key.ENTER)
		wait(4)

	def googleHome(self):
		self.myUtil.inputUrl("http://www.google.com/")
		wait(4)