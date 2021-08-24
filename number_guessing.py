import random
import math

#input
lower = int(input("Enter lower bound: "))

#input
upper = int(input("Enter upper bound: "))

#generating random number between lower and upper
x = random.randint(lower, upper)

y = math.log(upper-lower + 1, 2)
print("You have only", round(y), "chances to guess the number")

#initializing the number of guesses.

count = 0

# for calculation of minimum no of guesses depends upon range.

while count < y:
    count+=1
    #guessing number as input
    guess = int(input("guess a number: "))
    
    #condition testing
    if x == guess:
        print("Coungrats!! you did it in ", count, "try")
        break
    elif x>guess:
        print("you have guessed too small")
    elif x<guess:
        print("you have guessed too high")

#if guessing is more than required guess, shows this output

if count>y:
    print("The number is %d" %x)
    print("Better luck next time")