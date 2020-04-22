# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 17:50:59 2020

@author: Simge Aydilek
"""
#üstel dağılım fonsiyonunun gragiğinin sympy ile çizilmesi.
#lamdaya 0.3 değerini verdim.

import sympy as sym
from sympy import Symbol
from sympy import pprint
%matplotlib notebook
import sympy.plotting as syp
 
#sembol atamaları yaptım.
t=Symbol ('t') #zamanın değerini temsil ettiği için 0'dan büyük olmalı.
lamb=Symbol ('lambda') #lambda değeri mutlaka bilinmeli.
f=Symbol('f')

f= 1 - sym.exp(-lamb*t)
pprint(f)  #formülü yazdırıyoruz.

print(syp.plot(f.subs({lamb:0.3}),(t,1,10),tittle='exponential distribution'))

#üstel dağılım fonsiyonunun gragiğinin sympy ile çizilmesi.
#lamdaya 0.3 değerini verdim.

#%%
#üstel dağılım fonksiyonunun grafaiğinin matplotlib ile çizimi.
#lambdaya 0.3 değerini verdim.

#gerekli kütüphaneleri çağırdım.
import sympy as sym
from sympy import Symbol
from sympy import pprint
%matplotlib notebook
import sympy.plotting as syp 
import matplotlib.pyplot as plt
import sympy as sp


t=Symbol ('t')
lamb=Symbol ('lambda')
f=Symbol('f')

f= 1 - sym.exp(-lamb*t)
pprint(f)

t_value = []#zamanı ifade ediyor 0'dan büyük olmalı
z_value = []
for value in range (1,15):
    z = f.subs({lamb:0.3, t:value}).evalf()
    t_value.append(value)
    z_value.append(z) #z'ye karşılık gelen değerlerle dizi oluşturdum.
    
plt.plot(t_value,z_value)
plt.show()


#Simge Aydilek- 180401071
#https://github.com/simgeaydilek1


















