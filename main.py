import json
from fileManagement.file import fileExists
from lines.lines import headers, content

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

for i in range(0, data["lines"]):
    content(data)



newFile.close()