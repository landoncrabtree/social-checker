from itertools import cycle
import requests

with open("proxies.txt", "r+") as f:
	proxies = [x.strip() for x in f.readlines()]
proxy_pool = cycle(proxies)

"""
This code is licensed under QPL-1.0.

You CAN:
- Distribute
- Modify

You CANNOT:
- Commercial Use

You MUST:
- Include copyright
- Include license
- Disclose source

Source code can be found here:
https://git.landon.pw/r/social-checker
"""

def getWorkingProxy():
	proxy = next(proxy_pool)
	try:
		requests.get("http://ipinfo.io/json", proxies={"http": "http://"+proxy}, timeout=5)
		return proxy
	except Exception as e:
		return getWorkingProxy()
