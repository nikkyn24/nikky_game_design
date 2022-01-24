#NumberGuessingGame
#1/20/22

#Guess the number to win the game

from asyncio import events
import os
import random
from typing import Counter
os.system('cls')
gameOn=True

print("########################")
print("# Guess a Number Menu #")
userNumA=input("#1-10= A")
userNumB=input("#1-20= B")
userNumC=input("#1-50= C")

while True:
    prompt1=input('Select a level :').lower()

    if prompt1 == 'A':
       guess=random.randint(1,10)
    userNumA=input("guess a number from 1-10 ")
    while gameOn: 
        userNumA=int(userNumA)
        Counter = +1
        if userNumA == guess:
            print("Congratulations, you are smart")
        else:
            if userNumA > guess +1:
                print("So sad, not so bright!")
            else:
                if userNumA < guess -1:
                 print("So sad, too low!")
    if prompt1 == 'B':
        guess=random.randint(1,20)
    userNumA=input("guess a number from 1-20 ")
    while gameOn: 
        userNumA=int(userNumA)
        Counter = +1
        if userNumA == guess:
            print("Congratulations, you are smart")
        else:
            if userNumA > guess +5:
                print("So sad, not so bright!")
            else:
                if userNumA < guess -5:
                 print("So sad, too low!")
    if prompt1 == 'C':
        guess=random.randint(1,50)
    userNumA=input("guess a number from 1-50 ")
    while gameOn: 
        userNumA=int(userNumA)
        Counter = +1
        if userNumA == guess:
            print("Congratulations, you are smart")
        else:
            if userNumA > guess +10:
                print("So sad, not so bright!")
            else:
                if userNumA < guess -10:
                 print("So sad, too low!")
    
