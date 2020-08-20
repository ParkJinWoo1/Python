# -*- coding:utf-8 -*-

i = 1

while i <= 10:
    if i > 5:
        break
    print(i, end= ' ')
    i += 1
else :
    print('i', i, sep='=')

print()

for i in range(1,11):
    if i % 2 == 0:
        continue
    print(i, end= ' ')
else :
    print('i', i, sep='=')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
######################
# while의 실행결과 :
# for의 실행결과 :