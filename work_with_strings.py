#!/usr/bin/env python
# coding: utf-8

# In[2]:


def str_func(word):
    a=list(word)
    d=len(a)
    print(a[d-1])
q=input('enter:')
str_func(q)


# In[3]:



def sum_str_func(n):
    sum = 0
    while (n != 0):

        sum = sum + int(n % 10)
        n = int(n/10)

    print(sum)
n=input('Enter:')
try:
    sum_str_func(int(n))
except:
    print('PLEASE ENTER A NUMBER')


# In[4]:


def slicing_func (str):
    d=len(str)
    print(str[0:2],str[(d-2):d],str[1],str[-2])
string=input('enter string:')
slicing_func (string)


# In[ ]:




