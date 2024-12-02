# 旋转着画正方形，每次旋转正方形的尺寸会变大
from turtle import *

def init():
  color('blue')
  speed(0)
  shape('turtle')

def polygon(sides=4, side_length=100):
  angle = 360/sides
  for i in range(sides):
    forward(side_length)
    right(angle)

def main():
  init()
  side_length = 5
  for x in range(60):
    polygon(4, side_length)
    side_length += 5
    right(5)
  mainloop()

main()