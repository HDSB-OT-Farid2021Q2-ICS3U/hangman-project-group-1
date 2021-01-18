import random
import time
import os
from colorama import Fore, Back, Style 



black = "\033[30m"
grey = "\033[90m"
red = "\033[91m"
green = "\033[92m"
orange = "\033[93m"
blue = "\033[94m"
purple = "\033[95m"
lightBlue = "\033[96m"

# @The-Chef123 TODO create the main menu
# @mythos341 TODO make the text stuff work
#Check if the person uses mac/repl or windows for clear statements cls vs clear()

def kill():
    os.abort()

def make_blanks(letters):
    """ takes ammount of letters and displays blanks"""
    global blanks
    blanks = []
    for i in letters:
        blanks.append([i, False])
    """
    for i in range(len(letters)):
        blanks.append('_')
    """
    # return blanks
    
def printBlanks():
    for i in blanks:
        if i[1] == False:
            print('_', end='')
        else:
            print(i[0], end='')
    print()

def stillBlanks():
    areThereStill = [x[1] for x in blanks]
    return False in areThereStill

def stillLetter(playerLetter):
    howMany = [x[0] for x in blanks if x[1] == False]
    return howMany.count(playerLetter) > 0

def checker(letters):
    while stillBlanks():
        """checks for a letter then if it is correct it replaces string"""
        # print(blanks)
        player_input = input('guess a letter: ')
        # print(letters.count(player_input))
        if letters.count(player_input) == 0:
            print('try again')
        else: 
            lastFoundIndex = 0
            while stillLetter(player_input):
                lastFoundIndex = letters.index(player_input, lastFoundIndex)
                blanks[lastFoundIndex][1] = True
                lastFoundIndex += 1
                #print(letters.count(player_input), blanks.count(player_input))
                # index_num = letters.index(player_input)
                # blanks[index_num] = (player_input)
                # letters[index_num] = False
                # print(letters)
                # print('\n')
        printBlanks()
    print('congrats it was: ')
    printBlanks()





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
    time.sleep(1)
    clear()
    print('Loading.')
    time.sleep(1)   
    clear()
    print('Loading..')
    time.sleep(1)   
    clear()
    print('Loading...')
    time.sleep(1)   
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
        time.sleep(0.5)
        print(Style.RESET_ALL) 

        clear()
        print(Fore.YELLOW+ Back.RED + ''.center(310,'|'))
        print(Fore.YELLOW+ Back.RED + 'STICKMAN GAME 1986'.center(310,'|'))
        print(Fore.YELLOW+ Back.RED + ''.center(310,'|'))
        time.sleep(0.5)
        print(Style.RESET_ALL) 

        clear()
        print(Fore.LIGHTMAGENTA_EX+ Back.BLACK + ''.center(310,'\\'))
        print(Fore.LIGHTMAGENTA_EX+ Back.BLACK + 'STICKMAN GAME 1986'.center(310,'\\'))
        print(Fore.LIGHTMAGENTA_EX+ Back.BLACK + ''.center(310,'\\'))   
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




"""
loading()
title()
menu()
"""
# loading()
# title()
randomWord = selectDif(1)
make_blanks(randomWord)
checker(randomWord)
# Put your discord usernames here: Stick#1441, Freddrake 400#0748


"""
word = selectDif(int(input('dificulty: ')))
letters = list(word)
print(make_blanks(letters))
"""
