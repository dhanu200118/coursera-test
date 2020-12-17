import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    s=""
    s=s+str(n%2)
    w=s.split()

    a=0
    for i in w:
        if i==1:
            a+=1
        else:continue
    print(a)
