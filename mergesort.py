# -*- coding: utf-8 -*-
"""
Created on Mon May 17 16:50:55 2021

@author: DELL
"""
def merge(a,b):
    i=0
    j=0
    m=len(a)
    n=len(b)
    c=[-1]*(m+n)
    
    k=0
    while(k<(m+n)):
        if(j>=n):
            c[k]=a[i]
            k+=1
            i+=1
        elif(i>=m):
            c[k]=b[j]
            j+=1
            k+=1
        elif(a[i]<=b[j]):
            c[k]=a[i]
            k+=1
            i+=1
        elif(b[j]<a[i]):
            c[k]=b[j]
            j+=1
            k+=1
    return c

def divide(a):
    if(len(a)==1):
        return a
    else:
        m=int(len(a)/2)
        x=a[:m]
        y=a[m:]
        p=divide(x)
        q=divide(y)
        z=merge(p,q)
        return z
    
    
n=int(input())

ar=list()

for i in range(n):
    ar.append(int(input()))

print(divide(ar))




    