# 2020/08/19 시험 정리

> **Python** : 크롤링(스크래핑은 별개), 임베디드, ai, 빅데이터, 통계 / 금융, 웹.. 등등 다 할 수 있음.
>
> ​	모든 애들이 객체로 이루어져있어. INTERPRETER언어임. 한줄씩 읽을거야.
> 얘넨 OOP임 (객체지향)
> **Number, String, List[] ,  Tuple**(list랑 똑같이 값 저장 가능한데 한번 만들어지면 수정x 추가,삭제도
> **Dictionary** {k:v}형태임. (Map, JSON)
>
> 
>
> #### 파이썬 타입
>
> - **Number, String List[], Tupe, Dictionary**
>
>
> **츨력**
>
> - if x > y
>
>   ​     print(y);
>
>  
>
> ## **구구단**
>
> ```python
> 	for  [변수]   in     [범위, 혹은 객체]
> 
> for i in range(2, 10):
>      for j in range(1, 10):
> 	     print('{} * {} = {}'.format(i, j, ixj))
> 
>  a = set(['1','2','3','a','b','c'])
>  b = {'a', 'b', 'c', 'd', 'e', 'f'}
> 
> print(a.intersection(b))
> 
> 해설 ] intersection = 교집합을 뜻한다
> {'a', 'b', 'c'}
> ```
>
> 
>
>   
>
> #### 자르기
>
> ```python
> lst = list(range(1, 10))
> 
> print (lst[4:7])
> 
> 해설 ] 1부터 10중에 5,6,7 구하기
> ```
>
> 
>
>  
>
> ### 값 구하기
>
> ```python
> arr = ['1', '2', '3', '4']
> '+'.join(arr) => '1+2+3+4'
> print(eval('+'.join(arr)))
> 
>  = 10 
> ```
>
> 
>
>  
>
> ###  정규식
>
> [0-9] : 0부터 9까지
> r문자 표기법 -> \d
>
>  
>
>  def mysum(x, y):
> 	return 2* x + y
> 위의 식(함수) 아래(익명함수)로
>
> lambda x, y: 2*x + y
>
>   
>
>  'a' : 파일의 기존 내용 이후에 내용 작성할 수 있음
>
> **pickling(pickle) :** 
> 파이썬 객체를 파일에 저장하기 위한 직렬화. 객체 -> 파일
>
> **unpickling(unpickle) :**
> 파일에 저장되어있는 객체를 파이썬으로 로딩하기 위한 역직렬화.
> 파일 -> 객체
>
>   
>
> ```python
>  i = 1
> while i <= 10:
> 	if i > 5
> 		break
> 	print(i, end=' ')
> 	i += 1
> else :
> 	print('i=' , str(i))
> 
> = 1 2 3 4 5
> 해설 ] while문이 정상적으로 종료됐을 떄 else가 실행이 된다. 위와 같은 경우에는 정상적으로 종료한게 아니라 특정 값에서 멈췄기 떄문에 else문은 돌지 않고 5까지만 나온다.
> ```
>
> 
>
>
> ```python
> for i in range(1, 10):
> 	if i%2 == 0:
> 		continue
> 	print(i)
> else :
> 	print('i=', i)
> 
> =1 3 5 7 9 i = 9
> 해설 ] 정상적으로 for문이 끝났기 떄문에 else문이 실행이 되서 i=9까지 출력
> ```
>
> 
>
> 
>
>
> 서술형문제 4문제 / 평가자체크리스트문제 : 
>
> 
>
>  
>
> ## **피보나치 수열 :**
>
> ```python
> n = int(input('n : '))
> a, b = 0, 1
> while a < n:
> 	print(a, end=' ')
> 	a, b = b, a + b
> 
> 해설 ] input은 내가 입력할 값이고 String으로 들어오기때문에 int로 형변환.
> ```
>
> 
>
> ### 
>
> ```python
> def fibo(n) :
> 	n = int(input('n : '))
> 		a, b = 0, 1
> 	while a < n:
> 		print(a, end=' ')
> 		a, b = b, a + b\
> 
> 해설 ] 위의 코드를 함수로 만들었어
> ```
>
> 
>
>  
>
> ```python
> n = int(input (' n : '))
> res = list()
> a, b = 0, 1
> while a < n:
> 	res.append(a)
> 	a, b = b, a + b
> 
> 해설 ] 입력받은 값을 String이기 때문에 int로 형변환 해주고 list에 담아서 처리하자
> ```
>
> 
>
> ```python
> def fibo2(n)
> 	res = list()
> 	a, b = 0, 1
> 	while a < n:
> 		res.append(a)
> 		a, b = b, a + b
> 	return res;
> 
> 
> 해설 ] 위에  list로 fibonachi로 만든걸 함수로 만들어준다.
> ```
>
> 
>
> 
>
> ```python
> if__name__=="__main__": 
> 	n = int(input('n value :  '))
> 	fibo1(n)
> 	print(fibo2(n))
> 	
> 	
> 해설] if__name__=="__main__": 의 뜻은 메인함수라는 뜻.
> ```
>
> 
>
>  
>
>   
>
>  
>
>  
>
>  
>
>  
>
> 