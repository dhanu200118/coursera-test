def slicing_func (str):
    d=len(str)
    return str[0:2],str[(d-2):d],str[1],str[-2]
string=input('enter string:')
try:
    b=slicing_func (string)
    print(b)
except:
    print('enter valid string')
