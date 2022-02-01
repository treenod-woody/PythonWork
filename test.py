import win32com.client
import re
import os

def fileListSort(dirPath) :
    numbers = []    # 모든 회차 정보
    data = []
    first_name = ""
    last_name = ""

    dirList = os.listdir(dirPath)

    # 파일명에서 회차 정보만 추출하고 앞이름, 뒷이름을 따로 추출
    for f in dirList:
        regex = re.compile(r'\d+\w')
        mo = regex.search(f).group()
        num = re.findall(r'\d+', mo)[-1]    # 마지막 숫자값만 가져옴
        numbers.append(int(num))

        first_name = f.split(str(num))[0]   # 앞이름
        last_name = f.split(str(num))[1]    # 뒷이름

    numbers.sort()

    for n in numbers:   # 파일 이름 재정렬
        full_name = first_name + str(n) + last_name
        data.append(full_name)

    return data

root = "C:/hwpTest/"    # 루트 디렉토리
result_hwp = root + "/Result.hwp"
cnt = 1

# result 파일이 있다면 제거
if os.path.isfile(result_hwp):
    os.remove(result_hwp)

hwplist = fileListSort(root)

# 한글 파일들에 대한 처리 ==============================================
# =====================================================================

hwp = win32com.client.gencache.EnsureDispatch('HWPFrame.HwpObject')

# result 파일 생성후 저장
hwp.Run("FileNew")
hwp.SaveAs(result_hwp)
hwp.Run("FileClose")

for file in hwplist:
    # hwp 파일 열고 붙여넣기 반복
    hwp.Open(root + file)
    hwp.MovePos(2)  # 문서의 제일 첫번째에 커서 위치

    hwp.CreateField(Direction="-", memo="-", name="start")
    hwp.PutFieldText(Field="start", Text="@") # '@' 붙여넣기
    hwp.Run("MoveDocEnd")
    hwp.CreateField(Direction="-", memo="-", name="last")
    hwp.PutFieldText(Field="last", Text="\r\n\r\n") # 줄바꿈

    hwp.Run("MoveDocBegin")
    hwp.Run("Select")
    hwp.Run("MoveDocEnd")
    hwp.Run("Copy")
    hwp.XHwpDocuments.Item(0).Close(isDirty=False)
    # hwp.Run("FileClose")

    # result 파일에 붙여넣기
    hwp.Open(result_hwp)
    hwp.Run("MoveDocEnd")
    hwp.Run("Paste")
    hwp.XHwpDocuments.Item(0).Save(save_if_dirty=False)
    hwp.Run("FileClose")

hwp.Quit()