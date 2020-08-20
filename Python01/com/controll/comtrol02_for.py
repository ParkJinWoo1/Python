# -*- coding:utf-8 -*-

subject = ['java', 'javascript', 'python']

for i in subject:
    print(i, end= ' ')
else :
    print('재밌다.')
    
for i in range(1, 100):
    print(i, end= '+')
    
    
print('\n구구단')
for i in range(2, 10):
    for j in range(1,10):
        print('{} x {} = {}'.format(i, j, i*j))


print('-----')
for i in range(1, 11):
    print(i, end= ' ')
print()
for i in range(10, 0, -1):
    print(i,end= ' ')