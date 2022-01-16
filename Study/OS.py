import os

# 폴더 생성하기
# try:
#     os.mkdir('python')
#     print('폴더를 만들었습니다.')
# except FileExistsError as e:
#     print(e)

# 폴더 삭제하기
try:
    os.rmdir('python')
    print('폴더를 만들었습니다.')
except FileExistsError as e:
    print(e)
