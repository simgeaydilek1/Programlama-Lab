# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 17:45:13 2020

@author: Administrator
"""

from sympy import Symbol
x=Symbol('x')
y=Symbol('y')
p=x*(x+x)
print(p)
p=(x+2)*(x+3)
print(p)

from sympy import factor,expand
expr= x**2-y**2
print(factor(expr))#çarpanlarına ayırıyor

factors=factor(expr)
print(expand(factors))#çarpanlara ayrılmış denklemi tekrar tamlıyor

expr=x**3 + 3*x**2*y+3*x*y**2+y**3
factors = factor(expr)
print(factors)

from sympy import pprint
pprint(factors)#üstel bir şekilde çıktı veriyor

series = x
n=5
for i in range(2,n+1):
    series = series + (x**i)/i
pprint(series)

expr=x*x+x*y+x*y+y*y
res=expr.subs({x:1,y:2})#.subs() değerlere sayı vermeyi sağlıyor
print(res)
r=expr.subs({x:y-1})#x i yok ediyor x yerine y-1 yazıyor

series = x
n=5
x_value=10
for i in range(2,n+1):
    series = series + (x*i)/i
pprint(series)
series_value=series.subs({x:x_value})
print(series_value)



#%%
import sympy as sym
from sympy import Symbol
from sympy import pprint

%matplotlib notebook
import sympy.plotting as syp
sigma = Symbol('sigma')
x= Symbol('x')
mu= Symbol('mu')
pprint(2*sym.pi*sigma)

part1=1/(sym.sqrt(2*sym.pi*sigma**2))
part2=sym.exp(-1*((x-mu)**2)/(2*sigma**2))

my_gaus_f=part1*part2
pprint(my_gaus_f)

print(syp.plot(my_gaus_f.subs({mu:1,sigma:3}),(x,-10,10),title='gauss distribution'))#grafik çizdi
x_values=[]
y_values=[]
for value in range(-100,100):
    #y=my_gaus_f.subs({mu:10,sigma:30,x:value})
    y=my_gaus_f.subs({mu:10,sigma:30,x:value}).evalf()
    #y=my_gaus_f.subs({mu:10,sigma:30,x:value}).doit()
    y_values.append(y)
    x_values.append(value)
    print(x,y)
%matplotlib inline
import matplotlib.pyplot as plt
plt.plot(x_values,y_values)
plt.show()





















