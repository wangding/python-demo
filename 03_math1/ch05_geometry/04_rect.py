# 在 Processing 中画一个矩形，并旋转 20 度

def setup():
  size(600, 600)
  
def draw():
  rotate(radians(20))
  rect(20, 40, 50, 30)