#!/usr/bin/python3
#0-hbtn_status.py
"""0-hbtn_status.py"""

from urllib.request import Request, urlopen

req = Request('https://alu-intranet.hbtn.io/status')

with urlopen(req) as res:
	content = res.read()
	print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode("utf-8")))
