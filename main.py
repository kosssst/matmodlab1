import subprocess
from threading import Thread
import json
import time

keyfile = open("processes.json", 'r')
data = json.load(keyfile)

def start(name, file, xl, yl):
	subprocess.call("python model_builder.py " + str(name) + " " + str(file) + " " + str(xl) + " " + str(yl), shell=True)

if __name__ == "__main__":
    for i in data:
        Thread(target = start, args = (i["name"], i["data"], i["x-label"], i["y-label"])).start()
        time.sleep(1)