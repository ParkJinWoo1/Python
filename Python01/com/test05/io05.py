# -*- coding:utf-8 -*-

import pickle


score = {'name': 'kh', 'kor': 100, 'eng': 99, 'math': 56}
with open('test02.txt', 'wb') as file:
    pickle.dump(score,file)


