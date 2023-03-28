"""
# File       : MongoDBStorage.py
# Time       : 7:27 AM
# Author     : vincent
# version    : python 3.8
# Description:
"""
import pymongo
from bson import ObjectId

client = pymongo.MongoClient("mongodb+srv://"
                             "vincent:ZTXic3344"
                             "@tempcluster.kslgvab.mongodb.net/"
                             "?retryWrites=true&w=majority")
# select or create database
db = client.test
# db = client['test']  # equals last method

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
# result = collection.insert_one(student)
# print(result)

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
# result = collection.insert_many([student1, student2, student3])
# print(result.inserted_ids)

# query data
# result = collection.find_one({'name': 'Jordan'})
# print(type(result))
# print(result)
# result = collection.find_one({'_id': ObjectId('6422a9e61bec7b1f2abe36db')})
# print(result)
# result = collection.find({'age': '30'})
# print(type(result))
# for item in result:
#     print(item)
# result = collection.find({'age': {'$gt': '10'}})
# print(type(result))
# for item in result:
#     print(item)

# count number
# 构建聚合查询管道
pipeline = [
    {'$group': {'_id': None, 'count': {'$sum': 1}}}
]
# 执行聚合查询，并获取文档数量
# result = collection.aggregate(pipeline)
# count = result.next()['count']
# print(count)

# sort data
# results = collection.find().sort('name', pymongo.ASCENDING)
# print([rst['name'] for rst in results])  # 列表推导式

# offset
# results = collection.find().sort('name', pymongo.DESCENDING).skip(1)
# print([result['name'] for result in results])
# results = collection.find().sort('name', pymongo.DESCENDING).skip(1).limit(1)
# print([result['name'] for result in results])
# results = collection.find({'_id': {'$gt': ObjectId('6422a9e61bec7b1f2abe36db')}})
# print([(result['name'], result['age']) for result in results])

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

