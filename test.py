from tkinter import*
import time
root = Tk()
import os
import sys
string_var = StringVar() 
string_var.set('default')
label_tries = Label(root, font=(16), textvariable = string_var)
label_tries.pack(side=BOTTOM)

def canvas_create():
    global c
    global l
    c =  Canvas(root, width=500, height=500, bg= 'red')
    c.pack()
    l = Label(root, text="This is where the stickman will be drawn")
    l.place(height=50, width= 500)
    root.attributes("-topmost", True)
canvas_create()
c.create_line(50,450,150,450)
man = [[100,450,100,75], [100,75,250,75], [250,75,250,100], [200,200,300,100], [250,200,250,300], [250,300,350,400], [250,300,150,400], [250,250,150,250], [250,250, 350,250]]
tried_letters = sorted(['f','g','h','j', 'w','e'])



def loss(lost_turns):
    if lost_turns > 2:
        wide = 5
        col = 'white'
    else: 
        wide = 10
        col = 'saddlebrown'

    if lost_turns != 3:
        c.create_line(man[lost_turns], fill = col, width = wide)  
        print(lost_turns)
        print(man[lost_turns])
    else:
        c.create_oval(man[lost_turns], fill = col, width = wide)
    


for i in range(0,9):
    loss(i)
    time.sleep(0.1)
    root.update()
    
inp = input(': ')
if inp == 'True':
    print('done')
    string_var.set(tried_letters)
    root.update 
    

def restart_program():
    """Restarts the current program."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

root.mainloop()
