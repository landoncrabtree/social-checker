from itertools import cycle
import requests

with open("proxies.txt", "r+") as f:
	proxies = [x.strip() for x in f.readlines()]
proxy_pool = cycle(proxies)


def getWorkingProxy():
	proxy = next(proxy_pool)
	try:
		r = requests.get("http://ipinfo.io/json", proxies={"http": "http://"+proxy, "https": "https://"+proxy}, timeout=5)
		return proxy
	except Exception as e:
		#proxies.remove(proxy)
		#proxy_pool.__setattr__(proxy, None)
		return getWorkingProxy()
