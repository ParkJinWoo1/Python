# -*- coding:utf-8 -*-
i = 1

while i <= 10:
    print(i)
    i += 1
    #python 에는 증감연산자가 없다 (++, --)
    
# 1 ~ 10 까지의 총 합계 출력
mysum = 0
mycnt = 1
while mycnt <= 10:
    mysum += mycnt
    mycnt += 1
else :
    print('sum', mysum, sep='=')
    print('cnt', mycnt, sep='=')
    