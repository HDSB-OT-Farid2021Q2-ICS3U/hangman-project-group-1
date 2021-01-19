import random
import time
import os
import sys
import msvcrt
import tkinter # for some reason it need both imports of tkinter
from colorama import Fore, Back, Style 
from tkinter import*
window=Tk()
global triedChars
triedChars = []
man = [[100,450,100,75], [100,75,250,75], [250,75,250,100], [200,200,300,100], [250,200,250,300], [250,300,350,400], [250,300,150,400], [250,250,150,250], [250,250, 350,250],[250,250, 350,250]]


canvas = Canvas(window, width=500, height=500, bg= 'black')



window = Tk()# make the window
window.attributes('-topmost', True)
window.title('HANGMAN')
label = Label(window, textvariable='blank for test', font=16) # Create top Label
label.place(height=40, width= 500)
label.pack()
canvas.pack()

label_tries = Label(window, font=(16), text='tries will be diaplayed here')
userInput = Entry(window)
userInput.pack(side=BOTTOM)
label_tries.pack(side=BOTTOM)









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
    else:
        canvas.create_oval(man[lost_turns - 1], fill = col, width = wide)

for i in range(10):
    loss(i)
    window.update()
    time.sleep(2)


window.mainloop