human_year=int(input("human_year:"))
if 0<human_year<2:
    print("dog_year:",human_year*10.5)
elif human_year>=2:
    print("dog_year:",2*10.5+(human_year-2)*4)
else:
    print("Vui long nhap so duong")