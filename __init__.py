import json
import os
import time
from datetime import datetime
now = datetime.now()
try:
	import urllib.request
except:
	print("[NetJSON][ERROR/FATAL][" + now.strftime("%H:%M:%S") + "]: Could not import 'urllib'. Please install 'urllib' and try again.")
def loadnetjson(inputurl):
	totaltimestart = time.time()
	tempdir = "NetJSONtmp"
	ppath = os.getcwd()
	path = os.path.join(ppath, tempdir) 
	try:
		os.mkdir(path)
	except:
		print("[NetJSON][INFO][" + now.strftime("%H:%M:%S") + "]: Directory 'NetJSONtmp' already exists.")
	print("[NetJSON][INFO][" + now.strftime("%H:%M:%S") + "]: Started downloading JSON file...")
	starttime = time.time()
	try:
		urllib.request.urlretrieve(inputurl, "NetJSONtmp/main.json")
		endtime = time.time()
		print("[NetJSON][INFO][" + now.strftime("%H:%M:%S") + "]: Sucsess! Downloaded JSON file in " + str(int((endtime - starttime) * 1000)) + "ms")
	except:
		print("[NetJSON][ERROR/FATAL][" + now.strftime("%H:%M:%S") + "]: Failed to download JSON file.")
	print("[NetJSON][INFO][" + now.strftime("%H:%M:%S") + "]: Opening JSON file...")
	file = open("NetJSONtmp/main.json")
	try:
		data = json.load(file)
	except:
		print("[NetJSON][INFO/WARN][" + now.strftime("%H:%M:%S") + "]: An error occured while loading the JSON file. Is the file empty?")
	totaltimeend = time.time()
	print("[NetJSON][INFO][" + now.strftime("%H:%M:%S") + "]: Completed in " + str(int((totaltimeend - totaltimestart) * 1000)) + "ms!")
	return data