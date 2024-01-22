print('<챕터01 - 슬라이싱>')

id = '011226-3959293'
print('성별 : ' + id[7])
print('연 : ' + id[0:2]) # 0부터 2 직전까지
print('월 : ' + id[2:4]) # 2부터 4 직전까지

print('뒤 7자리 (뒤에부터) : ' + id[-7:])
#맨 뒤에서 7번째 부터 끝까지
print()

print('<챕터02 - 문자열 포맷>')
# 방법 1
print('나는 %d살입니다' %24)
print('나는 %s을 좋아해요' %'파이썬')
print('나는 %s색과 %s색을 좋아해요' % ('파란', '빨간'))
print()

# 방법 2
print('나는 {}살 입니다'.format(20))
print('나는 {}색과 {}색을 좋아해요'.format('파란', '빨간'))
print('나는 {1}색과 {0}색을 좋아해요'.format('파란', '빨간'))
print()

# 방법 3
print('나는 {age}살이며, {color}색을 좋아해요'.format(age=24, color='빨간'))
print()

# 방법 4
age = 20
color = '빨간'
print(f'나는 {age}살이며, {color}색을 좋아해요')
print()

print('<퀴즈>')
url = "http://naver.com"
my_str = url.replace("http://","")
my_str = my_str[:my_str.index(".")]
print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print(password)