import random
import time
import os
import msvcrt
import tkinter # for some reason it need both imports of tkinter
from colorama import Fore, Back, Style 
from tkinter import*
from platform   import system as system_name  # Returns the system/OS name

# @The-Chef123 TODO create the main menu
# @mythos341 TODO make the text stuff work

global triedChars # A list holding all of the tried characters
triedChars = []
man = [[100,450,100,75], [100,75,250,75], [250,75,250,100], [200,200,300,100], [250,200,250,300], [250,300,350,400], [250,300,150,400], [250,250,150,250], [250,250, 350,250],[250,250, 350,250]] # coordinates for how to draw the hangman

def create_canvas():
    """Creates a canvas in the tkinter window"""
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
create_canvas()
string_var = StringVar()
string_var.set('TRIED CHARACTERS')
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
    """Closes the window and exits the program"""
    window.destroy()
    clear_screen()
    os.abort()

def make_blanks(hangmanWord):
    """Makes a blanks list from a word"""
    global blanks
    blanks = []
    for i in hangmanWord:
        if ' ' == i:
            blanks.append([i, True])
        else:
            blanks.append([i, False])
    
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
    """checks for a letter then if it is correct it makes the required changes to blanks"""
    if hangmanWord.count(player_input) == 0:
        return False
    else: 
        lastFoundIndex = 0
        while stillLetter(player_input):
            lastFoundIndex = hangmanWord.index(player_input, lastFoundIndex)
            blanks[lastFoundIndex][1] = True
            lastFoundIndex += 1
        return True

def formatedTriedChars():
    """returns an ordered, duplicate free formated string of the tried characters list"""
    noRepeats = sorted(triedChars)
    noRepeats = list(dict.fromkeys(noRepeats))
    noRepeats = [i for i in noRepeats if i not in [x[0] for x in blanks]]
    return ' '.join(noRepeats)

def selectDif(difNum): #1=easy, 2=medium, 3=hard
    """enter difficullty, returns word(s) of that difficulty"""
    print('Game Started\n')
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
    """Print out the loading animation"""
    counterOne = 0 #Counter variable used for loop
    counterTwo = 0 #Second counter variable used for loop

    #Display loading screen with the number of dots increasing each loop.
    while counterOne != 3: 
        print('Loading' + '.' * counterOne)
        time.sleep(0.5)
        counterOne += 1
        clear_screen()
    
    #Flashes 'System Requirements Met' 3 times quickly.
    while counterTwo != 3:
        counterTwo += 1
        print('System Requirements Met')
        time.sleep(0.5)
        clear_screen()
        time.sleep(0.5)

def clear_screen():
    """Clears the terminal screen."""
    # Clear screen command as function of OS
    command = 'cls' if system_name().lower()=='windows' else 'clear'# makes sure that it uses the right command depending on operating system
    # Action
    os.system(command)

def title():
    """Prints the changing title screen in a loop until ente key is pressed"""

    
    while True:#Loops title screen until key is pressed.

        print(Fore.RED+ Back.YELLOW + ''.center(275,'/')) #Prints menu screen with a yellow background and a red font colour
        print(Fore.RED+ Back.YELLOW + 'STICKMAN GAME 1988'.center(275,'/'))
        print(Fore.RED+ Back.YELLOW + ''.center(275,'/'))

        if msvcrt.kbhit(): #Checks to see if a key has been pressed and ends the function/loop if it has
            print(Style.RESET_ALL)
            break


        time.sleep(0.5)#Delay the continuation for the program for 5 miliseconds
        print(Style.RESET_ALL)#Resets the style of the text in the terminal to the original setting
        clear_screen()#Calls the clear_screen() function*


        print(Fore.YELLOW+ Back.RED + ''.center(275,'|'))#Prints menu screen with a red background and a yellow font colour
        print(Fore.YELLOW+ Back.RED + 'Press Enter'.center(275,'|'))
        print(Fore.YELLOW+ Back.RED + ''.center(275,'|'))

        if msvcrt.kbhit():
            print(Style.RESET_ALL)
            break

        time.sleep(0.5) 
        print(Style.RESET_ALL)
        clear_screen()

        print(Fore.LIGHTMAGENTA_EX+ Back.BLACK + ''.center(275,'\\'))#Prints menu screen with a black background and a light magenta font colour
        print(Fore.LIGHTMAGENTA_EX+ Back.BLACK + 'STICKMAN GAME 1988'.center(275,'\\'))
        print(Fore.LIGHTMAGENTA_EX+ Back.BLACK + ''.center(275,'\\'))   

        if msvcrt.kbhit():
            print(Style.RESET_ALL)
            break

        time.sleep(0.5)
        print(Style.RESET_ALL)
        clear_screen()

def getPlayerChoice():
    """Gets the player to choose a number between 1 and 4"""
    while True:
        playerIn = input('What is your choice: ')#Asks for what function the user would like to select.

        if playerIn.isnumeric() == False: #Checks to make sure that the user inputted a number 
            print('Your choice must be a number between 1-4')
        elif int(playerIn) == 4: #If the user selects function 4, the kill function will be called
            kill()
        elif int(playerIn) < 1 or int(playerIn) > 3: #Checks to see if the number inputted is within the range of the menu
            print('Your choice is not in the range 1-4')
        else:
            try:
                return int(playerIn) 
            except:
                pass

def menu():
    """Prints the main menu"""
    print(Fore.RED + ''.center(275, '-').center(1, '|'))#Main menu printed with the font being red and centered with '-'.
    print('Stickman 1986'.center(275, '-').center(1, '|'))
    print(Fore.RED + ''.center(275, '-').center(1, '|'))
    print('CHOOSE YOUR DIFFICULTY'.center(275, '-').center(1, '|'))
    print('1. Easy | I dont like challenge'.center(275, '-').center(1, '|'))
    print('2. Medium | You want a challenge but you dont want to look bad'.center(275, '-').center(1, '|'))
    print('3. Hard | The obvious choice'.center(275, '-').center(1, '|'))
    print(Fore.RED + ''.center(275, '-').center(1, '|'))
    print('4. Exit | Had Enough?'.center(275, '-').center(1, '|'))
    print(Fore.RED + ''.center(275, '-').center(1, '|'))
    print(Style.RESET_ALL) 

def loss(lost_turns):
    """draws stickman from list of moves sequencially per lost turn"""
    if lost_turns == 0:
        string_var.set(formatedTriedChars())
        window.update()
        return
    if lost_turns > 3:
        wide = 5
        col = 'white'
    else: 
        wide = 10
        col = 'saddlebrown'

    if lost_turns != 4:
        canvas.create_line(man[lost_turns - 1], fill = col, width = wide)  
    else:
        canvas.create_oval(man[lost_turns - 1], fill = col, width = wide)
    
    string_var.set(formatedTriedChars()) #assuming tried chars is list of incorect
    window.update()


#Menu Functions are called:
loading()
title()
clear_screen()
menu()


usrDiffi = getPlayerChoice()
randomWord = 'i know this word'
randomWord = selectDif(usrDiffi)
make_blanks(randomWord)
livesLost = 0
while livesLost < 9:# main gameplay loop
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
    else:
        triedChars.append(recent)
        livesLost += 1
    if stillBlanks() == False:
        the_word.set(printBlanks())
        loss(livesLost)
        win = True
        break
else:
    loss(livesLost)
    print('you lose')
    win = False

#Restarts/Ends game depending on if the user wants to play again or not
if win:
    string_var.set('YOU WIN!!!, do you want to play again(Y/N)')
else:
    string_var.set('YOU LOSE, do you want to play again(Y/N)')
    the_word.set('The word was: ' + randomWord)
window.update()
replayGame = ''
userInput.delete(0, tkinter.END)
time.sleep(1)

while bool(replayGame) == False:
    recent = ''
    while bool(recent) == False:
        recent = userInput.get()
        time.sleep(0.01)
        userInput.delete(0, tkinter.END)
        window.update()
    if 'y' in recent.lower():
        restart_program()
    elif 'n' in recent.lower():
        break
    else:
        print('must chose yes or no')