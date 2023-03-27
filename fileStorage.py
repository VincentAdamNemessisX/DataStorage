"""
# File       : fileStorage.py
# Time       : 5:12 PM
# Author     : vincent
# version    : python 3.8
# Description:
"""
import json
import csv
import pandas as pd

# txt file write and read demo
# with open('test.txt', 'w+', encoding='utf-8') as f:
#     f.write('This is a test file!')
# with open('test.txt', 'r+', encoding='utf-8') as f:
#     print(f.read())
# using json file storage
# read json from string
# strs = '''
# [{
#     "name": "Bob",
#     "gender": "Male",
#     "birthday": "1992-10-18"
# }, {
#     "name": "Selina",
#     "gender": "Female",
#     "birthday": "1995-10-18"},
#     {
#     "name": "麦克",
#     "gender": "女",
#     "birthday": "1999-1-1"
# }]
# '''
# print(type(strs))
# data = json.loads(strs)
# print(data)
# print(type(data))
# print(data[0]["name"])
# print(data[0].get('gender'))
# print(data[0].get('age'))  # if key is not exist, it will return None
# print(data[0].get('age', 20))  # if key is not exist, but give second arg, it will return default

# strs = '''
#     [{
#         'hello': "bug"
#     }]
# '''
# strs = strs.replace("'", "\"")
# temp = json.loads(strs)
# print(temp)

# fuck create wheels fuck! equals next method
# with open('data.json', 'w+', encoding='utf-8') as f:
#     s = "["
#     for i in range(len(data)):
#         s += "{"
#         s += "\"name\"" + ":\"" + data[i]['name'] + "\"" + "," + \
#              "\"gender\"" + ":\"" + data[i]['gender'] + "\"" + "," + \
#              "\"birthday\"" + ":\"" + data[i]['birthday'] + "\""
#         s += "}"
#         if (i + 1) < len(data):
#             s += ","
#     s += "]"
#     f.write(s)

# equals last method
# with open('data.json', 'w+', encoding='utf-8') as f:
#     f.write(json.dumps(data))

# add indent to json file
# with open('data.json', 'w+', encoding='utf-8') as f:
#     f.write(json.dumps(data, indent=2))

# make sure chinese words in normal to file
# with open('data.json', 'w+', encoding='utf-8') as f:
#     f.write(json.dumps(data, indent=2, ensure_ascii=False))

# read json data from json file
# with open('data.json', 'r+') as f:
#     s = f.read()
#     data = json.loads(s)
# print(data)

# csv(Comma-Separated Values) file storage
with open('data.csv', 'w+') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Mike', 20])
    writer.writerow(['10002', 'Bob', 22])
    writer.writerow(['10003', 'Jordan', 21])

# using list
with open('data.csv', 'w+') as f:
    writer = csv.writer(f, delimiter='|')
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Mike', 20])
    writer.writerow(['10002', 'Bob', 22])
    writer.writerow(['10003', 'Jordan', 21])

# using multi-list
with open('data.csv', 'w+') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'name', 'age'])
    writer.writerows([['10001', 'Mike', 20],
                      ['10002', 'Bob', 22],
                      ['10003', 'Jordan', 21]
                      ])

# using multi-dict
with open('data.csv', 'w+') as f:
    keys = ['id', 'name', 'age']
    writer = csv.DictWriter(f, fieldnames=keys)
    writer.writeheader()
    writer.writerows([
        {'id': '10001', 'name': 'Mike', 'age': 20},
        {'id': '10002', 'name': 'Bob', 'age': 22},
        {'id': '10003', 'name': 'Jordan', 'age': 21},
        {'id': '10007', 'name': '刘俊芝', 'age': 99}
    ])

# read data from csv file
with open('data.csv', 'r+', encoding='utf-8') as f:
    reader = csv.reader(f)
    for item in reader:
        print(item)

# read data from csv file by panda library to output
df = pd.read_csv('data.csv')
print(df)