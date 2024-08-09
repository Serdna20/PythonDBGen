import json
from fileManagement.file import fileExists
from lines.lines import headers

# Loads the required data
data = json.load(open('data.json'))["newFileData"]

# True -> Creates a new file, False -> May cause data lost
changeFileName = True

# Creates the file

if changeFileName:
    fileName = fileExists(data["name"])
else:
    fileName = data["name"]

newFile = open((fileName+".csv"), 'a')
newFile.write(headers(data))




newFile.close()