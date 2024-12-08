# 在 Processing 中画一个矩形，并平移到屏幕中心

def setup():
  size(600, 600)
  
def draw():
  translate(width/2, height/2)
  rect(20, 40, 50, 30)