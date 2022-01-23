from tkinter import *
from tkinter import filedialog

win = Tk()
win.title("Text splitter")
# win.geometry("400x300")
# win.resizable(False, False)

# 파일 선택 프레임 -----------------------------------
frame_file = Frame(win, relief="solid", bd=1)
frame_file.pack(fill="x", padx=5, pady=5)

e_filepath = Entry(frame_file, width=30)
e_filepath.pack(side="left")

def get_file():
    file = filedialog.askopenfilename(title="원본 txt파일을 선택하세요.", \
        filetypes=(("TXT 파일", "*.txt"), ("모든 파일", "*.*")), \
            initialdir="TextSplitter")   # 최초 시작 경로는 C:/

    e_filepath.insert(END, file)

btn_getfile = Button(frame_file, padx=2, pady=2, text="파일선택", command=get_file)
btn_getfile.pack(side="right")

# 최대 텍스트값 입력 프레임 ---------------------------
frame_info = Frame(win, relief="solid", bd=1)
frame_info.pack(fill="x", padx=5, pady=5)

label_1 = Label(frame_info, text="최대 텍스트값 : ")
label_1.pack(side="left")

e = Entry(frame_info, width=20)
e.pack(side="left")
e.insert(END, "5000")

# 버튼 실행 -----------------------------------------
def btncmd():
    print(e.get())

btn_confirm = Button(win, padx=10, pady=4, text='실행하기', command=btncmd)
btn_confirm.pack(padx=5, pady=5)

win.mainloop()