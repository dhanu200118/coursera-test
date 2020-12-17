def func(n):
    q=[]
    a=[]
    for i in range(0,int(n)):
        b=input('enter element:')
        q.append(b)
        if i==0 or i==int(n)-1:
            a.append(b)
    print('input list is :',q)
    print('New list is:',a)
n=input('enter range of list :')
func(n)
