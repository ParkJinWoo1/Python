# 문자(single quotation / double quotation 의 차이 없음)

# single * 1
a = 'python\'s\nHello, World!'  #escape
print(a)
# single * 3
b = '''python's
Hello, World!        !!!!
    Hello, python'''
print(b)



# double * 1
c = "python's\n\"Hello, World!\""
print(c)

# double * 3
d = """python's
"Hello, World!" """
print(d)


e = "c:\\test"
print(e)
# raw String : \를 문자로 인식
f = r"c:\test"
print(f)

str01 = "Hello ,"
str02 = "World!"
print(str01 + str02)
print(str01 * 3 + str02)
















