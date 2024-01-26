print("<챕터01 - 리스트>")
num_list = [3,2,5,4,1]
num_list.sort()
print(num_list)
num_list.reverse()
print(num_list)
num_list.clear()
print(num_list)

num_list = [3,2,5,4,1]

print("리스트에는 다양한 자료형이 들어 갈 수 있습니다")
mix_list = ["사과", 20, True]

#리스트 확장
num_list.extend(mix_list)
print(num_list)
print()

print("<챕터02 - 딕셔너리>")
print("key : value로 구성")
print("키는 중복 불가능")
cabinet = {3:"유재석", 100:"김태   호"}
print(cabinet[3]) # 키에 맞는 값을 출력
print(cabinet.get(3))
print(cabinet.get(5, "사용가능"))

print(3 in cabinet)
print(5 in cabinet)

# 추가
cabinet[50] = "김종국"
print(cabinet)

#삭제
del cabinet[50]
print(cabinet)

# key 들만 출력
print(cabinet.keys())
# value 들만 출력
print(cabinet.values())
# key, values 쌍으로 출력
print(cabinet.items())

#모두 삭제
cabinet.clear()
print(cabinet)
print()

print("<챕터03 - 튜플>")
print("튜플은 내용의 변경이나 추가가 불가능, but 속도 좀 더 빠름")
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)
print()

print("<챕터04 - 집합(set)>")
print("중복 안됨, 순서없음")
my_set = {1,2,3,3,3,}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

#교집합 : 자바와 파이썬을 모두 할 수 있는 개발자 출력
print(java & python)
print(java.intersection(python))

#합집합 : 자바와 파이썬 중 하나라도 할 수 있는 개발자
print(java | python)
print(java.union(python))

#차집합 : 자바를 할 수 있지만 파이썬은 할 줄 모르는 개발자
print(java - python)
print(java.difference(python))

#파이썬을 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

#자바를 까먹음
java.remove("김태호")
print(java)
print()

print("<챕터05 - 자료구조의 변경>")
#커피숍
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))
print()

print("<챕터06 - 퀴즈>")
from random import *
users = range(1, 21) # 1부터 20까지 숫자를 생성
users = list(users)
print(users)

winners = sample(users, 4)

print("---당첨자 발표---")
print("치킨 당점자 : {0}".format(winners[0]))
print("커피 당점자 : {0}".format(winners[1:]))