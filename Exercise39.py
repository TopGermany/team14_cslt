i = int(input('Độ ồn (DB):'))
if i == 130:
    print(i,'Là độ ồn của tiếng Jackhammer')     
elif i == 106:
    print(i,'Là độ ồn của tiếng Gas lawnmower')
elif i == 70:
    print(i,'Là độ ồn của tiếng Alarm clock')
elif i == 40:
    print(i,'Là độ ồn của tiếng Quiet room')
elif 106 < i < 130:
    print(i,'Là tiếng ồn nằm ở giữa Jackhammer và Gas lawnmower')
elif 70 < i < 106:
    print(i,'Là tiếng ồn nằm ở giữa Gas lawnmower và Alarm clock')
elif 40 < i < 70:
    print(i,'Là tiếng ồn nằm ở giữa Alarm clock và Quiet room')
elif i > 130:
    print(i,'là tiếng ồn to hơn tiếng Jackhammer')
elif i<40:
    print(i,'Là tiếng ồn nhỏ hơn Quiet room')
