# 海龟漫步

from turtle import *
from random import randint

def init():
  color('blue')
  speed(0)
  shape('turtle')

def wander():
  while True:
    forward(5)
    if xcor() >= 200 or \
       xcor() <= -200 or \
       ycor() >= 200  or \
       ycor() <= -200:
      left(randint(90, 180))

def main():
  init()
  wander()
  mainloop()

main()