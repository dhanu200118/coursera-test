
while True:

    try:
        p=float(input('enter principal:'))
        r=float(input('enter rate:'))
        t=int(input('enter time in terms of numbernof days:'))
        if type(p)==float and type(r)==float and type(t)==float :break
        si=p*r*t/100
        print(si)
        break
    except:
        print('invalid enter... please enter again: ')
        continue
