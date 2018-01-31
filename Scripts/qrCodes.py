"""This is a short script that downloads qr_codes generated using google charts and stores them in disk as .png files
with the name of the file being a five digit customer account number. The qr_code links should be provided as a .txt file.

"""

import urllib
import re

#create a regex object to search the qr_code donload link for the five digit account number
account_re = re.compile(r'\d{5}')

# Open the .txt containing the download links and read its contents
with open('remainder.txt') as file_object:
	lines = file_object.readlines()

for line in lines:
	if(account_re.search(line)==None):
		print("No matches found")
	else:
		mo = account_re.search(line)
		name = mo.group()


		#download the qr_code and save it as a .png file
		urllib.urlretrieve(line,name + ".png")
	
	#qrImg = urlopen(line)
