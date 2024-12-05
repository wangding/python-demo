# 旋转画一圈五角星，旋转的同时增加五角星的变长
from turtle import *

def init():
  color('blue')
  speed(0)
  shape('turtle')

def star(side_length=100):
  for i in range(5):
    forward(side_length)
    right(144)

def main():
  init()
  side_length = 50
  for x in range(60):
    star(side_length)
    side_length += 5
    right(5)
  mainloop()

main()