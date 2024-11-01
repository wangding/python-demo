def validate(score):
  res = {"iswrong": False, "reason":  ''}

  if score == '':
    res["iswrong"] = True
    res["reason"]  = '不能为空'
    return res

  if type(score) in [str] and not score.isdigit():
    res["iswrong"] = True
    res["reason"]  = '不是数值'
    return res

  if int(score) > 100 or int(score) < 0:
    res["iswrong"] = True
    res["reason"]  = '超出范围'

  return res

def level(score):
  num = int(score)
  level = ''

  if num >= 90:
    level = '优'
  elif num >=80 and num < 90:
    level = '良'
  elif num >=70 and num < 80:
    level = '中'
  elif num >=60 and num < 70:
    level = '可'
  else:
    level = '差';
  return level

def main():
  scores = ['', 29, 69, 72, 88, 91, 'ab', 121];

  for score in scores:
    result = validate(score)
    if result["iswrong"]:
      print(f'score = {score}, {result["reason"]}')
    else:
      print(f'score = {score}, level = {level(score)}')

main()