import string

from randomIndex import *

def randomString(amount):
    stringList = []

    # Create two random strings
    for i in range(0, amount):
        
        # NO DUPLICATES
        randomString = (randomLetter()+randomLetter())
        while randomString in stringList:
            randomString = (randomLetter()+randomLetter())
            
        stringList.append(randomString)
        
    return stringList
    

def randomLetter():
    return randomIndex(string.ascii_lowercase)

print(randomLetter())