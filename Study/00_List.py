# # 리스트
# subway = ["유재석", "조세호", "박명수"]

# # 인덱스값 추출
# print(subway.index("조세호"))

# 마지막 인덱스에 리스트 추가
# subway.append("하하")

# # 지정한 인덱스 자리에 리스트를 추가하고 나머지를 뒤로 밀음
# subway.insert(1, "정형돈")

# # 리스트에서 뒤에서부터 하나씩 꺼냄
# print(subway.pop()) # 마지막에 꺼낸 값을 출력
# print(subway)       # 꺼내고 남은 리스트를 출력

# # 같은 값이 몇개나 있는지 확인
# subway.append("유재석")
# print(subway.count("유재석"))

# 순서대로 정렬하기
# num_list = [5,2,3,1,4]
# num_list.sort()
# print(num_list)

# # 순서 뒤집기
# num_list.reverse()
# print(num_list)

# # 모든 리스트 제거
# num_list.clear()
# print(num_list)

# 리스트 확장하기
num_list = [5,2,3,1,4]
mix_list = ["조세호", 20, True]
num_list.extend(mix_list)
print(num_list)