# -*- coding:utf-8 -*-

from pymongo import MongoClient

client = MongoClient('localhost',27017)
db = client.test
score = db.score

# {name : 자기이름, kor:?, eng:?, math:?} 등록하자.
result01 = score.insert_one({'name': '박진우', 'kor':100, 'eng':100, 'math':15})
print(result01.inserted_id)

result02 = score.insert_many([
    {
        'name':'한지용',
        'kor': 100,
        'eng': 100,
        'math':100
    },
    {
        'name':'강여림',
        'kor':90,
        'eng':90,
        'math':90
        
    },
    {
         'name':'김지후',
        'kor':80,
        'eng':80,
        'math':80
    },
    {
         'name':'위영석',
        'kor':70,
        'eng':70,
        'math':70
    }
    ])

print(result02.inserted_ids)

