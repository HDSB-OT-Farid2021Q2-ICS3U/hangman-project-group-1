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

def kill():
    os.abort()

def make_blanks(letters):
    """ takes ammount of letters and displays blanks"""
    global blanks
    blanks = []
    for i in range(len(letters)):
        blanks.append('_')
    
    return blanks
    


def checker():
    while blanks.count('_') > 0:
        """checks for a letter then if it is correct it replaces string"""
        print(blanks)
        player_input = input('guess a letter: ')
        print(letters.count(player_input))
        if letters.count(player_input) == 0:
            print('try again')
        else: 
            while letters.count(player_input) >= blanks.count(player_input):
                #print(letters.count(player_input), blanks.count(player_input))
                index_num = letters.index(player_input)
                blanks[index_num] = (player_input)
                letters[index_num] = False
                print(letters)
                print('\n')
    
    print('congrats it was', blanks)





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
        time.sleep(1.5)
        print(Style.RESET_ALL) 

        clear()
        print(Fore.YELLOW+ Back.RED + ''.center(310,'|'))
        print(Fore.YELLOW+ Back.RED + 'STICKMAN GAME 1986'.center(310,'|'))
        print(Fore.YELLOW+ Back.RED + ''.center(310,'|'))
        time.sleep(1.5)
        print(Style.RESET_ALL) 

        clear()
        print(Fore.LIGHTMAGENTA_EX+ Back.BLACK + ''.center(310,'\\'))
        print(Fore.LIGHTMAGENTA_EX+ Back.BLACK + 'STICKMAN GAME 1986'.center(310,'\\'))
        print(Fore.LIGHTMAGENTA_EX+ Back.BLACK + ''.center(310,'\\'))   
        time.sleep(1.5)
        print(Style.RESET_ALL) 

        clear()


print(make_blanks((selectDif(int(input('dificulty: '))))))
"""=======
        counterTwo += 1
"""

loading()
title()