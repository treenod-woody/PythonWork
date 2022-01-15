# 데이터 타입의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)   # List 타입으로 변경
print(menu, type(menu))

menu = tuple(menu)   # Tuple 타입으로 변경
print(menu, type(menu))