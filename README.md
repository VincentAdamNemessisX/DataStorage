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
### 关系型数据库
#### 数据库事务属性
|属性|解释|
| :-----: | ----- |
|原子性（atomicity）|事务是一个不可分割的工作单位，事务中包括的诸操作要么都做，要么都不做|
|一致性（consistency）|事务必须使数据库从一个一致性状态变到另一个一致性状态。一致性与原子性是密切相关的|
|隔离性（isolation）|一个事务的执行不能被其他事务干扰即一个事务内部的操作及使用的数据对并发的其他事务是隔离的，并发执行的各个事务之间不能互相干扰|
|持久性（durability）|持续性也称永久性（permanence），指一个事务一旦提交，它对数据库中数据的改变就应该是永久性的。接下来的其他操作或故障不应该对其有任何影响|

####  数据库连接与创建
```python
import pymysql
db = pymysql.connect(host='localhost', user='root', password='root', port=3333)
cursor = db.cursor()
cursor.execute('Select version()')
data = cursor.fetchone()
print('Database Version:', data)
cursor.execute("Create Database spiders Default CHARACTER SET utf8")
db.close()
```
#### 数据库之创建表与插入数据
```python
# create table
cursor.execute("Create Table if not exists students"
               "(id varchar(255) not null,"
               "name varchar(255) not null,"
               "age int not null,"
               "primary key (id))")

# insert data
id = '2012042141'
user = 'bob'
age = 20
sql = 'Insert into students(id, name, age) values (%s, %s, %s)'
try:
    cursor.execute(sql, (id, user, age))
    db.commit()
except:
    db.rollback()
```
```python
# insert data next generation method
data = {
    'id': '2012424234',
    'name': 'Bug',
    'age': 30
}
table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s'] * (len(data)))
sql = 'Insert into {table}({keys}) values ({values})'.format(table=table, keys=keys, values=values)
try:
    if cursor.execute(sql, tuple(data.values())):
        print('Insert successful')
        db.commit()
except:
    print("Insert failed")
    print(sql)
    db.rollback()
out:
/usr/local/bin/python3.9 /Volumes/WorkSpace/ProgramCodes/Python/DataStorage/databaseStorage.py 
Database Version: ('5.7.34',)
Insert successful

Process finished with exit code 0
```
#### 数据库之表中更新数据
```python
# update data to mysql
data = {
    'id': '2012424234',
    'name': 'bbbb',
    'age': 21
}
table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s'] * len(data))
sql = 'Insert into {table}({keys}) values ({values}) on duplicate key update '\
    .format(table=table, keys=keys, values=values)
update = ','.join(["{key} = %s".format(key=key) for key in data])
sql += update
try:
    if cursor.execute(sql, tuple(data.values()) * 2):
        print('Update successful')
        db.commit()
except:
    print("Update failed")
    db.rollback()
out:
/usr/local/bin/python3.9 /Volumes/WorkSpace/ProgramCodes/Python/DataStorage/databaseStorage.py 
Database Version: ('5.7.34',)
Insert failed
Update successful

Process finished with exit code 0
```
#### 数据库之表中删除数据
```python
# delete data from table that in database of mysql
table = 'students'
condition = 'age > 20'
sql = 'Delete from {table} where {condition}'.format(table=table, condition=condition)
try:
    cursor.execute(sql)
    print('Delete successful')
    db.commit()
except:
    print('Delete failed')
    db.rollback()
out:
/usr/local/bin/python3.9 /Volumes/WorkSpace/ProgramCodes/Python/DataStorage/databaseStorage.py 
Database Version: ('5.7.34',)
Insert failed
Delete successful

Process finished with exit code 0
```
#### 数据库之表中查询数据
```python
# query data from table that in database of mysql
table = 'students'
condition = 'age >= 20'
sql = 'select * from {table} where {condition}'.format(table=table, condition=condition)
try:
    cursor.execute(sql)
    print('Count', cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print('Row', row)
        row = cursor.fetchone()
except:
    print('Query with error!')
out:
/usr/local/bin/python3.9 /Volumes/WorkSpace/ProgramCodes/Python/DataStorage/databaseStorage.py 
Database Version: ('5.7.34',)
Insert failed
Count 2
Row ('2012042141', 'bob', 20)
Row ('2012424234', 'bbbb', 21)

Process finished with exit code 0
```
### 非关系型数据库
#### 定义
NoSQL，全称 Not Only SQL，意为不仅仅是 SQL，泛指非关系型数据库 。 NoSQL 是基于键值对的，而且不需要经过 SQL 层的解析，数据之间没有搞合性 ， 性能非常高 。 非关系型数据库又可细分如下 ：

键值存储数据库:代表有 Redis、 Voldemort和 Oracle BDB 等 。

 列存储数据库:代表有 Cassandra、 HBase 和 Riak等 。

文档型数据库:代表有 CouchDB和 MongoDB等。 

图形数据库:代表有 Neo4J、 lnfoGrid和 InfiniteGraph等

#### MongoDB 存储
##### 数据库创建与连接
```python
import pymongo
client = pymongo.MongoClient("mongodb+srv://"
                             "vincent:ZTXic3344"
                             "@tempcluster.kslgvab.mongodb.net/"
                             "?retryWrites=true&w=majority")
# select or create database
db = client.test
# db = client['test']  # equals last method
```
##### 创建collection与数据插入
```python
# create collections
collection = db['students'] # equals next method
# collection = db.students

# insert data
student = {
    'id': '20214124',
    'name': 'Jordan',
    'age': 30,
    'gender': 'Male'
}
result = collection.insert_one(student)
print(result)

# insert many data
student1 = {
    'id': '2021413324',
    'name': 'Jordadn',
    'age': 20,
    'gender': 'Male'
}
student2 = {
    'id': '20d2143324',
    'name': 'Jadn',
    'age': 40,
    'gender': 'Male'
}
student3 = {
    'id': '20214124',
    'name': 'Jodadn',
    'age': 46,
    'gender': 'Male'
}
result = collection.insert_many([student1, student2, student3])
print(result)
out:
/usr/local/bin/python3.9 /Volumes/WorkSpace/ProgramCodes/Python/DataStorage/MongoDBStorage.py 
<pymongo.results.InsertOneResult object at 0x111a6a730>
<pymongo.results.InsertManyResult object at 0x111a8a520>

Process finished with exit code 0
```
##### 比较符号
|符号|含义|示例|
| :-----: | :-----: | :-----: |
|\$lt|小于|{'age': {'\$lt': 20}}|
|\$gt|大于|{'age': {'\$gt': '20'}}|
|\$lte|小于等于|{'age': {'\$lte': 20}}|
|\$gte|大于等于|{'age': {'\$gte': 20}}|
|\$ne|不等于|{'age': {'\$ne': 20}}|
|\$in|在范围内|{'age': {'\$in': \[20, 30\]}}|
|\$nin|不在范围内|{'age': {'\$nin': \[20, 30\]}}|

##### 功能符号
|符号|含义|示例|示例含义|
| :-----: | :-----: | ----- | ----- |
|\$regex|匹配正则表达式|{'name': {'\$regex': '^M.\*'}}|name 以 M 开头|
|\$exists|属性是否存在|{'name': {'\$exists': True}}|name 属性存在|
|\$type|类型判断|{'age': {'\$type': 'int'}}|age 的类型为 int|
|\$mod|数字模操作|{'age': {'\$mod': \[5, 0\]}}|年龄模 5 余 0|
|\$text|文本查询|{'\$text': {'\$search': 'Mike'}}|text类型的属性中包含Mike 字符串|
|\$where|高级条件查询|{'\$where': 'obj.fans\_count == obj.follows\_count'}|自身粉丝数等于关注数|

##### 数据查询
```python
# query data
result = collection.find_one({'name': 'Jordan'})
print(type(result))
print(result)
result = collection.find_one({'_id': ObjectId('6422a9e61bec7b1f2abe36db')})
print(result)
result = collection.find({'age': '30'})
print(type(result))
for item in result:
    print(item)
result = collection.find({'age': {'$gt': '10'}})
print(type(result))
for item in result:
    print(item)
out:
/usr/local/bin/python3.9 /Volumes/WorkSpace/ProgramCodes/Python/DataStorage/MongoDBStorage.py 
<class 'dict'>
{'_id': ObjectId('6422a9e61bec7b1f2abe36db'), 'name': 'Jordan', 'age': '30', 'gender': 'Female'}
{'_id': ObjectId('6422a9e61bec7b1f2abe36db'), 'name': 'Jordan', 'age': '30', 'gender': 'Female'}
<class 'pymongo.cursor.Cursor'>
{'_id': ObjectId('6422a9e61bec7b1f2abe36db'), 'name': 'Jordan', 'age': '30', 'gender': 'Female'}
{'_id': ObjectId('6422a9e71bec7b1f2abe36dc'), 'name': 'Bagar', 'age': '30', 'gender': 'Male'}
<class 'pymongo.cursor.Cursor'>
{'_id': ObjectId('6422a9e61bec7b1f2abe36db'), 'name': 'Jordan', 'age': '30', 'gender': 'Female'}
{'_id': ObjectId('6422a9e71bec7b1f2abe36dc'), 'name': 'Bagar', 'age': '30', 'gender': 'Male'}
{'_id': ObjectId('6422a9e81bec7b1f2abe36dd'), 'name': 'Nondor', 'age': '32', 'gender': 'Male'}

Process finished with exit code 0
```
##### 计数
```python
# count number
# 构建聚合查询管道
pipeline = [
    {'$group': {'_id': None, 'count': {'$sum': 1}}}
]
# 执行聚合查询，并获取文档数量
result = collection.aggregate(pipeline)
count = result.next()['count']
print(count)
out:
/usr/local/bin/python3.9 /Volumes/WorkSpace/ProgramCodes/Python/DataStorage/MongoDBStorage.py 
3

Process finished with exit code 0
```
##### 排序与偏移
```python
# sort data
results = collection.find().sort('name', pymongo.ASCENDING)
print([rst['name'] for rst in results])  # 列表推导式

# offset
results = collection.find().sort('name', pymongo.DESCENDING).skip(1)
print([result['name'] for result in results])
results = collection.find().sort('name', pymongo.DESCENDING).skip(1).limit(1)
print([result['name'] for result in results])
results = collection.find({'_id': {'$gt': ObjectId('6422a9e61bec7b1f2abe36db')}})
print([(result['name'], result['age']) for result in results])
out:
/usr/local/bin/python3.9 /Volumes/WorkSpace/ProgramCodes/Python/DataStorage/MongoDBStorage.py 
3
['Bagar', 'Jordan', 'Nondor']
['Jordan', 'Bagar']
['Jordan']
[('Bagar', '30'), ('Nondor', '32')]

Process finished with exit code 0
```
##### 更新数据
```python
# update data
condition = {'name': 'Jordan'}
stu = collection.find_one(condition)
stu['age'] = 99
result = collection.update_one(condition, {'$set': stu})
print(result)
print(result.matched_count, result.modified_count)

condition = {'age': {'$gt': 15}}
result = collection.update_many(condition, {'$inc': {'age': 5}})
print(result)
print(result.matched_count, result.modified_count)
out:
/usr/local/bin/python3.9 /Volumes/WorkSpace/ProgramCodes/Python/DataStorage/MongoDBStorage.py 
<pymongo.results.UpdateResult object at 0x1124ff280>
1 1
<pymongo.results.UpdateResult object at 0x11028ad60>
3 3

Process finished with exit code 0
```
##### 删除数据
```python
# remove data
result = collection.delete_one({'name': 'Bagar'})
print(result, result.deleted_count)
result = collection.delete_many({'age': {'$lt': 25}})
print(result.deleted_count)
out:
/usr/local/bin/python3.9 /Volumes/WorkSpace/ProgramCodes/Python/DataStorage/MongoDBStorage.py 
<pymongo.results.DeleteResult object at 0x1044e5d60> 1
0

Process finished with exit code 0
```
##### Python mongoDB详细用法官方文档： [Python mongoDB Using](https://pymongo.readthedocs.io/en/stable/api/index.html)
#### Redis 存储
Redis 是一个基于内存的高效的键值型非关系型数据库，存取效率极高，而且支持多种存储数据 结构，使用也非常简单。

##### 数据库连接与测试
```python
from redis import StrictRedis, ConnectionPool, Redis

# redis connect
redis = StrictRedis(host='8.130.73.157', port=6379, db=0, password='ic34')
redis.set('name', 'Bob')
print(redis.get('name'))
redis.close()

# redis connection pool
url = 'redis://:ic34@8.130.73.157:6379/0'  # redis: //:password@host:port/db_number
# url = 'redis://[:ic34]@8.130.73.157:6379/0'  # redis: //:redis: //:[password]@host:port/db_number
# url = 'unix://[:ic34]@8.130.73.157:6379/to/socket.sock?db=0' # redis: //:redis:  //:[password]@/path/to/socket.sock?db=db
pool = ConnectionPool.from_url(url)
# pool = ConnectionPool(host='8.130.73.157', port=6379, db=0, password='ic34')
redis = Redis(connection_pool=pool)
redis.set('hello', 'world!')
print(redis.get('hello'))
out:
/usr/local/bin/python3.9 /Volumes/WorkSpace/ProgramCodes/Python/DataStorage/redisDB.py 
b'world!'

Process finished with exit code 0
```
##### 键操作
|方法|作用|参数说明|示例|示例说明|示例结果|
| :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
|exists(name)|判断一个键是否存在| name:键名|redis.exists('name')|是否存在 name 这个键|True|
|delete(name)|删除一个键|name:键名|redis.delete('name')|删除 name 这个键|1|
|type(name)|判断键类型|name:键名|redis.type('name')|判断name 这个键类型|b'string'|
|keys(pattern)|获取所有符合规则的键|pattern:匹配规则|redis.keys('n\*')|获取所有以 n 开头的键|\[b'name'\]|
|randomkey()|获取随机的一个键| |randomkey()|获取随机的一个键|b'name'|
|rename(src, dst)|重命名键|src: 原键名<br>dst:新键名|redis.rename('name', 'nickname')|将 name 重命名为 nickname|True|
|dbsize()|获取当前数据库中键的数目| |dbsize()|获取当前数据库中键的数目|100|
|expire(name, time)|设定键的过期时间，单位为秒|name:键名<br>time:秒数|redis.expire('name', 2)|将name 键的过期时间设置为2秒|True|
|ttl(name)|获取键的过期时间，单位为秒,-1表示永久不过期|name:键名|redis.ttl('name')|获取 name 这个键的过期时间|\-1|
|move(name, db)|将键移动到其他数据库|name:键名<br>db:数据库代号|move('name', 2)|将 name 移动到2号数据库|True|
|flushdb()|删除当前选择数据库中的所有键| |flushdb()|删除当前选择数据库中的所有键|True|
|flushall()|删除所有数据库中的所有键| |flushall()|删除所有数据库中的所有键|True|

##### 字符串操作
|方法|作用|参数说明|示例|示例说明|示例结果|
| :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
|set(name, value)|给数据库中键为 name 的 string 赋予值 value|name:键名<br>value:值|redis.set('name', 'Bob')|给 name 这个键赋值为 Bob|True|
|get(name)|返回数据库中键为 name 的 string 的 value|name:键名|redis.get('name')|返回 name 这个键的 value|b'Bob'|
|getset(name, value)|给数据库中键为 name 的 string 赋予值 value 并返回上次的 value|name:键名<br>value:新值|redis.getset('name', 'Mike')|赋值 name 为 Mike 并得到上次的 value|b'Bob'|
|mget(keys, \*args)|返回多个键对应的 value|keys:键的列表|redis.mget(\['name', 'nickname'\])|返回 name 和 nickname 的 value|\[b'Mike', b'Miker'\]|
|setnx(name, value)|如果不存在这个键值对，则更新 value，否则不变|name:键名|redis.setnx('newname', 'James')|如果 newname 这个键不存在，则设置值为 James| 第一次运行结果是 True,第二次运行结果是 False|
|setex(name, time, value)|设置可以对应的值为 string 类型的 value，并指定此键值对对应的有效期|name:键名<br>time:有效期<br>value:值|redis.setex('name', 1, 'James')|将 name 这个键的值设为 James，有效期为1秒|True|
|setrange(name, offset, value)|设置指定键的 value 值的子字符串|name:键名<br>offset:偏移量<br>value:值|redis.set('name', 'Hello')<br>redis.setrange('name', 6, 'World')|设置 name 为 Hello 字符串，并在 index 为6的位置补 World|11，修改后的字符串长度|
|mset(mapping)|批量赋值|mapping:字典|redis.mset({'name1': 'Durant', 'name2': 'James'})|将 name1设为 Durant，name2设为 James|True|
|msetnx(mapping)|键均不存在时才批量赋值|mapping:字典|redis.msetnx({'name3': 'Smith', 'name4': 'Curry'})|在 name3和 name4均不存在的情况下才设置二者值|True|
|incr(name, amount=1)|键为 name 的 value 增值操作，默认为1，键不存在则被创建并设为 amount|name:键名<br>amount:增长的值|redis.incr('age', 1)|age 对应的值增1，若不存在，则会创建并设置为1|1，即修改后的值|
|decr(name, amount=1)|键为 name 的 value 减值操作，默认为1，键不存在则被创建并将 value 设置为-amount|name:键名<br>amount:减少的值|redis.decr('age', 1)|age 对应的值减1，若不存在，则会创建并设置为-1|\-1，即修改后的值|
|append(key, value)|键为 name 的 string 的值附加 value|key:键名|redis.append('nickname', 'OK')|向键为 nickname 的值后追加 OK|13，即修改后的字符串长度|
|substr(name, start, end=-1)|返回键为 name 的 string 的子串|name:键名<br>start:其实索引<br>end:终止索引，默认为-1，表示截取到末尾|redis.substr('name', 1, 4)|返回键为 name的值得字符串，截取索引为1-4的字符串|b'ello'|
|getrange(key, start, end)|获取键的 value 值从 start 到 end 的子字符串|key:键名<br>start:起始索引<br>end:终止索引|redis.getrange('name', 1, 4)|返回键为 name 的值得字符串，截取索引为1-4的字符串|b'ello'|



##### 列表操作
|方法|作用|参数说明|示例|示例说明|示例结果|
| :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
|rpush(name, \*values)|在键为 name的列表末尾添加值为 value 的元素，可以传多个| name:键名<br>values:值| redis.rpush('list', 1, 2, 3)|向键为 list 的列表尾添加1、2、3|3，列表大小|
|lpush(name, \*values)|在键为 name 的列表头添加值为 value 的元素，可以传多个|name:键名<br>values:值| redis.lpush('list', 0)|向键为 list 的列表头部添加0|4，列表大小|
|llen(name)|返回键为 name 的列表的长度|name:键名|redis.llen('list')|返回键为 list 的列表的长度|4|
|lrange(name, start, end)|返回键为 name 的列表中 start 到 end 之间的元素|name:键名<br>start:起始索引<br>end:终止索引|redis.lrange('list', 1, 3)|返回起始索引为1，终止索引为3的索引范围对应的列表|\[b'3', b'2', b'1'\]|
|ltrim(name, start, end)|截取键为 name 的列表，保留索引为 start 到 end 的内容|name:键名<br>start:起始索引<br>end:终止索引|ltrim('list', 1, 3)|保留键为 list 的索引1到3的元素|True|
|lindex(name, index)|返回键为 name 的列表中 index 位置的元素|name:键名<br>index:索引|redis.lindex('list', 1)|返回键为 list 的列表索引为1的元素|b'2'|
|lset(name, index, value)|给键为 name 的列表中index 位置的元素赋值，越界则报错|name:键名<br>index:索引位置<br>value:值|redis.lset('list', 1, 5)|将键为list 的列表中索引为1的元素赋值为5|True|
|lrem(name, count, value)|删除 count 个键的列表中值为 value 的元素|name:键名<br>count:删除个数<br>value:|redis.lrem('list', 2, 3)|将键为 list 的列表删除两个3|1，即删除的个数|
|lpop(name)|返回并删除键为 name 的列表中的首元素|name:键名|redis.lpop('list')|返回并删除键为 list 的列表中的第一个元素|b'5'|
|rpop(name)|返回并删除键为 name 的列表中的尾元素|name:键名|redis.rpop('list')|返回并删除键为 list 的列表中的最后一个元素|b'2'|
|blpop(keys, timeout=0)|返回并删除名称在 keys 中的列表中的首个元素，如果列表为空，则会一直阻塞等待|keys:键列表<br>timeout:超时等待时间，0为一直等待|redis.blpop('list')|返回并删除键为 list 的列表中的第一个元素|\[b'5'\]|
|brpop(keys, timeout=0)|返回并删除名称在 keys 中的列表中的尾元素，如果列表为空，则会一直注册等待|keys:键列表<br>timeout:超时等待时间，0为一直等待|redis.brpop('list')|返回并删除键为list 的列表中的最后一个元素|\[b'2'\]|
|rpoplpush(src, dst)|返回并删除名成为 src 的列表的尾元素，并将该元素添加到名称为 dst 的列表头部|src:源列表的键<br>dst:目标列表的键|redis.rpoplpush('list', 'list2')|将键为 list 的列表尾元素删除并将其添加到键为 list2的列表头部，然后返回|b'2'|

##### 集合操作
|方法|作用|参数说明|示例|示例说明|示例结果|
| :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
|sadd(name, \* values)|向键为 name 的集合中添加元素|name:键名<br>values:值，可为多个|redis.sadd('tags', 'Book', 'Tea', 'Coffee')|向键为 tags 的集合中添加 Book、Tea 和 Coffee 这三个内容|3，即插入的数据个数|
|srem(name, \*values)|从键为 name 的集合中删除元素|name:键名<br>values:值，可为多个|redis.srem('tags', 'Book')|从键为 tags 的集合中删除 Book|1，即删除的数据个数|
|spop(name)|随机返回并删除键为 name 的集合中的一个元素|name:键名|redis.spop('tags')|从键为 tags 的集合中随机删除并返回该元素|b'Tea'|
|smove(src, dst, value)|从 src 对应的集合中移除元素并将其添加到 dst 对应的集合中<br>|src:源集合<br>dst:目标集合<br>value:元素值|redis.smove('tags', 'tags2', Coffee)|从键为 tags 的集合中删除元素Coffee 并将其添加到键为 tags2的集合|True|
|scard(name)|返回键为 name 的集合的元素个数|name:键名|redis.scard('tags')|获取键为 tags 的集合中的元素个数|3|
|sismember(name, value)|测试 member 是否是键为 name 的集合的元素|name:键值|redis.sismember('tags', 'Book')|判断 Book 是否是键为 tags 的集合元素|True|
|sinter(keys, \*args)|返回所有给定键的集合的交集|keys:键列表|redis.sinter(\['tags', 'tags2'\])|返回键为 tags 的集合和键为 tags2的集合的交集|{b'Coffee'}|
|sinterstore(dest, keys, \*args)|求交集并将交集保存到 dest 的集合|dest:结果集合<br>keys:键列表|redis.sinterstore('inttag', \['tags', 'tags'\])|求键为tags 的集合和键为 tags2的集合的交集并将其保存为 inttag|1|
|sunion(keys, \*args)|返回所有给定键的集合的并集|keys:键列表|redis.sunion(\['tags', 'tags2'\])|返回键为 tags 的集合和键为 tags2的集合的并集|{b'Coffee', b'Book', b'Pen'}|
|sunionstore(dest, keys, \*args)|求并集并将并集保存到 dest 的集合|dest:结果集合<br>keys:键列表|redis.sunionstore('inttag', \['tags', 'tags2'\])|求键为 tags 的集合和键为 tags2的集合的并集并将其保存为 inttag|3|
|sdiff(keys, \*args)|返回所有给定键的集合的差集|keys:键列表|redis.sdiff(\['tags', 'tags2'\])|返回键为 tags 的集合和键为tags2的集合的差集|{b'Book', b'Pen'}|
|sdiffstore(dest, keys, \*args)|求差集并将差集保存到 dest 集合|dest:结果集合<br>keys:键列表|redis.sdiffstore('inttag', \['tags', 'tags2'\])|求键为 tags 的集合和键为 tags2的集合的差集并将其保存为 inttag|3|
|smembers(name)|返回键为 name 的集合的所有元素|name:键名|redis.smembers('tags')|返回键为 tags 的集合的所有元素|{b'Pen', b'Book', b'Coffee'}|
|srandmember(name)|随机返回键为 name 的集合中的一个元素，但不删除元素|name:键值|redis.srandmember('tags')|随机返回键为 tags 的集合中的一个元素|srandmember(name)|

#####  有序集合操作
|方法|作用|参数说明|示例|示例说明|示例结果|
| :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
|zadd(name, *args, *\*kwargs)|向键为 name 的 zset 中添加元素member，<br>score 用于排序。如果该元素存在，则更新其顺序|name:键名<br>args：可变参数|redis.zadd('grade', 100, 'Bob', 98, 'Mike')|向键为 grade的zset 中添加Bob(其 score 为100)，并添加 Mike（其 score 为98）|2，即添加的元素个数|
|zrem(name, \*values)|删除键为 name 的 zset 中的元素|name:键名<br>values:元素|redis.zrem('grade', 'Mike')|从键为 grade 的 zset 中删除 Mike|1，即删除的元素个数|
|zincrby(name, value, amount=1)|如果在键为 name 的 zset 中已经存在元素 value，则将该元素的 score 增加 amount；否则向该集合中添加该元素，其 score 的值为 amount|name:键名<br>value:元素<br>amount:增长的 score 值|redis.zincrby('grade', 'Bob', -2)|键为 grade 的 zset 中 Bob 的 score 减2|98.0，即修改后的值|
|zrank(name, value)|返回键为 name 的 zset 中元素的排名，按 score 从小到大排序，即名次| name:键名<br>value:元素值|redis.zrank('grade', 'Amy')|得到键为 grade 的zset 中Amy 的排名|1|
|zrevrank(name, value)|返回键为 name 的 zset 中元素的倒数排名（按 score 从大到小排序），即名次|name:键名<br>value:元素值|redis.zrevrank('grade', 'Amy')|得到键为 grade 的 zset 中 Amy 的倒数排名|2|
|zrevrange(name, start, end, withscores=False)|返回键为name的 zset（按从大到小排序）中 index 从 start 到 end 的所有元素|<br>name:键名<br>start:开始索引<br>end:结束索引<br>min:最低 score<br>max:最高 score<br>|redis.zrevrange('grade', 0, 3)|返回键为 grade 的zset 中前四名元素|\[b'Bob', b'Mike', b'Amy', b'James'\]|
|zrangebyscore(name, min, max, start=None, num=None, withscores=False)|返回键为 name 的 zset 中 score 在给定区间的元素|name:键名<br>min:最低score<br>max:最高 score<br>start:起始索引<br>num:个数<br>withscores:是否带 score|redis.zrangebyscore('grade', 80, 95)|返回键为 grade 的 zset 中 score 在80和95之间的元素|\[b'Bob', b'Mike', b'Amy', b'James'\]|
|zcount(name, min, max)|返回键为 name 的 zset 中 score 在给定区间的数量|name:键名<br>min:最低 score<br>max:最高 score|redis.zcount('grade', 80, 95)|返回键为 gradezset 中 score 在80到95的元素个数|2|
|zcard(name)|返回键为 name 的 zset 的元素个数|name:键名|redis.zcard('grade')|获取键为 grade 的 zset 中元素的个数|3|
|zremrangebyrank(name, min, max)|删除键为 ame 的 zset 中排名在给定区间的元素|name:键名<br>min:最低位次<br>max:最高位次|redis.zremrangebyrank('grade', 0, 0)|删除键为 grade 的 zset 中排名第一的元素|1，即删除的元素个数|
|zremrangebyscore(name, min, max)|删除键为 name 的 zset 中 score 在给定区间的元素|name:键名<br>min:最低score<br>max:最高 score|redis.zremrangebyscore('grade', 80, 90)|删除 score 在80到90之间的元素|1，即删除的元素个数|

##### 散列操作
|方法|作用|参数说明|示例|示例说明|示例结果|
| :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
|hset(name, key, value)|向键为 name 的散列表中添加映射|name:键名<br>key:映射键名<br>value:映射键值|hset('price', 'cake', 5)|向键为 price 的散列表中添加映射关系，cake 的值为5|1，即添加的映射个数|
|hsetnx(name, key, value)|如果映射键名不存在，则向键为 name 的散列表中添加映射|name:键名<br>key:映射键名<br>value:映射键值|hsetnx('price', 'book', 6)|向键为 price 的散列表中添加映射关系，book 的值为6|1，即添加的映射个数|
|hget(name, key)|返回键为 name 的散列表中各个键对应的值|name：键名<br>keys：映射键名列表|redis.hget('price', 'cake')|获取键为 price 的散列表中键名为 cake 的值|5|
|hmget(name, keys, \*args)|返回键为 name 的散列表中各个键对应的值|name： 键名<br>key：映射键名列表|redis.hmget('price', \['apple', 'orange'\])|获取键为 price 的散列表中 apple 和 orange 的值|\[b'3', b'7'\]|
|hmset(name, mapping)|向键为 name 的散列表中批量添加映射| name：键名<br>mapping：映射字典|redis.hmset('price', {'banana': 2, 'pear': 6})|向键为 price 的散列表中批量添加映射|True|
|hincrby(name, key, amount=1)|将键为 name 的散列表中映射的值增加 amount|name：键名<br>key：映射键名<br>amount：增长量|redis.hincrby('price', 'apple', 3)|key 为 price 的散列表中 apple 的值增加3|6，修改后的值|
|hexists(name, key)|键为 name 的散列表中是否存在键名为键的映射|name：键名<br>key：映射键名|redis.hexists('price', 'banana')|键为 price 的散列表中 banana 的值是否存在|True|
|hdel(name, \*keys)|在键为 name 的散列表中，删除键名为键的映射|name:键名<br>keys：映射键名|redis.hde('price', 'banana')|从键为 price 的散列表中删除键名为 banana 的映射|True|
|hlen(name)|从键为 name 的散列表中获取映射个数|name：键名|redis.hlen('price')|从键为 price 的散列表中获取映射个数|6|
|hkeys(name)|从键为 name 的散列表中获取所有映射键名|name：键名|redis.hkeys('price')|从键为 price 的散列表中获取所有映射键名|\[b'cake', b'book', b'banana', b'pear'\]|
|hvals(name)|从键为 name 的散列表中获取所有映射键值|name:键名|redis.hvals('price')|从键为 price 的散列表中获取所有映射键值|\[b'5', b'6', b'2', b'6'\]|
|hgetall(name)|从键为 name 的散列表中获取所有映射键值对|name:键名|redis.hgetall('price')|从键为 price 的散列表中获取所有映射键值对|{b'cake': b'5', b'book': b'6', b'orange': b'7', b'pear': b'8'}|

##### RedisDump
###### redis-dump导出数据
```python
Usage: redis-dump [global options] COMMAND [command options]
-u, --uri=S            Reis URI (e.g. redis://hostname:[:port])
-d, --database=S        Redis database (e.g. -d 15)
-s, --sleep=S        Sleep for S seconds after dumping (for debugging)
-c, --count=S         Chunk size (default: 10000)
-f, --filter=S        Filter selected keys (passed directly to redis'KEYS command)
-O, --without_optimizations        Disable run time optimizations
-V, --version         Display version
-D, --debug         Turn on debug
    --nosafe
```
###### redis-load导入数据
```python
redis-load --help
Try: redis-load [global options] COMMAND [command options]
-u, --uri=S        Redis URI (e.g. redis://hostname[:port])
-d， --database=S        Redis database (e.g. -d 15)
-s, --sleep=S        Sleep for S seconds after dumping (for debugging)
-n, --no_check_utf8        Don't check utf8
 -V, --version        Display version
-D, --debug        Turn on debug
--nosafe
```


## The End


# 学习路线已同步 github:[数据存储](https://github.com/VincentAdamNemessisX/DataStorage)




