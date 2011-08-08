from sikuli.Sikuli import *
import subprocess
import datetime
import os
import shutil
import traceback
import sys
import ConfigParser
myPath = os.path.dirname(getBundlePath())
if not myPath in sys.path: sys.path.append(myPath)
from regionDictionary import *

class util:

	def __init__(self):
		# read the config file and get the variables
		config = ConfigParser.ConfigParser()
		config.read('C:\\sikuli\\config\\config.txt')
			
		# grab each variable seperately
		self.findFaildsCounter = int(config.get("vars","failCount"))
		self.findFaildsLimit = int(config.get("vars","failLimit"))
		self.startOfTimer = config.get("vars","startTimer")
		self.endOfTimer = config.get("vars","endTimer")
		self.dateFormatString = config.get("vars","dateFormat")
		self.site = config.get("vars","site")
		self.screenWidth = int(config.get("vars","screenWidth"))
		self.screenHeight = int(config.get("vars","screenHeight"))
		self.ie = config.get("vars","iePath")
		self.firefox = config.get("vars","firefoxPath")
		self.chrome = config.get("vars","chromePath")
		self.user = ""
		self.password = ""
		self.delim = ","
		#create region dictionary
		self.reg = regionDictionary(self.screenWidth,self.screenHeight)
		# create new directory
		self.folder = "C:\\sikuli\\logs\\"+self.timeStamp()
		self.createDirectory(self.folder)
		self.csvPath = self.folder+"\\logFile.txt"
		self.imagePath = self.folder

		# read the data file and get the variables
		data = ConfigParser.ConfigParser()
		data.read("C:\\sikuli\\testData\\testdata.txt")

		# grab the terms string and seperate them into an array
		self.termsArr = data.get("terms","term").split(",")
		self.usersArr = data.get("terms","users").split(",")
		self.paswordsArr = data.get("terms","passwords").split(",")
		for i in self.usersArr:
			print i

	# this method returns a time stamp
	def timeStamp(self):
	        return datetime.datetime.now().strftime(self.dateFormatString)
			
	# this method is used to terminate the test when
	# an error is too critical to continue
	def criticalError(self,test):
	        # if findFaildsCounter equals findFaildsLimit
	        # the handleFindFailds method terminates the test
	        self.findFaildsCounter =  self.findFaildsLimit
	
	        # terminate the test
	        self.handleFindFailds(test)
	
	# this method will move the mouse to the corner to avoid
	# disrupting an image the program is trying to locate
	def clearMouse(self):
	        # move the mouse to the top-left corner
	        mouseMove(Location(0,0))
	
	# this method will log information every time
	# a test passes successfully
	def passed(self,test,comment=""):
	        status = "PASSED"
	
	        # set 't' to today's date
	        t = datetime.datetime.now().strftime(self.dateFormatString)
	
	        # call this method to take the screenshot
	        self.captureMyScreen(status,t)
	
	        # format the string that will be written to a csv file
	        theString = test+self.delim+t+self.delim+self.user+self.delim+self.site+self.delim+comment+self.delim+status+"\n"
	
	        # write the string to the file
	        
	        logFile = open(self.csvPath,'a')
	        logFile.write(theString)
	        print(theString)
	        logFile.close()

	
	# this method will log information every time
	# a test fails
	def failed(self,test,comment=""):	
	        status = "FAILED"
			
	        # set 't' to today's date
	        t = datetime.datetime.now().strftime(self.dateFormatString)
	
	        # call this method to take the screenshot
	        self.captureMyScreen(status,t)
	
	        # format the string that will be written to a csv file
	        theString = test+self.delim+t+self.delim+self.user+self.delim+self.site+self.delim+comment+self.delim+status+"\n"
	
	        # write the string to the file
	        logFile = open(self.csvPath,'a')
	        logFile.write(theString)
	        print(theString)
	        logFile.close()

	        self.handleFindFailds(test)
	
	# this method takes a screenshot of the
	# entire screen
	def captureMyScreen(self,status,stamp):
	
	        # create a new region to screenshot
	        newarea = capture(Region(0,0,self.screenWidth,self.screenHeight))
	        print "File ", newarea
	
	        # create the file's name
	        fileName = stamp + status + ".png"
	
	        # create the path to save the screenshot
	        goodPath = os.path.join(self.imagePath,fileName)
	        print(goodPath)
	
	        # save the screenshot to the specified directory
	        shutil.move(newarea, goodPath)
	

	# this method stores a username and password
	def getUserAndPass(self):
	        # store the user's input
	        self.user = input("Enter username to test with.").strip()
	        self.password = input("Enter password.").strip()
	
	# this method stores the text from a textbox
	def getTextFromTextBox(self):
	        # select and copy the test
	        type("a", KEY_CTRL)
	        type("c", KEY_CTRL)
	
	        # return the selected text
	        return Env.getClipboard().strip()
	
	# this method stores the current time to time a test
	def startTimer(self):
	        # store the current time
	        self.startOfTimer = datetime.datetime.now()
	
	# this method stores the current time and
	# returns the time a test took to complete
	def stopTimer(self):
	        # get the current time
	        self.endOfTimer = datetime.datetime.now()
	
	# this method returns the time a test took
	# to complete
	def timerDiff(self):
	
	        # return the difference of the timers
	        return str(self.endOfTimer - self.startOfTimer)
	
	# this method will wait for an image to appear and
	# wait a given amount of time before checking again
	def myWaitUntil(img, tstep = .1, nMax = 90,msg=None):  # waits for defaults to find an image
	        found = False
	
                # loop through the check a given amount of
                # times to see if the image has appeared
                for i in range(nMax):

                        # if found then break out of
                        # the loop and return true
                        if exists(img, 0) != None:
                                found = True
                                break

                        # wait a given amount of time between
                        # each iteration of the loop
                        wait(tstep)
	
	        # return whether or not the image was found
	        return found
	
	# this method will wait for an image to disappear and
	# wait a given amount of time before checking again
	def imageGone(img="", tstep = 1, nMax = 90):  #look for a change on the screen
		counter = 0
		gone = False
	
	   # loop through the check to see if the
	   # image is gone
		for i in range(nMax):

			# if the image is gone increase the counter
			if exists(img, 0)  == None:
				counter = counter+1

				# return true after the image has been
				# gone for 2 iterations
				if counter == 2:
					gone = True
					break

				# wait a given amount of time between
				# each iteration
		wait(tstep)

        # return whether or not the image is gone
		return gone
	
	# this method will determine whether or not to
	# terminate the test after an error
	def handleFindFailds(self,test):
	        # if the number of fails is less than the limit
	        # then print a message to the console
	        if self.findFaildsCounter < self.findFaildsLimit:
	                failure = str(sys.exc_info())
	                myMessage = "My Message " + failure
	                print(myMessage)
	                #failed(test)
	                #findFaildsCounter = findFaildsCounter + 1
	
	        # if the fail count is greater than the limit
	        # then log it and terminate the test
	        else:
	                input("Critical Error(s) have occurred @ test " + test + " Script is stopping.")
	                self.endSanity()
	
	# this method opens internet explorer
	def openIE(self):
	        test = "IE Opened"
	        path = self.ie
	        if path == "":
	        	path = "C:\\Program Files\\Internet Explorer\\iexplore.exe"
	        openApp(path)
			
	def openFirefox(self):
	        test = "Firefox Opened"
	        path = self.firefox
	        print("path = " + path)
	        if path == "":
	        	path = "c:\\Program Files\\Mozilla Firefox\\firefox.exe"
	        openApp(path)

	
	# this method will insert a new URL
	def inputUrl(self,site="whyyounoenterurl?"):
	        wait(4)
	
	        # simulate keystrokes
	        type(" ",KEY_ALT)
	        wait(1)
	        type("x")
	        wait(1)
	        type("d",KEY_ALT)
	        wait(1)
	        if site=="":
	        	site=self.site
	        # paste in the URL
	        paste(site)
	        type(Key.ENTER)
	        print site

	# this method will create a new directory
	# example: newPath = "C:\\Documents and Settings\\RLevell\\Desktop\\sikuli_test"
	def createDirectory(self,path):
	        os.makedirs(path)

	# this method will open and run fiddler
	def runFiddler(self,scenario):
	
	        # try to open fiddler
	        try:
				subprocess.call("C:\\Program Files\\Fiddler2/ExecAction.exe \"sikuli " + scenario +"\"")
				print("wrote " + scenario + " scenario fiddler info to file." )
	
	        # end the test if not opened successfully
	        except FindFailed:
	                self.criticalError(test)

	def closeBrowser(self):
		type(Key.F4,KEY_ALT)