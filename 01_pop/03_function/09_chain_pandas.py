import pandas as pd

# 创建一个 DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# 使用链式调用进行数据处理
result = df[df['Age'] > 25]  \
            .sort_values(by='Age')  \
            .reset_index(drop=True)

print(result)