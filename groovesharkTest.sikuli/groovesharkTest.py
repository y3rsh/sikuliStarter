from sikuli.Sikuli import *
import os
myPath = os.path.dirname(getBundlePath())
if not myPath in sys.path: sys.path.append(myPath)
from groovesharkTestImages import *
from util import *
from regionDictionary import *

class groovesharkTest(util):
	myImages = groovesharkTestImages()
<<<<<<< HEAD
	reg = regionDictionary(900,1600)
	
=======
>>>>>>> a91df6350e6acba3f4b5ade8089de998144a5157
	def clickFavorites(self):
		
		self.reg.getReg("ne").click(self.myImages.getImage("favorites"))
		wait(2)

	def login(self,user,pw):
		try:
			self.reg.getReg("rightHalf").click(self.myImages.getImage("login")) 
			wait(2)
			type(user)
			type(Key.TAB)
			type(pw)
			type(Key.TAB)
			type(Key.ENTER)
			wait(4)
			self.passed("login")
		except FindFailed:
			self.criticalError("login")
	
	def playSong(self,image):
		doubleClick(image)
		wait(1)

	def addSong(self,image):
		hover(image)
		click(self.myImages.getImage("addSong"))
		wait(1)

	def clearPlaylist(self):
		click(self.myImages.getImage("removePlaylist"))
		wait(1)

	def playAll(self):
		click(self.myImages.getImage("playAll"))
		wait(1)

	def seeAllMusic(self):
		click(self.myImages.getImage("myMusic"))
		wait(1)

	def searchForMusic(self,term):
		try:
<<<<<<< HEAD
			self.reg.getReg("ne").click(self.myImages.getImage("searchButton"))
			wait(2)
			type(term)
=======
			click(self.myImages.getImage("searchButton"))
			wait(1)
			click(self.myImages.getImage("searchButton"))
			click(self.myImages.getImage("darkSearchMusic"))
			type(term)
			#click(self.myImages.getImage("searchButton2"))
>>>>>>> a91df6350e6acba3f4b5ade8089de998144a5157
			type(Key.ENTER)
			wait(4)
			self.passed("Music Search")
		except FindFailed:
			self.failed("Music Search")
<<<<<<< HEAD

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
		
=======
	
>>>>>>> a91df6350e6acba3f4b5ade8089de998144a5157
	def logoutGrooveshark(self):
		click(self.myImages.getImage("accountButton"))
		click(self.myImages.getImage("logout"))
		wait(1)

<<<<<<< HEAD
#g = groovesharkTest()
#g.searchForMusic("weezer")

=======
>>>>>>> a91df6350e6acba3f4b5ade8089de998144a5157



	