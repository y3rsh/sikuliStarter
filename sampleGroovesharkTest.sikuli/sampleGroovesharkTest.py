#import these lines to get extra functionality out of Sikuli
from sikuli.Sikuli import *
import os
myPath = os.path.dirname(getBundlePath())
if not myPath in sys.path: sys.path.append(myPath)
from groovesharkTest import *

# instantiate the class where we defined the functionality

g = groovesharkTest()

#use try/except to determine whether a part of the test passed or failed

g.searchForMusic("weezer", " search for single term ")
g.searchForTermsFromDataFile()

# done
print("TEST COMPLETE")
exit()

