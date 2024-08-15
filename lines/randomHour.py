import random
import datetime

def timeSeconds(timeFormat):
    timeConversion = [3600, 60, 1]
    seconds = 0
    for i in range(0, 2):
        seconds += timeFormat[i] * timeConversion[i]
    return seconds

def randomTime(limits):
    minT, maxT = list(map(int, limits[0].split(":"))), list(map(int, limits[1].split(":")))
    minSec, maxSec = timeSeconds(minT), timeSeconds(maxT)
    return str(datetime.timedelta(seconds=random.randint(minSec, maxSec)))
    
# randomTime(["00:20:10", "00:30:45"])