from os.path import exists
from datetime import datetime

def fileExists(name):
    if not exists(name+".csv"):
        return
    return changeName(name)

def changeName(name):
    currentTime = datetime.now()
    currentTime = currentTime.strftime(" %Y_%m_%d %H;%M;%S %p")
    return (name+currentTime)