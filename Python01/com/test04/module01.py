# -*- coding:utf-8 -*-

import math

def circle(r):
    return math.pi * r * r
    

if __name__ == '__main__':
    r = int(input('원의 반지름  : '))
    print('반지름이 {} 인 원의 넓이는 {} 입니다.'.format(r, circle(r)))