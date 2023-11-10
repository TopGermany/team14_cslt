letter = input("Nhập một chữ cái trong bảng chữ cái: ")
if letter in ('a', 'e', 'i', 'o', 'u'):
    print("Chữ cái", letter, "là một nguyên âm")
elif letter == 'y':
    print("Đôi khi y là một nguyên âm, và đôi khi là một phụ âm")
else:
    print("Chữ cái", letter, "là một phụ âm")
