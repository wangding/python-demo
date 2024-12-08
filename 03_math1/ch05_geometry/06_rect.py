# 在 Processing 中画一圈矩形

def setup():
  size(600, 600)
  background(255, 255, 255)
  
def draw():
  translate(width/2, height/2)
  for i in range(12):
    stroke(255, 0, 0)
    rect(200, 40, 50, 50)
    rotate(radians(360/12))