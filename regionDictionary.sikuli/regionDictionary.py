from sikuli.Sikuli import *

class regionDictionary:

	regDict = {}
	
	def __init__(self,screenWidth,screenHeight):
		self.regDict = {}
		self.addReg("topHalf",Region(0,0,screenWidth,(screenHeight/2)))
		self.addReg("bottomHalf",Region(0,(screenHeight/2),screenWidth,(screenHeight/2)))
		self.addReg("leftHalf",Region(0,0,(screenWidth/2),screenHeight))
		self.addReg("rightHalf",Region((screenWidth/2),0,(screenWidth/2),screenHeight))
		self.addReg("center",Region((screenWidth*(2/3)),(screenHeight*(2/3)),(screenWidth*(1/3)),(screenHeight*(1/3))))
		self.addReg("nw",Region(0,0,(screenWidth/2),(screenHeight/2)))
		self.addReg("sw",Region(0,(screenHeight/2),(screenWidth/2),(screenHeight/2)))
		self.addReg("ne",Region((screenWidth/2),0,(screenWidth/2),(screenHeight/2)))
		self.addReg("se",Region((screenWidth/2),(screenHeight/2),(screenWidth/2),(screenHeight/2)))
	def addReg(self, name, reg):
		self.regDict[name] = reg
		
	def getReg(self, name):
		return self.regDict[name]