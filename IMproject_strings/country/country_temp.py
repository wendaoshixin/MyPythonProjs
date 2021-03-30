import json

json_str = {'key1': 'value1', 'key2': 'value2'}

# 写入文件
# 可以通过json包，将json串（可以是字符串类型、字典类型、json类型）直接写入到文件中
with open('something.json') as sjw:
    json.dump(json_str, sjw)

# 读取文件
json_read = json.load('something.json')
print(json_read)
json_read.close()