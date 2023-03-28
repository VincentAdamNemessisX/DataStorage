"""
# File       : MongoDBStorage.py
# Time       : 7:27 AM
# Author     : vincent
# version    : python 3.8
# Description:
"""
import pymongo
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
# print(result)


