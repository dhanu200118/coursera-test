
def bool_func(num1,num2,num3,num4):
    exp1=False
    exp2=False
    exp3=False
    exp4=False
    if num1>num2 :
        exp1=True
    if num1=num3:
        exp2=True
    if num2<=num3:
        exp3=True
    if num4!=num1:
        exp4=True
    a=exp1+exp2+exp3+exp4
    return a
num1=input("enter num1:")
num2=input("enter num2:")
num3=input("enter num3:")
num4=input("enter num4:")
bool_func(num1,num2,num3,num4)
