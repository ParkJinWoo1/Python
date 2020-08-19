# -*- coding:utf-8 -*-

# 산술연산
a = 21
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a ** b)   # a의 b제곱
print(a / b)
print(a // b)   # 몫 (floor division)
print(a % b)    # 나머지 (modulo)

# 비교 연산
a, b = 3, 5
print(a == b)
print(a != b)
print(a > b)
print(a <= b)
print(a is b)
print(a is not b)

print('-------')
print(True or False)
print(False and True)
print(not False)

# 범위연산
lst = list(range(100))
print(lst)
print(lst[2])
print(lst[12:49])   # 12 ~ 48
print(lst[12: 49: 3])   # 3씩 뛰어넘음
# [start : end] -> start ~ end-1
# [start : end: step] -> start ~ end-1 까지 step만큼 뛰면서 출력

str01 = 'Hello World!'  # 순서가 있는 값
print(str01)
print(str01[0])
print(str01[0:5])
print(str01[6:11])
print(str01[0: 4] * 4)

# reverse
print(str01[-1])
print(str01[-1: ])
print(str01[: -1])
print(str01[:: -1]) #처음부터 끝까지 -1씩 출력해라 -> 거꾸로 출력

# 멤버 연산
lst02 = [0,1,2,3,4,5]
print(3 in lst02)
print(5 not in lst02)
print(7 not in lst02)







