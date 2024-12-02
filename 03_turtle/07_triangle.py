# 画等边三角形，三角形函数带默认参数
from turtle import *

def init():
  color('blue')
  width(3)
  shape('turtle')

def triangle(side_length=100):
  for i in range(3):
    forward(side_length)
    right(120)

def main():
  init()
  triangle()
  mainloop()

main()