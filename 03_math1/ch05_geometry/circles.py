# 在 Processing 中画一个矩形
# 先平移到屏幕中心
# 再旋转 20 度

def setup():
  size(600, 600)
  background(255, 255, 255)
  
def draw():
  translate(width/2, height/2)
  for i in range(12):
    stroke(255, 0, 0)
    circle(200, 0, 10)
    rotate(radians(360/12))