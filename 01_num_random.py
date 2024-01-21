'''
2024-01-22
파이썬 기초
'''
print('<챕터01 - 연산자>')
print(2**3) # 2^3=8
print(10//3) # 10을 3으로 나눈 몫 = 3
print()

'''
and == &
or == |
'''
print('<챕터02 - 숫자함수>')
print(pow(4, 2)) # 4^2 = 16
print(round(3.14)) #반올림하여 3
print()

from math import *
print(floor(4.99)) # 내림
print(ceil(3.14)) # 올림
print(sqrt(16)) # 제곱근
print()

print('<챕터03 - 렌덤함수>')
from random import *
print(random())
print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(int(random() * 10))
print(int(random() * 10))
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 정수 생성

print()
print('---로또---')
print(randrange(1, 46)) # 1~46 미만의 임의의 값 생성
print(randrange(1, 46)) # 1~46 미만의 임의의 값 생성
print(randrange(1, 46)) # 1~46 미만의 임의의 값 생성
print(randrange(1, 46)) # 1~46 미만의 임의의 값 생성
print(randrange(1, 46)) # 1~46 미만의 임의의 값 생성
print(randrange(1, 46)) # 1~46 미만의 임의의 값 생성
print(randrange(1, 46)) # 1~46 미만의 임의의 값 생성
print()

print('---로또---')
print(randint(1, 45)) # 1~45 미만의 임의의 값 생성
print(randint(1, 45)) # 1~45 미만의 임의의 값 생성
print(randint(1, 45)) # 1~45 미만의 임의의 값 생성
print(randint(1, 45)) # 1~45 미만의 임의의 값 생성
print(randint(1, 45)) # 1~45 미만의 임의의 값 생성
print(randint(1, 45)) # 1~45 미만의 임의의 값 생성