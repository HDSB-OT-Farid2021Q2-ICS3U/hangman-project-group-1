

def makeBlanks():
    global blanks 
    blanks = [['c', True],['o', True],['a', True],['t', True]]

def stillLetter(playerLetter):
    howMany = [x[0] for x in blanks if x[1] == False]
    return howMany.count(playerLetter) > 0

def stillBlanks():
    areThereStill = [x[1] for x in blanks]
    return False in areThereStill


makeBlanks()
print(stillBlanks())