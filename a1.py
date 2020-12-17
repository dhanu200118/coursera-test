import re

fhand = open('regex_sum_42.txt')


count = list()
for line in fhand:
    x=re.findall('[0-9]+',line)
    count+=x
print(count)
sum=0
for c in count:
    sum=sum+int(c)
print(sum)
