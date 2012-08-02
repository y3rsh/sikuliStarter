from sikuli.Sikuli import *

class groovesharkTestImages():

	imgDict = {}
	
	def __init__(self):
		self.imgDict = {}
		self.addImage("login",Pattern("namEMembermg.png").targetOffset(1,-2))
		self.addImage("myMusic","myMusic.png")
		self.addImage("playSong","playSong.png")
		self.addImage("playAll","playAll.png")
		self.addImage("favorites","favorites.png")
		self.addImage("username",Pattern("BecomeaMembe-1.png").similar(0.90).targetOffset(-124,56))
		self.addImage("password",Pattern("imammeLoginw.png").similar(0.58).targetOffset(-120,-64))
		self.addImage("loginButton",Pattern("imammeLoginw.png").targetOffset(-116,-20))
		self.addImage("addSong","addSong.png")
		self.addImage("removePlaylist","removePlaylist.png")
		self.addImage("accountButton","accountButton.png")
		self.addImage("logout","logout.png")
<<<<<<< HEAD
		self.addImage("searchButton",Pattern("1seam-1.png").similar(0.85).targetOffset(-18,1))
		self.addImage("lightSearchMusic",Pattern("1seam.png").targetOffset(-29,0))
		self.addImage("darkSearchMusic",Pattern("1seam.png").targetOffset(-29,0))
		
	
=======
		self.addImage("searchButton","searchButton.png")
		self.addImage("lightSearchMusic","lightSearchMusic.png")
		self.addImage("darkSearchMusic","darkSearchMusic.png")
		self.addImage("searchButton2","searchButton2.png")
		self.addImage("unwellSong","unwell.png")
>>>>>>> a91df6350e6acba3f4b5ade8089de998144a5157
		
	def addImage(self, name, img):
		self.imgDict[name] = img
		
	def getImage(self, name):
		return self.imgDict[name]