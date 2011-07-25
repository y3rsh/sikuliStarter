from sikuli.Sikuli import *
from util import *
from groovesharkTestImages import *

class groovesharkTest:

	myImages = groovesharkTestImages()
	myUtil = util()

	def openGrooveshark(self):
		self.myUtil.openFirefox()
		self.myUtil.inputUrl("http://grooveshark.com/")
		wait(4)

	def clickFavorites(self):
		click(self.myImages.getImage("favorites"))
		wait(2)

	def login(self,user,pw):
		click(self.myImages.getImage("login"))
		click(self.myImages.getImage("username"))
		type(user)
		click(self.myImages.getImage("password"))
		type(pw)
		click(self.myImages.getImage("loginButton"))
		wait(4)

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
		click(self.myImages.getImage("searchButton"))
		wait(1)
		click(self.myImages.getImage("searchButton"))
		click(self.myImages.getImage("darkSearchMusic"))
		type(term)
		#click(self.myImages.getImage("searchButton2"))
		type(Key.ENTER)
		wait(4)

	def logoutGrooveshark(self):
		click(self.myImages.getImage("accountButton"))
		click(self.myImages.getImage("logout"))
		wait(1)

	def closeGrooveshark(self):
		self.myUtil.closeBrowser()

	

	