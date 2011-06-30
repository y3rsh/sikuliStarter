import subprocess
import datetime
import os
import shutil
import traceback
import sys
import ConfigParser

class Utilities():

	def __init__(self):
		# read the config file and get the variables
		config = ConfigParser.ConfigParser()
		config.read("C:\\sikuli\\sikuliStarter\\config.txt")
		
		self.findFaildsCounter = config.get("vars","failCount")
		self.findFaildsLimit = config.get("vars","failLimit")
		self.startOfTimer = config.get("vars","startTimer")
		self.endOfTimer = config.get("vars","endTimer")
		self.dateFormatString = config.get("vars","dateFormat")
		self.site = config.get("vars","site")
		self.user = ""
		self.password = ""
		


	# this method is used to terminate the test when
	# an error is too critical to continue
	def criticalError(test):
	        #global findFaildsCounter
	        #global findFaildsLimit
	
	        # if findFaildsCounter equals findFaildsLimit
	        # the handleFindFailds method terminates the test
	        findFaildsCounter =  findFaildsLimit
	
	        # terminate the test
	        handleFindFailds(test)
	
	# this method will move the mouse to the corner to avoid
	# disrupting an image the program is trying to locate
	def clearMouse():
	        # move the mouse to the top-left corner
	        mouseMove(Location(0,0))
	
	# this method will log information every time
	# a test passes successfully
	def passed(test,comment=""):
	        # format the date
	        #global dateFormatString
	
	        # set 't' to today's date
	        t = datetime.datetime.now().strftime(dateFormatString)
	
	        # call this method to take the screenshot
	        captureMyScreen(status,t)
	
	        # format the string that will be written to a csv file
	        theString = test+delim+t+delim+user+delim+site+delim+comment+"\n"
	
	        # write the string to the file
	        f.write(theString)
	        print(theString)
	
	# this method will log information every time
	# a test fails
	def failed(test,comment=""):
	        # format the date
	        #global dateFormatString
	
	        # set 't' to today's date
	        t = datetime.datetime.now().strftime(dateFormatString)
	
	        # call this method to take the screenshot
	        captureMyScreen(status,t)
	
	        # format the string that will be written to a csv file
	        theString = test+delim+t+delim+user+delim+site+delim+comment+"\n"
	
	        # write the string to the file
	        f.write(theString)
	        print(theString)
	
	# this method takes a screenshot of the
	# entire screen
	def captureMyScreen(status,stamp):
	        # create a new region to screenshot
	        newarea = capture(Region(3,0,1273,796))
	        print "File ", newarea
	
	        # create the file's name
	        fileName = stamp + status + ".png"
	
	        # create the path to save the screenshot
	        goodPath = os.path.join(picPath,fileName)
	        print(goodPath)
	
	        # save the screenshot to the specified directory
	        shutil.move(newarea, goodPath)
	
	# this method ends the test
	def endSanity():
	        f.close()
	        exit()
	
	# this method stores a username and password
	def getUserAndPass():
	        #global user
	        #global password
	
	        # store the user's input
	        user = input("Enter username to test with.").strip()
	        password = input("Enter password.").strip()
	
	# this method stores the text from a textbox
	def getTextFromTextBox():
	        # select and cpoy the test
	        type("a", KEY_CTRL)
	        type("c", KEY_CTRL)
	
	        # return the selected text
	        return Env.getClipboard().strip()
	
	# this method stores the current time to time a test
	def startTimer():
	        #global startOfTimer
	
	        # store the current time
	        startOfTimer = datetime.datetime.now()
	
	# this method stores the current time and
	# returns the time a test took to complete
	def stopTimer():
	        #global startOfTimer
	        #global endOfTimer
	
	        # get the current time
	        endOfTimer = datetime.datetime.now()
	
	        # return the difference of the times
	        return str(endOfTimer - startOfTimer)
	
	# this method returns the time a test took
	# to complete
	def timerDiff():
	        #global startOfTimer
	        #global endOfTimer
	
	        # return the difference of the timers
	        return str(endOfTimer - startOfTimer)
	
	# this method will wait for an image to appear and
	# wait a given amount of time before checking again
	def myWaitUntil(img="", theRegion = Region(11,11,1636,1019) ,tstep = .1, nMax = 90,msg=None):  # waits for defaults to find an image
	        found = False
	
	        # search in a specific region
	        with(theRegion):
	
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
	def imageGone(img, theRegion = Region(11,11,1636,1019), tstep = 1, nMax = 90):  #look for a change on the screen
		counter = 0
		gone = False
	
	   # loop through the check to see if the
	   # image is gone
		for i in range(nMax):
			with(theRegion):

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
	def handleFindFailds(test):
	        #global findFaildsCounter
	        #global findFaildsLimit
	
	        # if the number of fails is less than the limit
	        # then print a message to the console
	        if findFaildsCounter < findFaildsLimit:
	                failure = str(sys.exc_info())
	                myMessage = "My Message " + failure
	                print(myMessage)
	                #failed(test)
	                #findFaildsCounter = findFaildsCounter + 1
	
	        # if the fail count is greater than the limit
	        # then log it and terminate the test
	        else:
	                failed(test)
	                input("Critical Error(s) have occurred @ test " + test + " Script is stopping.")
	                endSanity()
	
	# this method opens internet explorer
	def openIE():
	        test = "IE Opened"
	        openApp("C:\Program Files\Internet Explorer\iexplore.exe")
	
	        # called the method and pass the test if IE
	        # opened correctly
	        if myWaitUntil(Region(0,296,1280,504)):
				passed(test)
	
	        # end the test if not
	        else:
				criticalError(test)
	
	# this method opens firefox
	###
	def openFF():
	        test = "FF Opened"
	        with(Region(0,698,308,102)):
	                click()
	        wait(3)
	
	        # called the method and pass the test if IE
	        # opened correctly
	        if myWaitUntil(Region(0,296,1280,504)):
	                passed(test)
	
	        # end the test if not
	        else:
	                criticalError(test)
	
	# this method will open chrome
	def openChrome():
	        test = "Chrome Opened"
	        openApp("C:\Documents and Settings\jtmcve\Local Settings\Application Data\Google\Chrome\Application\chrome.exe")
	
	        # called the method and pass the test if IE
	        # opened correctly
	        if myWaitUntil(Region(0,296,1280,504)):
	                passed(test)
	
	        # end the test if not
	        else:
	                criticalError(test)
	
	# this method will insert a new URL
	def inputUrl(s):# = site):
	        wait(7)
	
	        # simulate keystrokes
	        type(" ",KEY_ALT)
	        wait(2)
	        type("x")
	        wait(3)
	        type("d",KEY_ALT)
	        wait(1)
	
	        # paste in the URL
	        paste(s)           #USES VARIABLE !!!!!!!!!!!!!!!!!!!!!!!!!!
	        type(Key.ENTER)
	
	# this method will create a new directory
	# example: newPath = "C:\\Documents and Settings\\RLevell\\Desktop\\sikuli_test"
	def createDirectory(path):
	        os.makedirs(path)
	
	# this method will open and run fiddler
	def runFiddler(scenario):
	
	        # try to open fiddler
	        try:
				subprocess.call("C:/Program Files/Fiddler2/ExecAction.exe \"sikuli " + scenario +"\"")
				print("wrote " + scenario + " scenario fiddler info to file." )
	
	        # end the test if not opened successfully
	        except FindFailed:
	                criticalError(test)

x = Utilities()
print x.findFaildsLimit # works

#x.getUserAndPass # doesnt work