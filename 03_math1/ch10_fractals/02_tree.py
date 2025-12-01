from turtle import *

speed(100)
left(90)

def branch(branch_len):
  if branch_len > 10:
    angle = 30
    forward(branch_len)
    left(angle)
    branch(branch_len*0.7)
    right(angle*2)
    branch(branch_len*0.7)
    left(angle)
    backward(branch_len)
    
branch(100)
done()