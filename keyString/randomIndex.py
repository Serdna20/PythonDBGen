import random

def randomIndex(element):
    randomIndex = random.randint(0, len(element)-1)
    return element[randomIndex]