def fun(a,b):
    t=0
    try:
        for i in list(a):
            if i==b:
                t=t+1

            else:
                continue
        print(t)
    except:
        print('enter valid input')

a=input('Enter string:')
b=input('Enter char:')

fun(a,b)
