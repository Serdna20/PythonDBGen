from lines.randomHour import *

def headers(data):
    data = data["data"]
    headers = ""
    if data["linkedLists"]:
        linkedLists = data["linkedLists"]
        for lists in linkedLists:
            headers += lists["name"]+";"

    normalLists = data["normalLists"]
    for lists in normalLists:
        if lists == normalLists[-1]:
            headers += lists["name"]
        else:
            headers += lists["name"]+";"
    return headers

def content(data):
    data = data["data"]
    line = ""
    if data["normalLists"]:
        normalLists = data["normalLists"]
        for lists in normalLists:
            line += checkColumnType(lists)
            print(line)

def checkColumnType(column):
    if column["type"]=="ranTime": 
        # WORKINGGGGG
        return randomTime(column["values"])
    elif column["values"]: 
        return "VALUE"
    elif column["randomInt"]: 
        return "RANDINT"
    elif column["randomDate"]: 
        return "DATE"
    else: return "ERROR"


#from datetime import datetime
#from random import randint

#datetime.date(year, month, day)
#minDate = datetime.strptime('20.12.2016', '%d.%m.%Y')
#maxDate = datetime.strptime('20.12.2024', '%d.%m.%Y')
#minMs = int(minDate.timestamp())
#maxMs = int(maxDate.timestamp())


#dateChosen = randint(minMs, maxMs)
#print(minMs, dateChosen, maxMs)

#print("%s"%datetime.fromtimestamp(dateChosen))
#print(dateChosen.strftime("%d/%m/%y"))