import random

temp_list = ['apple', 'banan', 'oranges']
word = temp_list[random.randint(0,2)]
letters = list(word)

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
make_blanks(letters)
checker()