import win32com.client
import os

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

root = "C:/hwpTest/"    # 루트 디렉토리
result_hwp = root + "/Result.hwp"

# result 파일이 있다면 제거
if os.path.isfile(result_hwp):
    os.remove(result_hwp)

filelist = fileListSort(root)

# 한글 파일들에 대한 처리 ==============================================
# =====================================================================

hwp = win32com.client.gencache.EnsureDispatch('HWPFrame.HwpObject')

# result 파일을 하나 생성후 저장
hwp.Run("FileNew")
hwp.SaveAs(result_hwp)

# hwp 파일 열기
hwp.Open("C:/hwpTest/한글파일테스트 1화.hwp")
hwp.MovePos(2)  # 문서의 제일 첫번째에 커서 위치
hwp.Run("Select")
hwp.Run("MoveDocEnd")
hwp.Run("Copy")
hwp.Run("FileClose")

# result 파일에 붙여넣기
hwp.Open(result_hwp)
hwp.Run("MoveDocEnd")
hwp.Run("Paste")
hwp.Run("FileSave")
hwp.Run("FileClose")

hwp.Quit()