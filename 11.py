
def sum_str_func(n):
    sum = 0
    while (n != 0):

        sum = sum + int(n % 10)
        n = int(n/10)
    return sum
n=input()
try:
    b=sum_str_func(int(n))
    print(b)
except:
    print('PLEASE ENTER A NUMBER')
