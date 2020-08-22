# -*- coding:utf-8 -*-
import random
# 1부터 45 사이의 숫자 6개를 중복 없이 만들어서 리스트로 리턴하는 lotto()함수 만들기
# main 함수에서 호출하여 출력하자

def lotto():
    lotto = set()
    
    while len(lotto) <= 6:
        ran = random.randint(1, 45)
        lotto.add(ran)
        
    result = sorted(lotto)
    return result


if __name__ == '__main__':
    print(lotto())