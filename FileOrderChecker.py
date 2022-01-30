from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as msgbox
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
e_openDir.insert(END, "폴더를 선택해주세요.")

def open_dir():
    dir = filedialog.askdirectory(title="파일을 검사할 폴더를 선택하세요.")
    e_openDir.delete(0, "end")
    e_openDir.insert(END, dir)

btn_openDir = Button(frame_dir, padx=4, pady=4, text="폴더선택", command=open_dir)
btn_openDir.pack(side="right")

# 검사 회차 선택 프레임 ----------------------------
frame_num = Frame(win, relief="solid", bd=1)
frame_num.pack(fill="x", padx=10, pady=10)

labelRef_num = Label(frame_num, text="시작회차(숫자만 입력) : ")
labelRef_num.pack(side="left")

e_startNum = Entry(frame_num, width=10)
e_startNum.pack(side="left", padx=4, pady=4)
e_startNum.insert(END, "1")

# 버튼 실행 --------------------------------------
def btncmd():

    dir = e_openDir.get()   # 검사할 폴더 경로
    sep_txt = e_startNum.get()
    cnt = int(sep_txt)
    logfile = dir + "/00_log.txt"   # 로그 파일
    fileNames = []

    try:
        if os.path.isfile(logfile): # 로그 파일이 있다면 제거한후 검사 시작
            os.remove(logfile)

        fileList = os.listdir(dir)

        for f in fileList:
            if f==".DS_Store":
                continue
            else:
                fileNames.append(f)

        fileNames.sort()
        fname = str(fileNames[0])    # 1화 파일명

        try:
            values = fname.split(sep=sep_txt)   # 1을 기준으로 앞이름과 뒷이름으로 분리

            # log 파일 생성
            logfile = dir + "/00_log.txt"
            fileMake(logfile, 'w', '검사를 시작합니다.\n\n')

            # 검증 : fileNames <-> values[0] + str(cnt) + values[1]
            for v in fileNames:
                check_fname = values[0] + str(cnt) + values[1]
                if(v == check_fname):
                    cnt += 1
                else:
                    content = v + " : 파일명 이상 발견\n================================\n" 
                    fileMake(logfile, 'a', content)
                    cnt += 1

            win.quit()

        except:
            msgbox.showinfo("알림", "시작 회차 정보가\n잘못 입력되었습니다.")
    except:
        msgbox.showinfo("알림", "폴더 경로를 찾을 수 없습니다.\n검사할 폴더를 다시 선택해주세요.")

# 파일 생성 또는 수정 --------------------------------------
def fileMake(path, state, content):
    with open(path, state, encoding="utf8") as file:
        file.write(content)

btn_confirm = Button(win, padx=4, pady=4, text="검사하기", command=btncmd)
btn_confirm.pack(padx=5, pady=5)

win.mainloop()