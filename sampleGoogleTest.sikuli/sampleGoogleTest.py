#import these lines to get extra functionality out of Sikuli
from sikuli.Sikuli import *
import os
myPath = os.path.dirname(getBundlePath())
if not myPath in sys.path: sys.path.append(myPath)

# import util and googleSearch classes to use the scripts from these files
from util import *
from googleSearch import *

# use count to keep track of what iteration the loop is on
# (it doesn't use the first 2 terms of the array - term 0 and 1)
count = 2

# instantiate the util class
u = util()

# instantiate the googleSearch class
g = googleSearch()

	
# use try/except to determine whether a part of the test passed or failed
try:
	# use googleSearch's method "openGoogle" to open Google
	g.openGoogle()
	# if opened correctly pass this section of the test
	# a screenshot is taken and a log file is updated with a "passed"
	u.passed("openGoogle")
except FindFailed:
	# a screenshot is taken and a log file is updated with a "failed"
	u.failed("openGoogle")
	
# search all the terms in the testdata array by using a while loop
# (len = find the length of the array)
while(count < len(u.termsArr)):

	try:
		# select Google's search box
		g.selectSearchBox()
		u.passed("selectSrchBox")
	except FindFailed:
		u.failed("selectSrchBox")

	try:
		# type in one term from the array into the search box
		g.typeInSearchBox(u.termsArr[count])
		u.passed("typeSrchBox")
	except FindFailed:
		u.failed("typeSrchBox")

	try:
		# search google
		g.searchGoogle()
		u.passed("srchGoogle")
	except FindFailed:
		u.failed("srchGoogle")

		# take a screenshot of the search results
		# the image is saved in the logs folder under a timestamp
		u.captureMyScreen("googleSearch",u.timeStamp())

	try:
		# go back to Google's homepage
		g.googleHome()
		u.passed("googleHome")
	except FindFailed:
		u.failed("googleHome")
		
		# increment the count to get the next term in the array
		# or to end the loop
	count = count+1

# close the browser
u.closeBrowser()

# test is over
print "TEST COMPLETE"
	


