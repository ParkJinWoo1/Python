# -*- coding:utf-8 -*-

import pickle

file = open('test02.txt', 'rb')
score = pickle.load(file)
file.close()

print(score)




