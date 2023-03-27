# DataStorage
## File Storage（文件存储）
### 文件打开模式：
#### w: 
以写入方式打开一个文件 。 如果该文件已存在，则将其瞿盖 。 如果该文件不存在，则创 建新文件 。

#### wb:
以二进制写入方式打开一个文件。 如果该文件已存在，则将其覆盖。 如果该文件不存 在， 则创建新文件。

##### 附:
以读写方式打开一个文件 。 如果该文件已存在，则将其覆盖 。 如果该文件不存在，则创 建新文件 。

#### wb+:
以二进制读写格式打开一个文件。 如果该文件已存在， 则将其覆盖。 如果该文件不存 在， 则创建新文件。

#### a: 
以追加方式打开一个文件。 如果该文件已存在，文件指针将会放在文件结尾 。 也就是 说，新的内容将会被写入到已有内容之后。 如果该文件不存在， 则创建新文件来写入。

#### ab:
以二进制追加方式打开一个文件 。 如果该文件已存在，则文件指针将会放在文件结尾 。 回 也就是说，新的内容将会被写入到己有内容之后。 如果该文件不存在，则创建新文件来写入。

#### a+:
以读写方式打开一个文件 。 如果该文件已存在，文件指针将会放在文件的结尾 。 文件打 开时会是追加模式。 如果眩文件不存在，则创建新文件来读写。

#### ab+:
以二进制追加方式打开一个文件。 如果该文件已存在，则文件指针将会放在文件结尾。 如果该文件不存在，则创建新文件用于读写 。

### txt 文件存储与读取
```python
# file write and read demo
with open('test.txt', 'w+', encoding='utf-8') as f:
    f.write('This is a test file!')
with open('test.txt', 'r+', encoding='utf-8') as f:
    print(f.read())
out:
This is a test file!
```
### json文件存储与读取
```python
import json
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
out:
/usr/local/bin/python3.9 /Volumes/WorkSpace/ProgramCodes/Python/DataStorage/fileStorage.py 
<class 'str'>
[{'name': 'Bob', 'gender': 'Male', 'birthday': '1992-10-18'}, {'name': 'Selina', 'gender': 'Female', 'birthday': '1995-10-18'}, {'name': '麦克', 'gender': '女', 'birthday': '1999-1-1'}]
<class 'list'>
Bob
Male
None
20
[{'hello': 'bug'}]
[{'name': 'Bob', 'gender': 'Male', 'birthday': '1992-10-18'}, {'name': 'Selina', 'gender': 'Female', 'birthday': '1995-10-18'}, {'name': '麦克', 'gender': '女', 'birthday': '1999-1-1'}]

Process finished with exit code 0
```
### csv 文件存储与读取
```python
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
out:
/usr/local/bin/python3.9 /Volumes/WorkSpace/ProgramCodes/Python/DataStorage/fileStorage.py 
['id', 'name', 'age']
['10001', 'Mike', '20']
['10002', 'Bob', '22']
['10003', 'Jordan', '21']
['10007', '刘俊芝', '99']
      id    name  age
0  10001    Mike   20
1  10002     Bob   22
2  10003  Jordan   21
3  10007     刘俊芝   99

Process finished with exit code 0
```
## Database Storage（数据库存储）
### 














# 学习路线已同步 github:[数据存储](https://github.com/VincentAdamNemessisX/DataStorage)




