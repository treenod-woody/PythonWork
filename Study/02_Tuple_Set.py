# # 튜플은 리스트의 내용을 변경할 수 없음
# tuple_val = (1, 2, 3)
# set_val = {1, 2, 3, 3, 3}
# print(set_val)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합(java와 python을 모두 할 수 있는 사람)
print(java & python)
print(java.intersection(python))

# 합집합(java 또는 python 중 하나라도 할 수 있는 사람)
print(java | python)
print(java.union(python))

# 차집합(java만 할 수 있는 사람)
print(java - python)
print(java.difference(python))

# set에 값 추가하기
python.add("김태호")

# set에 값 제거하기
java.remove("김태호")