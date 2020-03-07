# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 23:57:46 2020

@author: Administrator
***
"""

#Olasılık
#İstenilen durum/Tüm durumlar

from sympy import FiniteSet

def probability(space, event):
    return len(event)/len(space)

def check_prime(number):
    if number != 1:
        for factor in range(2, number):
            if number % factor == 0:
                return False
    else:
        return False
    return True


space = FiniteSet(*range(1, 21)) #Virgülle ayrılmış eleman oluşturuluyor.
primes = []
for num in space:
    if check_prime(num):
        primes.append(num)
event = FiniteSet(*primes)
p = probability(space,event)
print(p)
