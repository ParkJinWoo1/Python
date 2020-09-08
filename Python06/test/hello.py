# -*- coding:utf-8 -*-

from pymongo import MongoClient
# pymongo 로부터 임포트했다

# MongoDB와 연결
# client = MongoClient('127.0.0.1', 27017)
client = MongoClient('mongo://localhost:27017')
# 몽고디비랑 연결할거야 ip주소가 'localhost =127.0.0.1'이거인 애랑

# 연결된 client에서 db와 연결
# db = client.test
db = client['test']


# 연결된 db에서 collection 가져오기
# collection = db.score
collection = db['score']

for doc in collection.find():
    print(doc)
