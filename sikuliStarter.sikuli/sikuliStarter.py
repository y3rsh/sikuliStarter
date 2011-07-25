from sikuli.Sikuli import *
 # works on all platforms
import os
import re
# get the directory containing your running .sikuli
myPath = os.path.dirname(getBundlePath())
if not myPath in sys.path: sys.path.append(myPath)

# now you can import every .sikuli in the same directory
#import util
from util import *
u = util()
paste(u.termsArr[0])
