import sys 
import math
import time
import random
from random import randint

print"\n------------------------ Welcome to the Guessing Game -----------------------------------"
print """
Here are the rules:

#The Computer will choose a random number in the range of 0-50
#You will get chances to correctly guess the number that the computer chose
#You have to do it in as many less chances as possible
#When you the number correctly, the program ends with the count (i.e. the number of guesses you required for doing the task)\


"""

a=randint(0,50)

print "\n The Computer has finished picking up a random number between 0 and 50. Can you guess it ??"



rep=0
finalcount=0
while(rep!=1):
    correct=0
    while(correct!=1):
        try:
            print"\n"
            guess=int(raw_input("What is Your Guess :"))
            correct=1
        except:
            print"\n Please enter a valid integer value"
    
    if (a==guess):
        print"\nCorrect Guess"
        finalcount=finalcount+1
        rep=1
    else:
        print"\nWrong Guess. You get one more chance"
        finalcount=finalcount+1
        if (guess<a):
            print"\nYour Guess is less than the chosen number "
        if (guess>a):
            print"\nYour Guess is greater than the chosen number  "
        
print"\n You guessed it in %d chances"%finalcount



