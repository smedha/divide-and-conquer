# -*- coding: utf-8 -*-
"""
Created on Wed May 19 15:19:36 2021

@author: DELL
"""
#works for 2*2 matrices only
def strassen(x,y):
    a=x[0][0]
    b=x[0][1]
    c=x[1][0]
    d=x[1][1]
    e=y[0][0]
    f=y[0][1]
    g=y[1][0]
    h=y[1][1]
    
    p1=a*(f-h)
    p2=(a+b)*h
    p3=(c+d)*e
    p4=d*(g-e)
    p5=(a+d)*(e+h)
    p6=(b-d)*(g+h)
    p7=(a-c)*(e+f)
    
    l=[[-1]*len(x)]*len(y[0])
    l[0][0]=p5+p4-p2+p6
    l[0][1]=p1+p2
    l[1][0]=p3+p4
    l[1][1]=p1+p5-p3-p7
    
    return l

    
    
a=int(input())
b=int(input())

c=int(input())
d=int(input())


if(b==c):
    x=[]
    y=[]
    
    for i in range(a):
        l=[]
        for j in range(b):
            l.append(int(input()))
        x.append(l)
        
    for i in range(c):
        l=[]
        for j in range(d):
            l.append(int(input()))
        y.append(l)
    
    print(strassen(x, y))
    
        
else:
    print("Multiplication of matrices is not possible")