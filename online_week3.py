# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 20:31:42 2020

@author: Administrator
"""

import sympy as sym
from sympy import Symbol
from sympy import pprint

p = Symbol('p')
x = Symbol('x')
n = Symbol('n')

my_f_3_part_0 = sym.factorial(n)/(sym.factorial(x)*sym.factorial(n-x))
pprint(my_f_3_part_0)

my_f_3_part_1 = p**x
pprint(my_f_3_part_1)

my_f_3_part_2 = (1-p)**(n-x)
pprint(my_f_3_part_2)

my_f_3 = my_f_3_part_0*my_f_3_part_1*my_f_3_part_2
pprint(my_f_3)

sym.plot(my_f_3.subs({p:0.2,n:50}),(x,0,50),title = 'binomial distribution plot for n = 50')

#%%


  
from sympy import Symbol,Limit
from sympy import pprint


t = Symbol('t')
t1 = Symbol('t1')
delta_t = Symbol('delta_t')


St = 5*t**2 + 2*t + 8

St1 = St.subs({t:t1})
St1_delta = St.subs({t: t1 + delta_t})

f_limit = Limit((St1_delta - St1)/delta_t,delta_t,0).doit()
print("{}  fonksiyonun limiti: {}".format(St,f_limit))


#%%


from sympy import exp,sqrt,pi,Integral
from sympy import Symbol

x = Symbol('x')

p = exp(-(x - 10)**2/2)/sqrt(2*pi)
f_integral = Integral(p,(x,11,12)).doit().evalf()
print(f_integral)

















