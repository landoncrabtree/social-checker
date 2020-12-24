from multiprocessing import Pool
from requests.packages.urllib3.util.retry import Retry
import requests
from proxy import getWorkingProxy
requests.packages.urllib3.disable_warnings()


def request(line):
	#proxy = getWorkingProxy()
	#proxies = {
	#	"http": "http://" + proxy,
	#	"https": "https://" + proxy
	#}
	url = "https://steamcommunity.com/id/"
	user = line.strip()
	headers = {
		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
	}
	try:
		r = requests.get(url + user, headers=headers, verify=False)
		status = r.text
		if ("The specified profile could not be found." in status):
			print(f"{user} is available.")
			file = open("available.txt", "a")
			file.write(url + user + "\n")
			file.close()
		else:
			print(f"{user} is taken.")
	except Exception as e:
		print(f"Connection Error: {user}. Retrying.")
		request(user)


if __name__ == '__main__':
	print("Checking Steam names... No proxies needed.")
	filename = input("What is the filename?: ")
	usernames = open(f"wordlist/{filename}")
	pool = Pool(processes=100)
	lines = usernames.readlines()
	results = pool.map(request, lines)
