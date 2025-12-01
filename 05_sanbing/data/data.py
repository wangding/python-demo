import csv

f_in = open('list.txt', 'r', encoding='utf-8')
f_out = open('output.csv', 'a', newline='', encoding='utf-8-sig')

lines = f_in.readlines()
for line in lines:
  parts = line.strip().split()[1:5]
  writer = csv.writer(f_out)
  writer.writerow(parts)
f_in.close()
f_out.close()
