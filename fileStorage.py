"""
# File       : fileStorage.py
# Time       : 5:12 PM
# Author     : vincent
# version    : python 3.8
# Description:
"""
import json
# txt file write and read demo
# with open('test.txt', 'w+', encoding='utf-8') as f:
#     f.write('This is a test file!')
# with open('test.txt', 'r+', encoding='utf-8') as f:
#     print(f.read())
# using json file storage
# read json from string
strs = '''
[{
    "name": "Bob",
    "gender": "Male",
    "birthday": "1992-10-18"
}, {
    "name": "Selina",
    "gender": "Female",
    "birthday": "1995-10-18"}, 
    {
    "name": "麦克",
    "gender": "女",
    "birthday": "1999-1-1"   
}]
'''
print(type(strs))
data = json.loads(strs)
print(data)
print(type(data))
print(data[0]["name"])
print(data[0].get('gender'))
print(data[0].get('age'))  # if key is not exist, it will return None
print(data[0].get('age', 20))  # if key is not exist, but give second arg, it will return default

strs = '''
    [{
        'hello': "bug"
    }]
'''
strs = strs.replace("'", "\"")
temp = json.loads(strs)
print(temp)

# fuck create wheels fuck! equals next method
with open('data.json', 'w+', encoding='utf-8') as f:
    s = "["
    for i in range(len(data)):
        s += "{"
        s += "\"name\"" + ":\"" + data[i]['name'] + "\"" + "," + \
             "\"gender\"" + ":\"" + data[i]['gender'] + "\"" + "," + \
             "\"birthday\"" + ":\"" + data[i]['birthday'] + "\""
        s += "}"
        if (i + 1) < len(data):
            s += ","
    s += "]"
    f.write(s)

# equals last method
with open('data.json', 'w+', encoding='utf-8') as f:
    f.write(json.dumps(data))

# add indent to json file
with open('data.json', 'w+', encoding='utf-8') as f:
    f.write(json.dumps(data, indent=2))

# make sure chinese words in normal to file
with open('data.json', 'w+', encoding='utf-8') as f:
    f.write(json.dumps(data, indent=2, ensure_ascii=False))

# read json data from json file
with open('data.json', 'r+') as f:
    s = f.read()
    data = json.loads(s)
print(data)

