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