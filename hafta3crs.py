# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 22:22:34 2020

@author: Administrator
"""

#Histogram fonksiyonu
#Verilerin istatiksel olarak frekansını tutar
def myHistogram(list_1,myDic):
    myDic = dict()
    for i in list_1:
        if i in myDic:
            myDic[i] = myDic[i]+1
        else:
            myDic[i] = 1
    return myDic

#Tekrar etme ve değer eşit mi?
def lookUp(myDic,value):
    for i in myDic:
        if myDic[i]==value:
            return i
    return -1

list_1 = [2,3,4,6,2,5,6,6,6,6,6,6,6,2]
print(myHistogram(list_1,myDic))
print(repetition(myDic,5))

#Fibonacci recursive
def fib(n):
    #if n<2:
        #return n
    #else:
        #return fib(n-1)+fib(n-2)
    known = {0:0,1:1} #İlk iki değeri girdik
    if n in known:
        return known[n]
    else:
        result = fib(n-1)+fib(n-2)
        known[n] = result
        return result
print(fib(6))

#Küme oluşturma
from sympy import FiniteSet
from fractions import Fraction
s = FiniteSet(1,1.5,Fraction(1.5),Fraction(2.5),3.5)
for member in s:
    print(member)

t = FiniteSet(1,Fraction(4.5),4.5,6)
if s==t:
    print("True")
else:
    print("FALSE")
#s.intersect(t) kesişim
#s.union(t)  birleşim
   
list_2 = [1,4,7,84,3,6,2,62]
my_d = dict()
my_d = {1:'Bir',2:2,'3':'Three'}

for key in my_d.keys():
    print(key,my_d[key])
if -10 not in my_d:  
    my_d[-10] = 50    
def my_h(list_2):
    my_d = {}
    if i not in my_d:
        my_d[i] = 1
    else:
        my_d[i] = i+1
    return my_d

print(my_h(list_2))