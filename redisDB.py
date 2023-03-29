"""
# File       : redisDB.py
# Time       : 6:53 PM
# Author     : vincent
# version    : python 3.8
# Description:
"""
from redis import StrictRedis, ConnectionPool, Redis

# redis connect
# redis = StrictRedis(host='8.130.73.157', port=6379, db=0, password='ic34')
# redis.set('name', 'Bob')
# print(redis.get('name'))
# redis.close()

# redis connection pool
url = 'redis://:ic34@8.130.73.157:6379/0'  # redis: //:password@host:port/db_number
# url = 'redis://[:ic34]@8.130.73.157:6379/0'  # redis: //:redis: //:[password]@host:port/db_number
# url = 'unix://[:ic34]@8.130.73.157:6379/to/socket.sock?db=0' # redis: //:redis:  //:[password]@/path/to/socket.sock?db=db
pool = ConnectionPool.from_url(url)
# pool = ConnectionPool(host='8.130.73.157', port=6379, db=0, password='ic34')
redis = Redis(connection_pool=pool)
redis.set('hello', 'world!')
print(redis.get('hello'))




redis.close()