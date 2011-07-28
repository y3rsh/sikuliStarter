#import these lines to get extra functionality out of Sikuli
from sikuli.Sikuli import *
import os
myPath = os.path.dirname(getBundlePath())
if not myPath in sys.path: sys.path.append(myPath)

# import util and googleSearch classes to use the scripts from these files
from util import *
from groovesharkTest import *

# instantiate the classes
u = util()
g = groovesharkTest()
# this class is imported from grooveSharkTest so it didn't need imported again
i = groovesharkTestImages()

# to iterate through the terms and end the loop when out of terms
count = 2

# use try/except to determine whether a part of the test passed or failed
try:
	# open the music player GrooveShark
	g.openGrooveshark()
	# if opened correctly pass this section of the test
	# a screenshot is taken and a log file is updated with a "passed"
	u.passed("openGrooveshark")
# if an image was not found by Sikuli then catch the exception
# and fail the test
except FindFailed:
	# a screenshot is taken and a log file is updated with a "failed"
	u.failed("openGrooveshark")

try:
	# log into the application using the first 2 terms of the testdata array
	# which are valid credentials for this site
	g.login(u.termsArr[0],u.termsArr[1])
	u.passed("login")
except FindFailed:
	u.failed("login")

try:
	# click the favorites tab
	g.clickFavorites()
	u.passed("favorites")
except FindFailed:
	u.failed("favorites")

try:
	# play all of the songs in the favorites playlist
	g.playAll()
	u.passed("playAll")
except FindFailed:
	u.failed("playAll")

try:
	# see all the music that has been added
	g.seeAllMusic()
	u.passed("allMusic")
except FindFailed:
	u.failed("allMusic")

try:
	# add a song to the playlist
	g.addSong(i.getImage("unwellSong"))
	u.passed("addSong")
	wait(2)
except FindFailed:
	u.failed("addSong")

# start loops to search for new artists
while(count < len(u.termsArr)):
	try:
		# use terms from the testdata array
		g.searchForMusic(u.termsArr[count])
		u.passed("searchMusic")
	except FindFailed:
		u.failed("searchMusic")

	try:
		# play all from the artist that is searched
		g.playAll()
		u.passed("playAll")
	except FindFailed:
		u.failed("playAll")

	# increment count iterate over the terms and end the loop
	count = count + 1

# listen to a song for 10 seconds
wait(10)

try:
	# clear the playlist
	g.clearPlaylist()
	u.passed("clearList")
except FindFailed:
	u.failed("clearList")

try:
	# log out of the application
	g.logoutGrooveshark()
	u.passed("logout")
except FindFailed:
	u.failed("logout")

	g.closeGrooveshark()
	u.passed("close")

# done
print "TEST COMPLETE"