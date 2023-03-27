"""
# File       : databaseStorage.py
# Time       : 12:22 PM
# Author     : vincent
# version    : python 3.8
# Description:
"""
import pymysql
import pymongo

# mysql database
# db = pymysql.connect(host='localhost', user='root', password='root', port=3333, db='spiders')
# cursor = db.cursor()
#
# # make sure mysql connect successful and create database
# cursor.execute('Select version()')
# data = cursor.fetchone()
# print('Database Version:', data)
# cursor.execute("Create Database if not exists spiders Default CHARACTER SET utf8")
#
# # create table
# cursor.execute("Create Table if not exists students"
#                "(id varchar(255) not null,"
#                "name varchar(255) not null,"
#                "age int not null,"
#                "primary key (id))")
#
# # insert data
# # id = '2012042141'
# # user = 'bob'
# # age = 20
# # sql = 'Insert into students(id, name, age) values (%s, %s, %s)'
# # try:
# #     cursor.execute(sql, (id, user, age))
# #     db.commit()
# # except:
# #     db.rollback()
#
# # insert data next generation method
# data = {
#     'id': '2012424234',
#     'name': 'Bug',
#     'age': 30
# }
# table = 'students'
# keys = ','.join(data.keys())
# values = ','.join(['%s'] * (len(data)))
# sql = 'Insert into {table}({keys}) values ({values})'.format(table=table, keys=keys, values=values)
# try:
#     if cursor.execute(sql, tuple(data.values())):
#         print('Insert successful')
#         db.commit()
# except:
#     print("Insert failed")
#     db.rollback()
#
# # update data to mysql
# data = {
#     'id': '2012424234',
#     'name': 'bbbb',
#     'age': 21
# }
# table = 'students'
# keys = ','.join(data.keys())
# values = ','.join(['%s'] * len(data))
# sql = 'Insert into {table}({keys}) values ({values}) on duplicate key update '\
#     .format(table=table, keys=keys, values=values)
# update = ','.join(["{key} = %s".format(key=key) for key in data])
# sql += update
# try:
#     if cursor.execute(sql, tuple(data.values()) * 2):
#         print('Update successful')
#         db.commit()
# except:
#     print("Update failed")
#     db.rollback()
#
# # delete data from table that in database of mysql
# # table = 'students'
# # condition = 'age > 20'
# # sql = 'Delete from {table} where {condition}'.format(table=table, condition=condition)
# # try:
# #     cursor.execute(sql)
# #     print('Delete successful')
# #     db.commit()
# # except:
# #     print('Delete failed')
# #     db.rollback()
#
# # query data from table that in database of mysql
# table = 'students'
# condition = 'age >= 20'
# sql = 'select * from {table} where {condition}'.format(table=table, condition=condition)
# try:
#     cursor.execute(sql)
#     print('Count', cursor.rowcount)
#     row = cursor.fetchone()
#     while row:
#         print('Row', row)
#         row = cursor.fetchone()
# except:
#     print('Query with error!')
# db.close()
