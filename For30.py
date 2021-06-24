# -*- coding: utf-8 -*-
"""
For30. n butun soni va sonlar o’qida 2 ta A, B nuqta berilgan. (A, B haqiqiy son). [A, B] kesmani
teng n ta kesmaga bo’ling. [A, B] kesmada ajratilgan barcha nuqtalar uchun F(X) = 1 – sin(X)
funksiya qiymatini hisoblang.

Created on Thu Jun 24 22:24:38 2021

@author: Mansurjon Kamolov
"""
import math

n = int(input('n='))
a = int(input('A='))
b = int(input('B='))
if a<b:
    qadam = (b-a)/n
    for i in range(n-1):
        a+=qadam
        fx=1-math.sin(a)
        print(fx)
else:
    print('A soni B dan kichik bo\'lishi shart')