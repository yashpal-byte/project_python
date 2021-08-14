#word guessing game
#random.choice() method to select random word from list, tuple or string

import random

name = input('Ender your name: ')
print('Ab dikha apna jalwa', name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
         
#function will choose random word from list

word = random.choice(words)
print('Guess the characters')

guesses = ''

turns = 5

while turns>0:
    # counts the number of times a user fails
    failed = 0
     
    # all characters from the input
    # word taking one at a time.
    for char in word:
        # comparing that character with
        # the character in guesses
        if char in guesses:
            print(char)
             
        else:
            print("_")
             
            # for every failure 1 will be
            # incremented in failure
            failed += 1
        if failed == 0:
            print('You win')
            
            print('The word is: ', word)
            break
        
        guess = input('guess the character: ')
        
        guesses += guess
        
        # check input with the character in word
        if guess not in word:
            turns -=1 
            print('Wrong')
            
            print('You have', + turns, 'more guesses')
            
            if turns == 0:
                print('You loose')