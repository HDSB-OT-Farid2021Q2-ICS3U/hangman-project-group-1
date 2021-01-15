import random
import os
# @The-Chef123 TODO create the main menu
# #mythos341 TODO make the text stuff work

def kill():
    os.abort()


def selectDif(difNum): #1=easy, 2=medium, 3=hard
    if difNum == 1:
        words = open('easy.txt', 'rt')
    elif difNum == 2:
        words = open('medium.txt', 'rt')
    elif difNum == 3:
        words = open('hard.txt', 'rt')
    else:
        print(f'You tried to select difficulty {difNum}')# What if they enter '2     '  IDK prolly be fine
        kill()
    wordChoice = random.randrange(0, len(list(words)))
    words.close()
    words = open('easy.txt', 'rt')
    for i, line in enumerate(words):
        if i == wordChoice:
            words.close()
            return line.strip('\n')





