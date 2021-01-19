import random
import time
import os
import msvcrt
from colorama import Fore, Back, Style 
from tkinter import*
window =Tk()
man = [[100,400,100,75], [100,75,250,75], [250,75,250,100], [200,200,300,100], [250,200,250,300], [250,300,350,400], [250,300,150,400], [250,250,150,250], [250,250, 350,250]]

def create_canvas():
    global canvas
    global label
    canvas = Canvas(window, width=500, height=500, bg= 'black')
    canvas.pack()
    label = Label(window, text="This is where the stickman will be drawn")
    label.place(height=40, width= 500)

    window.title('HANGMAN')

create_canvas()

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
# @The-Chef123 TODO create the main menu
# @mythos341 TODO make the text stuff work
#Check if the person uses mac/repl or windows for clear statements cls vs clear()

def kill():
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
    else: 
        lastFoundIndex = 0
        while stillLetter(player_input):
            lastFoundIndex = hangmanWord.index(player_input, lastFoundIndex)
            blanks[lastFoundIndex][1] = True
            lastFoundIndex += 1

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
        print(f'You tried to select difficulty {difNum}')# What if they enter '2     '  IDK prolly be fine
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
        print(Fore.RED+ Back.YELLOW + ''.center(310,'/'))
        print(Fore.RED+ Back.YELLOW + 'STICKMAN GAME 1986'.center(310,'/'))
        print(Fore.RED+ Back.YELLOW + ''.center(310,'/'))
        if input() != None:
            break
        time.sleep(0.5)
        print(Style.RESET_ALL) 

        clear()
        print(Fore.YELLOW+ Back.RED + ''.center(310,'|'))
        print(Fore.YELLOW+ Back.RED + 'STICKMAN GAME 1986'.center(310,'|'))
        print(Fore.YELLOW+ Back.RED + ''.center(310,'|'))
        if input() != None:
            break
        time.sleep(0.5)
        print(Style.RESET_ALL) 

        clear()
        print(Fore.LIGHTMAGENTA_EX+ Back.BLACK + ''.center(310,'\\'))
        print(Fore.LIGHTMAGENTA_EX+ Back.BLACK + 'STICKMAN GAME 1986'.center(310,'\\'))
        print(Fore.LIGHTMAGENTA_EX+ Back.BLACK + ''.center(310,'\\'))   
        if input() != None:
            break
        time.sleep(0.5)
        print(Style.RESET_ALL) 

        clear()


"""=======
        counterTwo += 1"""


def menu():
    print(Fore.RED + ''.center(310, '-').center(1, '|'))
    print('Stickman 1986'.center(310, '-').center(1, '|'))
    print(Fore.RED + ''.center(310, '-').center(1, '|'))
    print('CHOOSE YOUR DIFFICULTY'.center(310, '-').center(1, '|'))
    print('1. | I dont like challenge'.center(310, '-').center(1, '|'))
    print('2. | You want a challenge but you dont want to look bad'.center(310, '-').center(1, '|'))
    print('3. | The obvious choice'.center(310, '-').center(1, '|'))
    print(Fore.RED + ''.center(310, '-').center(1, '|'))
    print('4. | Had Enough?'.center(310, '-').center(1, '|'))
    print(Fore.RED + ''.center(310, '-').center(1, '|'))
    print(Style.RESET_ALL) 



def loss(lost_turns):
    if lost_turns > 2:
        wide = 5
        col = 'white'
    else: 
        wide = 10
        col = 'saddlebrown'

    if lost_turns != 3:
        canvas.create_line(man[lost_turns], fill = col, width = wide)  
        print(lost_turns)
        print(man[lost_turns])
    else:
        canvas.create_oval(man[lost_turns], fill = col, width = wide)
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
loss(2)
# Put your discord usernames here: Stick#1441, Freddrake 400#0748

#this should be the very last part of the code. V
window.mainloop()
