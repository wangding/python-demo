# 海龟漫步
# 带随机传送功能，避免边界外卡死现象

from turtle import *
from random import randint

def init():
  color('blue')
  speed(0)
  shape('turtle')

def wander():
  num = 0  # 海龟逃逸次数
  while True:
    forward(5)
    if num > 5:
      num = 0
      goto(randint(-200, 200), 
           randint(-200, 200))

    if xcor() >= 200 or \
       xcor() <= -200 or \
       ycor() >= 200  or \
       ycor() <= -200:
      left(randint(90, 180))
      num += 1

def main():
  init()
  wander()
  mainloop()

main()