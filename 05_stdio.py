print("챕터01 - <표준출력>")

print("Python", "Java", sep=",")
print("Python", "Java", sep=",", end="?")
print()

import sys
print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)

# 시험성적

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
  print(subject.ljust(8), str(score).rjust(4), sep=":")
  #과목은 8칸 공간 확보 후 왼쪽 정렬, 점수는 4칸 공간 확보 후 오른쪽 정렬, :로 구분

# 은행 대기순번표
# 001, 002, 003, ....
for i in range(1,21):
  print("대기번호 : " + str(i).zfill(3))
print()

'''
print("챕터02 - <표준입력>")
answer = input("아무값이나 입력하세요 : ")
print("입력하신 값은 " + answer + "입니다")
print()
'''

print("챕터03 - <다양한 출력 포맷>")
print("빈 자리는 빈공간으로 두고, 오른쪽 정렬, 총 10자리 공간 확보")
print("{0: >10}".format(4723))
print("양수일 때는 +로 표시, 음수일때는 -로 표시")
print("{0: >+10}".format(4723))
print("{0: >+10}".format(-4723))
print("왼쪽 정렬, 빈칸을 _로 채움")
print("{0:_<10}".format(500))
print("3자리 마다 콤마를 찍어주기")
print("{0:,}".format(1000000000000))
print("3자리 마다 콤마를 찍어주기, +- 부호도 붙이기")
print("{0:+,}".format(1000000000000))
print("3자리 마다 콤마를 찍어주기, +- 부호도 붙이기, 자릿수 확보, 빈 자리는 ^로 채우기")
print("{0:^<+20,}".format(1000000000000))
print("소수점 출력")
print("{0:f}".format(5/3))
print("소수점 특정 자리수 까지만 출력")
print("{0:.2f}".format(5/3))
print()

print("챕터04 - <파일 입출력>")
# score_file = open("score.txt", "w", encoding="utf8") # w는 쓰기를 의미
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close() # 파일을 열었으면 항상 닫아주어야함

# score_file = open("score.txt", "a", encoding="utf8") # a는 기존 파일에 이어서 쓰는 것을 의미
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100") # write()를 쓰면 자동으로 줄바꿈이 안됨
# score_file.close()

# # 전체파일 한번에 읽기
# score_file = open("score.txt", "r", encoding="utf8") # r은 읽기를 의미
# print(score_file.read())
# score_file.close()

# # 파일 한줄씩 읽기
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# # 파일 한줄씩 읽는데 파일이 총 몇줄인지 모를때
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#   line = score_file.readline()
#   if not line:
#     break
#   print(line)
# score_file.close()

# # 파일 한줄씩 읽는데 파일이 총 몇줄인지 모를때
# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() # list 형태로 저장
# for line in lines:
#   print(line, end="")
# score_file.close()

print()

print("챕터05 - <피클>")
import pickle
# # 쓰기
# profile_file = open("profile.pickle", "wb") # wb는 write binary 피클에서는 바이너리를 사용해야함
# profile = {"이름":"박명수", "나이":48, "취미":["축구", "골프", "베이스"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# profile_file.close()

# # 읽기
# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

print()

print("챕터06 - <with>")
# 파일을 열고 처리하고 닫는 과정을 with를 사용하여 좀 더 편하게 할 수 있음

with open("profile.pickle", "rb") as profile_file:
  print(pickle.load(profile_file))
# close를 쓸 필요없이 with문을 탈출하면서 자동으로 종료
  
with open("study.txt", "w", encoding="utf8") as study_file:
  study_file.write("파이썬을 공부하고 있어요")

with open("study.txt", "r", encoding="utf8") as study_file:
  print(study_file.read())

print()

print("챕터07 - <퀴즈>")
for i in range (1,11):
  with open(str(i) + "주차.txt", "w", encoding="utf8") as weekly_file:
    print("- " + str(i) + " 주차 주간보고 -")
    print("부서 : ")
    print("이름 : ")
    print("업무 요약 : ")

  with open(str(i) + "주차.txt", "r", encoding="utf8") as weekly_file:
    print(weekly_file.read())


