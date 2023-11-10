nốt_nhạc = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
tần_số = [440.0, 466.16, 493.88, 261.63, 277.18, 293.66, 311.13, 329.63, 349.23, 369.99, 392.00, 415.30, 440.00]

tần_số_nhập = float(input("Nhập tần số: "))

if any(abs(tần_số_nhập - tần_số_có) <= 1.0 for tần_số_có in tần_số):
    nốt = nốt_nhạc[tần_số.index(min(filter(lambda x: abs(tần_số_nhập - x) <= 1.0, tần_số)))]
    print(f"Tần số {tần_số_nhập} Hz tương ứng với một nốt nhạc {nốt}")
else:
    print(f"Tần số {tần_số_nhập} Hz không tương ứng với bất kỳ nốt nhạc nào cả")