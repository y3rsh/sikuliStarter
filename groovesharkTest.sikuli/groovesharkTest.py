from sikuli.Sikuli import *
import os
myPath = os.path.dirname(getBundlePath())
if not myPath in sys.path: sys.path.append(myPath)
from groovesharkTestImages import *
from util import *
from regionDictionary import *

class groovesharkTest(util):
	myImages = groovesharkTestImages()
	def searchForTermsFromDataFile(self):
		for i in range(len(self.termsArr)):	
			self.searchForMusic(self.termsArr[i]," Terms from data File ")
			
	def searchForMusic(self,term,testName):
		try:
			self.clearMouse()
			self.reg.getReg("ne").click(self.myImages.getImage("searchButton"))
			wait(2)
			self.clearSearch()
			type(term)
			type(Key.ENTER)
			wait(4)
			self.passed(testName + term)
		except FindFailed:
			self.failed(testName + term)


	def clearSearch(self):
		try:
			self.reg.getReg("ne").click(self.myImages.getImage("searchButton"))
			wait(2)
			type("a",KEY_CTRL)
			type(Key.DELETE)
			wait(4)
		except FindFailed:
			self.failed("Clear Search  Field")

	
#unit test
#g = groovesharkTest()
#g.searchForTermsFromDataFile("Terms from File")