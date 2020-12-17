def factor_func(num):
    total=0
    try:
        n=int(num)
        if n>0:
            for i in range(1,n+1):
                if n%i==0 and i%2!=0:
                    total=int(total)+int(i)
                else:
                    continue
            print(total)
        else:
            print(-10)
    except:
        print(-10)

num=input()
factor_func(num)
