#!/usr/bin/python

import requests
from time import sleep
from sys import exit

names = {}
while True:
	try:
		r = requests.get('https://mcprohosting.com/api/name')
		names[r.text] = ''
	except KeyboardInterrupt:
		with open('names.txt','w') as FILE:
			FILE.write(str(len(names.keys())) + "\n")
			for value in names.keys():
				FILE.write(value + "\n")
			exit(0)
