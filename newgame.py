import random
import os
guessesTaken = 0  
print("##################")
print("                  ")
print('What is your name?')
print("                  ")
myName = input() 
print("                  ")
print('Hello, ' + myName  )
print("  Level 1: #1-10  ")
print("  Level 2: #1-30  ")
print("  Level 3: #1-50  ")
print("                  ")
gametype= int(input('Hello, ' + myName + ', Select a level:'))
print("                  ")
if gametype== 1:
    number = randint(1, 10) 
while guessesTaken < 5:
  print("                  ")
  print("You selected Level 1 (#1-10)")
  print('Take a guess')
  print("                  ")
  guess = int(input())  
  guessesTaken = guessesTaken + 1 
  if guess < number:
    print("                  ")
    print('So sad! Too low.')
    print("                  ")
  if guess > number:
    print("                  ")
    print('So sad! Too high')
    print("                  ")
  if guess == number:
    break
if guess == number:
  guessesTaken = str(guessesTaken)
  print("                  ")
  print('Aight- Good job, ' + myName + '! You guessed the correct number in ' + guessesTaken + ' guesses!')
if guess != number:
  number = str(number)
  print("                  ")
  print('Dude- you suck. Get it together. The number that I was thinking is ' + number)

if gametype== 2:
    number = randint(1, 30) 
while guessesTaken < 5:
  print("                  ")
  print("You selected Level 1 (#1-30)")
  print('Take a guess')
  print("                  ")
  guess = int(input())  
  guessesTaken = guessesTaken + 1 
  if guess < number:
    print("                  ")
    print('So sad! Too low.')
    print("                  ")
  if guess > number:
    print("                  ")
    print('So sad! Too high')
    print("                  ")
  if guess == number:
    break
if guess == number:
  guessesTaken = str(guessesTaken)
  print("                  ")
  print('Aight- Good job, ' + myName + '! You guessed the correct number in ' + guessesTaken + ' guesses!')
if guess != number:
  number = str(number)
  print("                  ")
  print('Dude- you suck. Get it together. The number that I was thinking is ' + number)

  if gametype== 3:
    number = randint(1, 50) 
while guessesTaken < 5:
  print("You selected Level 1 (#1-50)")
  print("                  ")
  print('Take a guess')
  print("                  ")
  guess = int(input())  
  guessesTaken = guessesTaken + 1 
  if guess < number:
    print("                  ")
    print('So sad! Too low.')
    print("                  ")
  if guess > number:
    print("                  ")
    print('So sad! Too high')
    print("                  ")
  if guess == number:
    break
if guess == number:
  guessesTaken = str(guessesTaken)
  print("                  ")
  print('Aight- Good job, ' + myName + '! You guessed the correct number in ' + guessesTaken + ' guesses!')
if guess != number:
  number = str(number)
  print("                  ")
  print('Dude- you suck. Get it together. The number that I was thinking is ' + number)
