'''
if문, 반복문은 영상만 참고하고 코드를 직접 작성하지는 않았습니다
'''

print("<챕터01 - 기본값>")
def profile(name, age, main_lang):
  print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}\
        ".format(name, age, main_lang))
  
profile("유재석", 20, "자바")

print("같은 학교 같은 학년 같은 반 같은 수업")
def profile2(name, age=17, main_lang="파이썬"):
  print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}\
        ".format(name, age, main_lang))
  
profile2("유재석")
profile2("김태호")
print()

print("<챕터02 - 키워드값>")
# 파라미터의 순서가 바뀌어도 키워드대로 따라감
profile(name="유재석", main_lang="파이썬", age=24)
print()

print("<챕터03 - 가변인자>")
# 여러개가 있을 경우 변수앞에 *
def profile3(name , age, *language):
  print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
  for lang in language:
    print(lang, end=" ")
  print()

profile3("유재석", 20, "파이썬", "자바", " 씨", "코틀린", "스위프트")
profile3("김태호", 25, "자바", "씨")
print()

print("<챕터04 - 지역변수, 전역번수>")
# global을 사용하여 전역변수를 사용