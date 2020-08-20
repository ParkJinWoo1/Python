# -*- coding:utf-8 -*-
'''
*
**
***
****
*****
'''

for i in range(1,6):
    print('*'*i)
        
'''
*****
****
***
**
*
'''
print()
   
for i in range(1,6):
    print('*'*(6-i))



'''
    *
   **
  ***
 ****
*****
'''

print()

for i in range(5):
    print(' '* (4 - i) + '*' * (i + 1))

'''
*****
 ****
  ***
   **
    *
'''

print()

for i in range(5):
    print(' '*(i) + '*' * (5 - i))



'''
     *
    ***
   *****
  *******
 *********
***********
'''
print()

for i in range(5):
    print(' ' * (4 - i) + '*' * (2 * i + 1))


