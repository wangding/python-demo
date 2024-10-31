# 1.数值类型之间的转换
# 整数转浮点数
int_value = 10
float_value = float(int_value)
print(float_value)  # 输出: 10.0

# 浮点数转整数
float_value = 10.5
int_value = int(float_value)
print(int_value)  # 输出: 10

# 字符串转整数
str_value = "123"
int_value = int(str_value)
print(int_value)  # 输出: 123

# 字符串转浮点数
str_value = "123.45"
float_value = float(str_value)
print(float_value)  # 输出: 123.45

# 整数转字符串
int_value = 123
str_value = str(int_value)
print(str_value)  # 输出: "123"

# 浮点数转字符串
float_value = 123.45
str_value = str(float_value)
print(str_value)  # 输出: "123.45"

# 2.列表和元组之间的转换
# 列表转元组
list_value = [1, 2, 3]
tuple_value = tuple(list_value)
print(tuple_value)  # 输出: (1, 2, 3)

# 元组转列表
tuple_value = (1, 2, 3)
list_value = list(tuple_value)
print(list_value)  # 输出: [1, 2, 3]

# 3.列表和集合之间的转换
# 列表转集合
list_value = [1, 2, 3, 3, 4]
set_value = set(list_value)
print(set_value)  # 输出: {1, 2, 3, 4}

# 集合转列表
set_value = {1, 2, 3}
list_value = list(set_value)
print(list_value)  # 输出: [1, 2, 3] （顺序可能不同）

# 4.字典和列表之间的转换
# 字典的键转列表
dict_value = {"name": "Alice", "age": 25}
keys_list = list(dict_value.keys())
print(keys_list)  # 输出: ['name', 'age']

# 字典的值转列表
dict_value = {"name": "Alice", "age": 25}
values_list = list(dict_value.values())
print(values_list)  # 输出: ['Alice', 25]

# 列表转字典
keys = ["name", "age"]
values = ["Alice", 25]
dict_value = dict(zip(keys, values))
print(dict_value)  # 输出: {'name': 'Alice', 'age': 25}

# 5.字符串和列表之间的转换
# 字符串转列表
str_value = "hello"
char_list = list(str_value)
print(char_list)  # 输出: ['h', 'e', 'l', 'l', 'o']

# 列表转字符串
char_list = ['h', 'e', 'l', 'l', 'o']
str_value = ''.join(char_list)
print(str_value)  # 输出: "hello"

# 6.布尔值转换
# 整数转布尔值
int_value = 0
bool_value = bool(int_value)
print(bool_value)  # 输出: False

int_value = 1
bool_value = bool(int_value)
print(bool_value)  # 输出: True

# 浮点数转布尔值
float_value = 0.0
bool_value = bool(float_value)
print(bool_value)  # 输出: False

float_value = 1.0
bool_value = bool(float_value)
print(bool_value)  # 输出: True

# 字符串转布尔值
str_value = ""
bool_value = bool(str_value)
print(bool_value)  # 输出: False

str_value = "hello"
bool_value = bool(str_value)
print(bool_value)  # 输出: True

# 列表、元组、集合、字典转布尔值
empty_list = []
bool_value = bool(empty_list)
print(bool_value)  # 输出: False

non_empty_list = [1, 2, 3]
bool_value = bool(non_empty_list)
print(bool_value)  # 输出: True

empty_tuple = ()
bool_value = bool(empty_tuple)
print(bool_value)  # 输出: False

non_empty_tuple = (1, 2, 3)
bool_value = bool(non_empty_tuple)
print(bool_value)  # 输出: True

empty_set = set()
bool_value = bool(empty_set)
print(bool_value)  # 输出: False

non_empty_set = {1, 2, 3}
bool_value = bool(non_empty_set)
print(bool_value)  # 输出: True

empty_dict = {}
bool_value = bool(empty_dict)
print(bool_value)  # 输出: False

non_empty_dict = {"name": "Alice", "age": 25}
bool_value = bool(non_empty_dict)
print(bool_value)  # 输出: True