# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request       # 파이썬 내부에 가지고 있는 라이브러리를 요청한다

resp = urllib.request.urlopen('https://movie.naver.com/movie/running/current.nhn')
# print(resp)
soup = BeautifulSoup(resp, 'html.parser')
# print(soup)

movies = soup.find_all('dl', class_='lst_dsc')
# print(movies)
# print(movies[0])


# 제목과 별점만 출력하자.
# print(soup.find('dt',class_='tit').find('a'))
# print(soup.find('div', class_='star_t1').find('span',class_='num'))

for movie in movies:
    title = movie.find('a').text
    star = movie.find('span', class_='num').text
    print('{} [{}]'.format(title, star))