import os
import shutil

# 저장 폴더가 존재한다면 제거한후 다시 생성하기
def folderMake(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        shutil.rmtree(path)
        os.mkdir(path)

# 데이터의 마지막 라인의 텍스트 추출하기
def endTextLine(path, start_index, end_index, sub_data, number):
    reverseData = sub_data[::-1]
    firstIndex = end_index - start_index - reverseData.find('\n', 0)
    end_text = sub_data[firstIndex:end_index]

    if len(end_text) < 10:
        logTxt = f'{str(number)}.txt 파일 이상 발견 : ' + str(len(end_text)) + '\n' + end_text + '\n----------------------------------------------------------\n'
        fileMake(path, 'a', logTxt)
    else:
        logTxt = ''

    return end_text

# 파일 생성 또는 수정
def fileMake(path, state, content):
    with open(path, state, encoding="utf8") as file:
        file.write(content)

# 00.txt 원본 파일의 내용 읽어오기
try:
    with open("TextSplitter/00.txt", "r", encoding="utf8") as source_file:
        data = source_file.read()
        source_file.close()
except FileExistsError:
    print("00.txt 파일이 존재하지 않습니다.")

# final 디렉토리 생성하고 로그파일 생성  -------------------------------------------
dir = "TextSplitter/final"
logfile = dir + "/00_log.txt"
folderMake(dir)
fileMake(logfile, 'w', '로그파일이 생성되었습니다.\n')

maxChar = 5000  # 1화당 최대 글자수
data_length = len(data)
startIdx = 0    # 시작 인덱스값
endIdx = data.find('\n', maxChar) # maxChar 인덱스 이후에 나오는 첫번째 줄바꿈 인덱스값
subData = data[startIdx:endIdx]

# 텍스트 파일에 데이터 기록하고 저장하기
num = 0
while data_length > 0:

    num += 1
    endLineTxt = endTextLine(logfile, startIdx, endIdx, subData, num)

    if num < 10:
        filePath = dir + f'/0{str(num)}.txt'
    else:
        filePath = dir + f'/{str(num)}.txt'

    # print('저장 파일 경로 : ' + filePath)
    fileMake(filePath, 'w', subData)

    # 파일 생성후 다음 파일 컨텐츠를 위한 인덱스 조정
    data_length -= (endIdx - startIdx)
    startIdx = endIdx
    findIdx = startIdx + maxChar

    if findIdx < len(data):
        endIdx = data.find('\n', findIdx)
    else:
        endIdx = len(data)

    subData = data[startIdx+1:endIdx]