from sikuli.Sikuli import *

class groovesharkTestImages():

	imgDict = {}
	
	def __init__(self):
		self.imgDict = {}
		self.addImage("login","login.png")
		self.addImage("myMusic","myMusic.png")
		self.addImage("playSong","playSong.png")
		self.addImage("playAll","playAll.png")
		self.addImage("favorites","favorites.png")
		self.addImage("username","username.png")
		self.addImage("password","password.png")
		self.addImage("loginButton","loginButton.png")
		self.addImage("addSong","addSong.png")
		self.addImage("removePlaylist","removePlaylist.png")
		self.addImage("accountButton","accountButton.png")
		self.addImage("logout","logout.png")
		self.addImage("searchButton","searchButton.png")
		self.addImage("lightSearchMusic","lightSearchMusic.png")
		self.addImage("darkSearchMusic","darkSearchMusic.png")
		self.addImage("searchButton2","searchButton2.png")
		self.addImage("unwellSong","unwell.png")
		
	def addImage(self, name, img):
		self.imgDict[name] = img
		
	def getImage(self, name):
		return self.imgDict[name]