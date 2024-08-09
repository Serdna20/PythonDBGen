import json
from fileManagement.file import fileExists
# Loads the required data
data = json.load(open('data copy.json'))["newFileData"]

# True -> Creates a new file, False -> May cause data lost
changeFileName = True

# Creates the file

if changeFileName:
    fileName = fileExists(data["name"])
else:
    fileName = data["name"]

newFile = open((fileName+".csv"), 'w')
newFile.close()
