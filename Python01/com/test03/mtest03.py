# -*- coding:utf-8 -*-

# 1. for문을 사용하여 구구단을 전체 출력하는 함수 gugu()를 작성하고,
#    main함수에서 호출하자.
def gugu():
    print('구구단')
    for i in range(2,10):
        print('<<%d단>>' % i)
        for j in range(1,10):
            print('%d x %d = %d' %(i, j, i*j))
        print()


# 2. while문을 사용하여 구구단 중 파라미터로 전달된 단만 출력하는 함수 gugudan(x)를
#    작성하고, main 함수에서 콘솔을 통해 n을 입력받아 호출하자.
def gugudan(x):
    print('<<',x,'단>>')
    i = 1
    while i < 10:
        print('{} x {} = {}'.format(x, i, int(x) * i))
        i += 1
    print()
        

if __name__ == '__main__':
    gugu()
    print('-----------')
    n = input('dan : ')
    gugudan(n)