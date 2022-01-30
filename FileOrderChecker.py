from ast import For
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

# 버튼 실행 --------------------------------------
def btncmd():

    dir = e_openDir.get()   # 검사할 폴더 경로
    logfile = dir + "/00_log.txt"   # 로그 파일
    fileList = []   # 폴더내 모든 파일 리스트
    numbers = []    # 모든 회차 정보

    try:
        if os.path.isfile(logfile): # 로그 파일이 있다면 제거한후 검사 시작
            os.remove(logfile)

        fileList = os.listdir(dir)

        # log 파일 생성
        logfile = dir + "/00_log.txt"
        fileMake(logfile, 'w', '검사를 시작합니다.\n\n')

        for f in fileList:
            if f==".DS_Store":
                continue
            else:
                # N화를 모두 추출한 후 숫자만 남김 -----------
                regex = re.compile(r'\d+\w+')
                mo = regex.search(f).group()
                num = re.findall(r'\d+', mo)
                for n in num:
                    numbers.append(int(n))

        numbers.sort()
        
        for i in range(0, len(fileList)-1):
            value = numbers[0] + i
            if numbers[i] == value:
                continue
            else:
                content = str(value) + "화에서 문제가 발견되었습니다.\n-------------------------------\n"
                fileMake(logfile, 'a', content)

        win.quit()

    except:
        msgbox.showinfo("알림", "폴더 경로를 찾을 수 없습니다.\n검사할 폴더를 다시 선택해주세요.")

# 파일 생성 또는 수정 --------------------------------------
def fileMake(path, state, content):
    with open(path, state, encoding="utf8") as file:
        file.write(content)

btn_confirm = Button(win, padx=4, pady=4, text="검사하기", command=btncmd)
btn_confirm.pack(padx=5, pady=5)

win.mainloop()