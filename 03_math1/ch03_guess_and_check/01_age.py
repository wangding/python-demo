# 根据用户输入年龄，给出反馈

age = int(input('How old are you? '))

if age < 10:
  print('What school do you go to?')
elif 10 <= age < 20:
  print("You're cool!")
elif 20 <= age < 30:
  print('What job do you have?')
elif 30 <= age < 40:
  print('Are you married?')
else:
  print("Wow, you're old!")