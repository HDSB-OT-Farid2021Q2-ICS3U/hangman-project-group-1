import random
import time
import os

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

i = 1


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









def menu():
    while i != 0:
        clear = lambda: os.system('cls')
        print('\033[1;33;41m//////////////////////////////////////////////\033[1;33;41m')
        print('\033[1;33;41mStickman Game \033[2;33;41m'.center(20))
        print('\033[1;33;41m//////////////////////////////////////////////\033[1;33;41m')


        time.sleep(1)





        clear()
        #print('"\031[1;33;43m [\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\]')
        print('\033[1;33;41m/|||||||||||||||||||||||||||||||||||||||||||||\033[1;33;41m')
        print('\033[1;33;41mStickman Game \033[2;33;41m'.center(20))
        print('\033[1;33;41m|||||||||||||||||||||||||||||||||||||||||||||\033[1;33;41m')
        time.sleep(1)
        clear()

print(make_blanks((selectDif(int(input('dificulty: '))))))