def bool_func(num1,num2,num3,num4):
    exp1=str(num1>num2 )
    exp2=str( num1==num3)
    exp3=str(num2<=num3)
    exp4=str(num4!=num1)
    a= exp1+exp2+exp3+exp4
    print(a)
num1=input("enter num1:")
num2=input("enter num2:")
num3=input("enter num3:")
num4=input("enter num4:")
bool_func(num1,num2,num3,num4)
