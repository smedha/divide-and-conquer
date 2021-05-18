# -*- coding: utf-8 -*-
"""
Created on Tue May 18 14:44:56 2021

@author: DELL
"""

def merge_and_countSplitInv(a,b):
    n=len(a)
    m=len(b)
    c=[-1]*(len(a)+len(b))
    count=0
    i=0
    j=0
    for k in range(n+m):
        if(i>=n):
            c[k]=b[j]
            j+=1
        elif(j>=m):
            c[k]=a[i]
            i+=1
        elif(b[j]<a[i]):
            c[k]=b[j]
            j+=1
            count+=(n-i)
        else:
            c[k]=a[i]
            i+=1
    return count,c

def sort_and_count(a,n):
    if(n==1):
        return 0,a
    else:
        x,b=sort_and_count(a[:(int(n/2))], len(a[:(int(n/2))]))
        y,c=sort_and_count(a[(int(n/2)):], len(a[(int(n/2)):]))
        z,d=merge_and_countSplitInv(b, c)
        return (x+y+z),d
    
n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
value,ar=sort_and_count(l,n)
print("Number of inversions = ",value)
print("Sorted array = ",ar)

        
    
