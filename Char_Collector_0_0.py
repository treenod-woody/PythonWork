import os
from tkinter import *
from tkinter import filedialog

# 원본 폴더
def open_folder_dialog():
    file_dir = filedialog.askdirectory(title="저장 폴더 선택")
    entry_0.delete(0)
    entry_0.insert(0, file_dir)


# 폴더내 모든 파일 경로를 추출
def extract_file_paths(folder_path):
    file_paths = []
    for root, directories, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    return file_paths


# 특정 문자열 개수 추출
def count_character(file_path, character):
    with open(file_path, 'r', encoding='UTF8') as file:
        content = file.read()
        count = content.count(character)
        return count

# 파일명 이름 변경
def rename_file_with_character_count(file_path, save_folder_path, characters):
    
    file_name = os.path.basename(file_path)
    signed = ""
    i = 0
    for character in characters:
        # '@' 문자 개수 추출
        count = count_character(file_path, character)
        if not count == 0:
            signed += fr"{character}{count}__"
            i += 1
    if not i == 0:
        new_file_name = fr"{save_folder_path}/0__{signed}{file_name}"
    elif i == 0:
        new_file_name = fr"{save_folder_path}/{file_name}"

    return new_file_name

# 신규 폴더 생성
def create_folder(folder_path):
    try:
        os.makedirs(folder_path)
        print("폴더가 성공적으로 생성되었습니다.")
    except FileExistsError:
        print("이미 동일한 이름의 폴더가 존재합니다.")
    except Exception as e:
        print("폴더 생성 중 오류가 발생했습니다:", str(e))

# 원본 파일의 내용 가져오기
def extract_txt_content(file_path):
    with open(file_path, 'r', encoding='UTF8') as file:
        content = file.read()
    return content

# 파일 저장하기
def save_text_to_file(file_path, content):
    with open(file_path, 'w', encoding='UTF8') as file:
        file.write(content)

def signed_char_save():
    input_path = entry_0.get()
    folder_path = fr"{input_path}"
    create_folder(fr"{folder_path}/Complete")
    save_folder_path = fr"{folder_path}/Complete"
    print(save_folder_path)
    file_paths = extract_file_paths(folder_path)

    # 확인할 문자 리스트
    characters = ['@', '#', '(']

    for file_path in file_paths:
        if not os.path.basename(file_path) == '.DS_Store':
            content = extract_txt_content(file_path)
            save_file_path = rename_file_with_character_count(file_path, save_folder_path, characters)
            save_text_to_file(save_file_path, content)
            # print(save_file_path)


tk = Tk()
tk.title('Character Collector')

# row 0
entry_0 = Entry(tk)
entry_0.grid(row=0, column=0)
button_0 = Button(tk, text='원본 폴더 선택', command=open_folder_dialog)
button_0.grid(row=0, column=1)

# row 1
label_empty = Label(tk, text="")
label_empty.grid(row=1, column=0)

# row 2
button_confirm = Button(tk, text="실행하기", command=signed_char_save, width=10, height=2, padx=1, pady=1)
button_confirm.grid(row=2, column=1)


tk.mainloop()