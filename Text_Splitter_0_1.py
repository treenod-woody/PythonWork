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

def save_txt():
    file_path = entry_0.get()       # 원본 파일 경로
    save_dir = entry_1.get()        # 저장 폴더 경로
    input_num = int(entry_2.get())         # 분리할 숫자 크기

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
        # print(save_file_path)

    # print(page_num)
    # print(sep_contents[page_num - 1])
    # print(f"원본 파일 : {file_path}")
    # print(f"저장 경로 : {save_dir}")
    # print(f"분리할 기준값 : {str(sep_num)}")
    

    
    # export_content = []
    # content = extract_txt_content(file_path, start_index)


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
label_1 = Label(tk, text="원본 TXT 파일 : ")
entry_1 = Entry(tk)
button_1 = Button(tk, text='저장 경로 선택', command=save_folder_dialog)

label_1.grid(row=1, column=0)
entry_1.grid(row=1, column=1)
button_1.grid(row=1, column=2)

# row 2
label_2 = Label(tk, text="최대 텍스트 값 : ")
entry_2 = Entry(tk)

label_2.grid(row=2, column=0)
entry_2.grid(row=2, column=1)

# row 3
button_confirm = Button(tk, text="실행하기", command=save_txt, width=10, height=2, padx=1, pady=1)
button_confirm.grid(row=3, column=2)

tk.mainloop()