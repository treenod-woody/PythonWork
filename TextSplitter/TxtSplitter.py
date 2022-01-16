maxChar = 5000  # 1화당 최대 글자수

with open("TextSplitter/00.txt", "r", encoding="utf8") as source_file:
    data = source_file.read()

print(len(data))
