# 1. 基本输出
print("Hello, World!")

# 2. 输出多个值
name = "Alice"
age = 30
print("2. Name:", name, "Age:", age)

# 3. 使用 sep 参数
print("3. Name:", name, "Age:", age, sep=" | ")

# 4. 使用 end 参数
print("Hello,", end=" ")
print("World!")

# 5. 使用 file 参数
with open("output.txt", "w") as f:
    print("Hello, World!", file=f)
# 上面两行等价于下面两行
f = open("output.txt", "w")
print("Hello, World!", file=f)

# 6. 使用 flush 参数
print("Hello, World!", flush=True)

# 7. 字符串格式化
print("7. Name: %s, Age: %d" % (name, age))

# 8. 使用 str.format 方法
print("8. Name: {}, Age: {}".format(name, age))

# 9. 使用 f-string
print(f"9. Name: {name}, Age: {age}")