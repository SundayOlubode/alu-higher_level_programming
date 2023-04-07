#!/usr/bin/python3
#0-hbtn_status.py

from urllib.request import Request, urlopen

req = Request('https://alu-intranet.hbtn.io/status')
with urlopen(req) as res:
	resBody = res.read()
	print(resBody)
