# cabinet = {3:"유재석", 100:"김태호"}

# # 값이 없으면 에러를 띄우고 다음 라인을 실행하지 않음
# print(cabinet[3])

# # 값이 없으면 None을 출력하고 다음 라인을 실행함
# print(cabinet.get(5))
# print(cabinet.get(5, "사용 가능함"))    # None 대신에 디폴트 값을 입력하고자 할 경우
# print(cabinet.get(100))

# # 값이 Dictionary 안에 있는지를 확인
# cabinet = {3:"유재석", 100:"김태호"}

# print(3 in cabinet) # True
# print(5 in cabinet) # False

# # 딕셔너리에 값을 추가하는 방법
# cabinet = {3:"유재석", 100:"김태호"}
# cabinet[5] = "조세호"
# print(cabinet)

# # 딕셔너리에서 값을 제거하는 방법
# cabinet = {3:"유재석", 100:"김태호"}
# del cabinet[3]
# print(cabinet)

# 모든 키값 또는 밸류값만 출력, 키밸류 모두 출력
cabinet = {3:"유재석", 5:"정형돈", 100:"김태호"}
print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())