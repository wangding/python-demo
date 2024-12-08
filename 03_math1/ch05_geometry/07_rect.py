# 在 Processing 中画一圈矩形
# 并实现矩形旋转动画，没有擦除，带残影

t = 0

def setup():
  size(600, 600)
  background(255, 255, 255)

def draw():
  global t
  translate(width/2, height/2)
  rotate(radians(t))
  for i in range(12):
    stroke(255, 0, 0)
    rect(200, 40, 50, 50)
    rotate(radians(360/12))
  t += 0.1