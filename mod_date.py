# Giovani Granzotto Oliani
# 21/04/2018
# Small script that iterates through a folder changing 
# the files' modification date to that specified in the
# first line (date format dd/mm/yyy)

import sys
import datetime
import os
import calendar

if len(sys.argv) < 2:
	print "Usage: python mod_date.py [folder_name]"
	exit(1)

for filename in os.listdir(sys.argv[1]):
	file = open(sys.argv[1] + filename, "r")
	data = file.readline()
	file.close()
	data = data.split("/")
	seconds = calendar.timegm(datetime.datetime(int(data[2]), int(data[1]), int(data[0]), 0, 0).timetuple())
	os.utime(sys.argv[1] + filename, (seconds,seconds))

