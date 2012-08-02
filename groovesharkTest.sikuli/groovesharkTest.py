from sikuli.Sikuli import *
import os
myPath = os.path.dirname(getBundlePath())
if not myPath in sys.path: sys.path.append(myPath)
from groovesharkTestImages import *
from util import *
from regionDictionary import *

class groovesharkTest(util):
	myImages = groovesharkTestImages()

	reg = regionDictionary(900,1600)
	
	def searchForMusic(self,term):
		try:
			self.reg.getReg("ne").click(self.myImages.getImage("searchButton"))
			wait(2)
			type(term)
			click(self.myImages.getImage("searchButton"))
			wait(1)
			click(self.myImages.getImage("searchButton"))
			click(self.myImages.getImage("darkSearchMusic"))
			type(term)
			#click(self.myImages.getImage("searchButton2"))
			type(Key.ENTER)
			wait(4)
			self.passed("Music Search")
		except FindFailed:
			self.failed("Music Search")


	def clearSearch(self):
		try:
			self.reg.getReg("ne").click(self.myImages.getImage("searchButton"))
			wait(2)
			type("a",KEY_CTRL)
			type(Key.DELETE)
			wait(4)
			self.passed("Clear Search Field")
		except FindFailed:
			self.failed("Clear Search  Field")

	

#g = groovesharkTest()
#g.searchForMusic("weezer")





	