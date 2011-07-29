#import these lines to get extra functionality out of Sikuli
from sikuli.Sikuli import *
import os
myPath = os.path.dirname(getBundlePath())
if not myPath in sys.path: sys.path.append(myPath)

# import util and googleSearch classes to use the scripts from these files
from util import *
from groovesharkTest import *

# instantiate the classes

g = groovesharkTest()
# this class is imported from grooveSharkTest so it didn't need imported again
i = groovesharkTestImages()

# to iterate through the terms and end the loop when out of terms
count = 2

# use try/except to determine whether a part of the test passed or failed
try:
	# open the music player GrooveShark
	g.openFirefox()
	g.inputUrl("http://grooveshark.com/")
	wait(7)
	# if opened correctly pass this section of the test
	# a screenshot is taken and a log file is updated with a "passed"
	g.passed("openGrooveshark")
# if an image was not found by Sikuli then catch the exception
# and fail the test
except FindFailed:
	# a screenshot is taken and a log file is updated with a "failed"
	g.failed("openGrooveshark")

try:
	# log into the application using the first 2 terms of the testdata array
	# which are valid credentials for this site
	g.login(g.termsArr[0],g.termsArr[1])
	g.passed("login")
except FindFailed:
	g.failed("login")

try:
	# click the favorites tab
	g.clickFavorites()
	g.passed("favorites")
except FindFailed:
	g.failed("favorites")

try:
	# play all of the songs in the favorites playlist
	g.playAll()
	g.passed("playAll")
except FindFailed:
	g.failed("playAll")

try:
	# see all the music that has been added
	g.seeAllMusic()
	g.passed("allMusic")
except FindFailed:
	g.failed("allMusic")

try:
	# add a song to the playlist
	g.addSong(i.getImage("unwellSong"))
	g.passed("addSong")
	wait(2)
except FindFailed:
	g.failed("addSong")

# start loops to search for new artists
while(count < len(g.termsArr)):
	try:
		# use terms from the testdata array
		g.searchForMusic(g.termsArr[count])
		g.passed("searchMusic")
	except FindFailed:
		g.failed("searchMusic")

	try:
		# play all from the artist that is searched
		g.playAll()
		g.passed("playAll")
	except FindFailed:
		g.failed("playAll")

	# increment count iterate over the terms and end the loop
	count = count + 1

# listen to a song for 10 seconds
wait(10)

try:
	# clear the playlist
	g.clearPlaylist()
	g.passed("clearList")
except FindFailed:
	g.failed("clearList")

try:
	# log out of the application
	g.logoutGrooveshark()
	g.passed("logout")
except FindFailed:
	g.failed("logout")

g.closeBrowser()
g.passed("close")
# done
print("TEST COMPLETE")
exit()

