# -*- coding: utf-8 -*-
"""
Created on Mon May 17 12:53:23 2021

@author: DELL
"""



x=input()
y=input()

l1=int(len(x)/2)
l2=int(len(y)/2)

a=x[:l1]
b=x[l1:]

c=y[:l2]
d=y[l2:]

a=int(a)
b=int(b)

c=int(c)
d=int(d)

s1=a*c
s2=b*d
s3=(a+b)*(c+d)
s4=s3-s2-s1
s5=(s1*(10**len(x)))+s2+(s4*(10**l1))

print(s5)