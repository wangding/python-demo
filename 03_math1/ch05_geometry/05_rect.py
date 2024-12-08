# 在 Processing 中画一个矩形
# 先平移到屏幕中心
# 再旋转 20 度

def setup():
  size(600, 600)
  
def draw():
  translate(width/2, height/2)
  rotate(radians(20))
  rect(20, 40, 50, 30)