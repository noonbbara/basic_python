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
cabinet = {3:"유재석", 100:"김태호"}
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