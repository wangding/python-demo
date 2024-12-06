# 猜数游戏

from random import randint

def game():
  number = randint(1, 100)
  print("I'm thinking of a number between 1 and 100.")
  while True:
    guess = int(input("What's your guess? "))
    if guess == number:
      print("That's correct! The number was %d" % number)
      break
    elif guess < number:
      print('Nope. Higher.')
    else:
      print('Nope. Lower.')

game()