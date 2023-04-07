#!/usr/bin/python3
""" I document """

import sys
from urllib.request import urlopen, Request

if __name__ == "__main__":
	req = Request(argv[1])
	
	with urlopen(req) as res:
		content = res.read()
		print(res.getheader('X-Request-Id'))
