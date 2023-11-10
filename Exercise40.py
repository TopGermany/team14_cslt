a=float(input(''))
b=float(input(''))
c=float(input(''))
if (a+b>c) and (a+c>b) and (b+c>a) and a>0 and b>0 and c>0:
    if (a == b) and (b == c) and (c == a):
        print('Tam giác đều')
    elif (a==b) and (a!=c) or (a==c) and (a!=b) or (b==c) and (b!=a):
        print('Tam giác cân')
    else:
        print('Tam giác tù')