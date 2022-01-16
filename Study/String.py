# val = 'Hello world~ I love Python! I like pizza.'

# newlist = val.split()   # 빈 칸을 기준으로 리스트 생성
# print(newlist)

txt = '     abcde     fghij     '
print('>' + txt.strip() + '<')  # 좌우측끝 공백 제거
print('>' + txt.lstrip() + '<')  # 좌측끝 공백 제거
print('>' + txt.rstrip() + '<')  # 우측끝 공백 제거
print('>' + txt.strip('a ') + '<')  # a를 제거하려면 a 와 공백을 함께 써줘야 제거됨