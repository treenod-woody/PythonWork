import shutil
import re
import os

root = "C:/hwpTest"

# 파일 리스트 숫자 기준으로 정렬된 리스트 리턴
def fileListSort(dirPath) :

    
    numbers = []    # 모든 회차 정보
    fileNames = []
    first_name = ""
    last_name = ""

    fileList = os.listdir(root)

    for f in fileList:  # 파일에서 숫자값만 추출해서 정렬
        # N화를 모두 추출한 후 숫자만 남김 -----------
        # regex = re.compile(r'\d+\w')
        # mo = regex.search(f).group()
        num = re.findall(r'\d+', f)[-1]    # 마지막 숫자값만 가져옴
        numbers.append(int(num))

        first_name = f.split(str(num))[0]
        last_name = f.split(str(num))[1]

    numbers.sort()

    for n in numbers:   # 파일 이름 재정렬
        full_name = first_name + str(n) + last_name
        fileNames.append(full_name)

    return fileNames

filelist = fileListSort(root)
print(filelist)
