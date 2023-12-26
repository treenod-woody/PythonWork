import os
from tkinter import *
from tkinter import filedialog

# end_index 얻어오기
def find_end_index(content, sep_num):
    start_index = min(sep_num, len(content) - 1)
    substring = content[start_index:] # 4000번째부터 나머지까지
    newline_index = substring.find('\n')
    if newline_index != -1:
        return start_index + newline_index
    return -1

# 원본 파일의 내용 가져오기
def extract_txt_content(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

# 파일 저장하기
def save_text_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

# 원본 파일 경로 얻기
def open_file_dialog():
    file_path = filedialog.askopenfilename(title="원본 txt 파일 선택")
    entry_0.delete(0)    # 엔트리 내용을 모두 제거
    entry_0.insert(0, file_path) # 엔트리에 파일 패스를 표시

def save_folder_dialog():
    file_dir = filedialog.askdirectory(title="저장 폴더 선택")
    entry_1.delete(0)
    entry_1.insert(0, file_dir)

# 신규 폴더 생성
def create_folder(folder_path):
    try:
        os.makedirs(folder_path)
        print("폴더가 성공적으로 생성되었습니다.")
    except FileExistsError:
        print("이미 동일한 이름의 폴더가 존재합니다.")
    except Exception as e:
        print("폴더 생성 중 오류가 발생했습니다:", str(e))


def save_txt():
    file_path = entry_0.get()       # 원본 파일 경로
    folder_path = os.path.dirname(file_path)
    create_folder(f"{folder_path}/Complete")
    save_dir = f"{folder_path}/Complete"        # 저장 폴더 경로
    input_num = int(entry_1.get())         # 분리할 숫자 크기

    content = extract_txt_content(file_path) # 컨텐츠 내용
    start_index = 0
    end_index = 0
    sep_num = input_num
    page_num = 0
    sep_contents = []


    while end_index != -1:
        page_num += 1
        end_index = find_end_index(content, sep_num)

        # 파일 export : start_index ~ end_index
        sep_contents.append(content[start_index:end_index])

        # idx 0 ~ end_idx 까지 1차 분리후 값 재조정
        start_index = end_index
        sep_num = input_num + start_index

        # print(f"end index : {str(end_index)}")
        # print(f"start index : {start_index}")
    
    for i in range(page_num):
        save_file_path = f"{save_dir}/{str(i)}.txt"
        save_text_to_file(save_file_path, sep_contents[i])



tk = Tk()
tk.title('Text Splitter')

# row 0
label_0 = Label(tk, text="원본 TXT 파일 : ")
entry_0 = Entry(tk)
button_0 = Button(tk, text='원본 파일 선택', command=open_file_dialog)

label_0.grid(row=0, column=0)
entry_0.grid(row=0, column=1)
button_0.grid(row=0, column=2)

# row 1
label_1 = Label(tk, text="최대 텍스트 값 : ")
entry_1 = Entry(tk)

label_1.grid(row=1, column=0)
entry_1.grid(row=1, column=1)

# row 2
button_confirm = Button(tk, text="실행하기", command=save_txt, width=10, height=2, padx=1, pady=1)
button_confirm.grid(row=2, column=2)

tk.mainloop()