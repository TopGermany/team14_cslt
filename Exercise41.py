note = input('Nhập nốt nhạc (A5, B6,...): ')     
notnhac = note[0] 
n = int(note[1:4])
if notnhac == 'C' or notnhac == 'D' or notnhac == 'E' or notnhac == 'F' or notnhac == 'G' or notnhac == 'A' or notnhac == 'B':
    if n < 0 or n > 8:
        print('Nốt không hợp lệ')
    else:
        if notnhac == 'C':
            tanso = 261.63 / 2 ** (4 - n)
            print('Nốt nhạc',note, 'co tan so = ',tanso, 'Hz')
        elif notnhac == 'D':
            tanso = 293.66 / 2 ** (4 - n)
            print('Nốt nhạc',note, 'co tan so = ',tanso,'Hz')
        elif notnhac == 'E':
            tanso = 329.63 / 2 ** (4 - n)
            print('Nốt nhạc',note, 'co tan so = ',tanso,'Hz')
        elif notnhac == 'F':
            tanso = 349.23 / 2 ** (4 - n)
            print('Nốt nhạc',note, 'co tan so = ',tanso,'Hz')
        elif notnhac == 'G':
            tanso = 392.00 / 2 ** (4 - n)
            print('Nốt nhạc',note, 'co tan so= ',tanso,'Hz')
        elif notnhac == 'A':
            tanso = 440.00  /2 ** (4 - n)
            print('Nốt nhạc',note, 'co tan so = ',tanso,'Hz')
        elif notnhac == 'B':
            tanso = 493.88 / 2 ** (4 - n)
            print('Nốt nhạc',note, 'co tan so = ',tanso,'Hz')  
else: 
    print('Nốt không hợp lệ')
