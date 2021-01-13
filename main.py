import random

temp_list = ['apple', 'banana', 'oranges']
word = temp_list[random.randint(0,2)]
letters = list(word)

def make_blanks(letters):
    global blanks
    blanks = []
    for i in range(len(letters)):
        blanks.append('_')
    
    return blanks
    


make_blanks(letters)
print(blanks)