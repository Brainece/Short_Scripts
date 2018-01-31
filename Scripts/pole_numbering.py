"""
Define new functions using @qgsfunction. feature and parent must always be the
last args. Use args=-1 to pass a list of values as arguments
"""

from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Custom')
def pole_numberer(r_number,site_string, feature, parent):
	pole_string = ""
	
	if(r_number > 0 and r_number < 10):
		pole_string = site_string + "00" + str(r_number)
	elif (r_number >= 10 and r_number < 100):
		pole_string = site_string + "0" +  str(r_number)
	else:
		pole_string = site_string + str(r_number)
	
	return pole_string
