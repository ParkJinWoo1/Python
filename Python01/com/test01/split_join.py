# -*- coding:utf-8 -*-

import re


# split
str01 = 'Hello, World!\nHello, Python!'
print(str01)

arr01 = str01.split(' ')   #list로 return
print(arr01)

arr02 = str01.split(' ', 1)
print(arr02)

arr03 = re.split("[\s]|[,]", str01)
print(arr03)

# join
arr04 = ['1','2','3','4']
print(arr04)
a = '+'.join(arr04)
print(a)

print(eval(a))








