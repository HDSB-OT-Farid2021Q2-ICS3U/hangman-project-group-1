import random
import time
import os
import sys
import msvcrt
import tkinter # for some reason it need both imports of tkinter
from colorama import Fore, Back, Style 
from tkinter import*

black = "\033[30m"
grey = "\033[90m"
red = "\033[91m"
green = "\033[92m"
orange = "\033[93m"
blue = "\033[94m"
purple = "\033[95m"
lightBlue = "\033[96m"
global triedChars
triedChars = []
man = [[100,450,100,75], [100,75,250,75], [250,75,250,100], [200,200,300,100], [250,200,250,300], [250,300,350,400], [250,300,150,400], [250,250,150,250], [250,250, 350,250],[250,250, 350,250]]

def create_canvas():
    global canvas
    canvas = Canvas(window, width=500, height=500, bg= 'black')
    canvas.pack()

window = Tk()# make the window
window.attributes('-topmost', True)
window.title('HANGMAN')
the_word = StringVar()
the_word.set('SELECT DIFFICULTY FIRST')
label = Label(window, textvariable=the_word, font=16) # Create top Label
label.place(height=40, width= 500)
label.pack()

string_var = StringVar()
string_var.set('')
label_tries = Label(window, font=(16), textvariable = string_var)
userInput = Entry(window)
userInput.pack(side=BOTTOM)
label_tries.pack(side=BOTTOM)


def restart_program():
    """Restarts the current program."""
    window.destroy()
    os.system('py main.py')


restart_button = Button(window, text='RESTART', command=restart_program)
restart_button.pack(side=TOP)




def kill():
    window.destroy()
    time.sleep(2)
    os.abort()

def make_blanks(hangmanWord):
    """ takes ammount of hangmanWord and displays blanks"""
    global blanks
    blanks = []
    for i in hangmanWord:
        if ' ' == i:
            blanks.append([i, True])
        else:
            blanks.append([i, False])
    """
    for i in range(len(hangmanWord)):
        blanks.append('_')
    """
    # return blanks
    
def printBlanks():
    """Returns the string of the players progress"""
    userProgress = ''
    for i in blanks:
        if i[1] == False:
            userProgress += '_ '
        else:
            userProgress += f'{i[0]}'
    return userProgress

def stillBlanks():
    """Checks if there are still undiscovered letters"""
    areThereStill = [x[1] for x in blanks]
    return False in areThereStill

def stillLetter(playerLetter):
    """Checks if there are any undescovered of a certain character"""
    howMany = [x[0] for x in blanks if x[1] == False]
    return howMany.count(playerLetter) > 0

def checker(hangmanWord, player_input):
    # while stillBlanks():
    """checks for a letter then if it is correct it replaces string"""
    if hangmanWord.count(player_input) == 0:
        print('try again')
        return False
    else: 
        lastFoundIndex = 0
        while stillLetter(player_input):
            lastFoundIndex = hangmanWord.index(player_input, lastFoundIndex)
            blanks[lastFoundIndex][1] = True
            lastFoundIndex += 1
        return True

def formatedTriedChars():
    noRepeats = sorted(triedChars)
    noRepeats = list(dict.fromkeys(noRepeats))
    noRepeats = [i for i in noRepeats if i not in [x[0] for x in blanks]]
    return noRepeats

def getPlayerInput():
    while True:
        usr = input('Choose a character: ')
        if bool(usr) == False:
            print('You must enter a character')
        elif len(usr) > 1:
            print('You can only enter one character')
        elif usr in triedChars:
            print(f'You have already tried "{usr}"')
        else:
            triedChars.append(usr)
            return usr

def selectDif(difNum): #1=easy, 2=medium, 3=hard
    """enter difficullty, returns word(s) of that difficulty"""
    if difNum == 1:
        wordDict = 'easy.txt'
        words = open(wordDict, 'rt')
    elif difNum == 2:
        wordDict = 'medium.txt'
        words = open(wordDict, 'rt')
    elif difNum == 3:
        wordDict = 'hard.txt'
        words = open(wordDict, 'rt')
    else:
        print(f'You tried to select difficulty {difNum}')
        kill()
    wordChoice = random.randrange(0, len(list(words)))
    words.close()
    words = open(wordDict, 'rt')
    for i, line in enumerate(words):
        if i == wordChoice:
            words.close()
            return line.strip('\n')

def loading():
    counterOne = 0
    clear = lambda: os.system('cls')
    clear()
    print('Loading')
    time.sleep(0.5)
    clear()
    print('Loading.')
    time.sleep(0.5)   
    clear()
    print('Loading..')
    time.sleep(0.5)   
    clear()
    print('Loading...')
    time.sleep(0.5)   
    clear()
    while counterOne != 3:
        counterOne += 1
        print('System Requirements Met')
        time.sleep(1)
        clear()
        time.sleep(0.5)


def title():

    counterTwo = 0
    while counterTwo != 3:
        clear = lambda: os.system('cls')
        print(Fore.RED+ Back.YELLOW + ''.center(275,'/'))
        print(Fore.RED+ Back.YELLOW + 'STICKMAN GAME 1986'.center(275,'/'))
        print(Fore.RED+ Back.YELLOW + ''.center(275,'/'))
        if msvcrt.kbhit():
            print(Style.RESET_ALL)
            break
        time.sleep(0.5)
        print(Style.RESET_ALL)
         

        clear()
        print(Fore.YELLOW+ Back.RED + ''.center(275,'|'))
        print(Fore.YELLOW+ Back.RED + 'STICKMAN GAME 1986'.center(275,'|'))
        print(Fore.YELLOW+ Back.RED + ''.center(275,'|'))
        if msvcrt.kbhit():
            print(Style.RESET_ALL)
            break
        time.sleep(0.5) 
        print(Style.RESET_ALL)

        clear()
        print(Fore.LIGHTMAGENTA_EX+ Back.BLACK + ''.center(275,'\\'))
        print(Fore.LIGHTMAGENTA_EX+ Back.BLACK + 'STICKMAN GAME 1988'.center(275,'\\'))
        print(Fore.LIGHTMAGENTA_EX+ Back.BLACK + ''.center(275,'\\'))   
        if msvcrt.kbhit():
            print(Style.RESET_ALL)
            break
        time.sleep(0.5)
        print(Style.RESET_ALL)

        clear()

def getPlayerChoice():
    while True:
        playerIn = input('What is your choice: ')
        if playerIn.isnumeric() == False:
            print('Your choice must be a number between 1-4')
        elif int(playerIn) == 4:
            kill()
        elif int(playerIn) < 1 or int(playerIn) > 3:
            print('Your choice is not in the range 1-4')
        else:
            try:
                return int(playerIn)
            except:
                pass

def menu():
    """Prints the main menu"""
    print(Fore.RED + ''.center(275, '-').center(1, '|'))
    print('Stickman 1986'.center(275, '-').center(1, '|'))
    print(Fore.RED + ''.center(275, '-').center(1, '|'))
    print('CHOOSE YOUR DIFFICULTY'.center(275, '-').center(1, '|'))
    print('1. | I dont like challenge'.center(275, '-').center(1, '|'))
    print('2. | You want a challenge but you dont want to look bad'.center(275, '-').center(1, '|'))
    print('3. | The obvious choice'.center(275, '-').center(1, '|'))
    print(Fore.RED + ''.center(275, '-').center(1, '|'))
    print('4. | Had Enough?'.center(275, '-').center(1, '|'))
    print(Fore.RED + ''.center(275, '-').center(1, '|'))
    print(Style.RESET_ALL) 

def loss(lost_turns):
    """draws stickman from list of moves sequencially per lost turn"""
    if lost_turns == 0:
        return
    if lost_turns > 3:
        wide = 5
        col = 'white'
    else: 
        wide = 10
        col = 'saddlebrown'

    if lost_turns != 4:
        canvas.create_line(man[lost_turns - 1], fill = col, width = wide)  
        print(lost_turns)
        print(man[lost_turns])
    else:
        canvas.create_oval(man[lost_turns - 1], fill = col, width = wide)
    
    string_var.set(formatedTriedChars()) #assuming tried chars is list of incorect
    window.update()



"""
loading()
title()
menu()
"""
"""
randomWord = selectDif(2)
make_blanks(randomWord)
while stillBlanks():
    print(printBlanks())
    checker(randomWord, getPlayerInput())
print(f'congrats it was: {randomWord}')
"""
"""
for i in range (9):   #this is a test of gui
    letter = input('temporary replacement for where false letter input: ')
    triedChars.append(letter)
    loss(i)
print(triedChars)
"""
loading()
title()
os.system('cls')
menu()
usrDiffi = getPlayerChoice()
randomWord = selectDif(usrDiffi)
# time.sleep(5)
# randomWord = 'i know this word'
make_blanks(randomWord)
livesLost = 0
while livesLost < 10:
    the_word.set(printBlanks())
    loss(livesLost)
    recent = ''
    while bool(recent) == False:
        recent = userInput.get()
        time.sleep(0.01)
        window.update()
    userInput.delete(0, tkinter.END)
    recent = recent[0].lower()
    if checker(randomWord, recent):
        pass
    elif recent.isalpha() == False:
        print('No numbers/special characters')
    elif recent in triedChars:
        print('You have already tried that letter')
        print(triedChars)
    else:
        triedChars.append(recent)
        livesLost += 1
    if stillBlanks() == False:
        win = True
else:
    win = False

if win:
    string_var = 'YOU WIN!!!'
else:
    string_var = 'YOU LOSE'
    the_word = 'The word was: ' + randomWord

    


