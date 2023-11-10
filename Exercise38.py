n = input('Tháng trong năm:')
if n == 'Tháng 1' or n == 'Tháng 3' or n == 'Tháng 5' or n == 'Tháng 7' or n == 'Tháng 8' or n == 'Tháng 10' or n == 'Tháng 12':
    print(n,'Có 31 ngày')
elif n == 'Tháng 2':
    print(n,'Có 28 hoặc 29 ngày')
elif n == 'Tháng 4' or n == 'Tháng 6' or 'Tháng 9' or 'Tháng 11':
    print(n,'Có 30 ngày')