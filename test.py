import win32com.client
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as msgbox
import re
import os

# ==========================================================
# 다이얼로그 사용자 입력 정의
# ==========================================================

win = Tk()
win.title("FileOrderChecker")

# 폴더 선택 프레임 -------------------------------
frame_dir = Frame(win, relief="solid", bd=1)
frame_dir.pack(fill="x", padx=10, pady=10)

labelRef = Label(frame_dir, text="폴더경로 : ")
labelRef.pack(side="left")

e_openDir = Entry(frame_dir, width=30)
e_openDir.pack(side="left", padx=4, pady=4)
e_openDir.insert(END, "검사 폴더를 선택하세요")

def open_dir():
    dir = filedialog.askdirectory(title="파일을 검사할 폴더를 선택하세요.")
    e_openDir.delete(0, "end")
    e_openDir.insert(END, dir)

btn_openDir = Button(frame_dir, padx=4, pady=4, text="폴더선택", command=open_dir)
btn_openDir.pack(side="right")

# 파일 리스트 재정렬
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

# 버튼 실행 --------------------------------------
def btncmd():
    try:
        root = e_openDir.get() + "/"   # 검사할 폴더 경로
        result_hwp = root + "Result.hwp"

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

        # hwp 파일 열고 붙여넣기 반복
        for file in hwplist:
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
        win.quit()

    except:
        msgbox.showinfo("알림", "폴더 경로를 찾을 수 없습니다.\n검사할 폴더를 다시 선택해주세요.")

btn_confirm = Button(win, padx=4, pady=4, text="검사하기", command=btncmd)
btn_confirm.pack(padx=5, pady=5)

win.mainloop()