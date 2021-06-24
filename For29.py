# -*- coding: utf-8 -*-
"""
For29. n butun soni va sonlar o’qida 2 ta A, B nuqta berilgan. (A, B haqiqiy son). [A, B] kesmani
teng n ta kesmaga bo’ling. [A, B] kesmada ajratilgan barcha nuqtalarni chiqaring.

Created on Thu Jun 24 21:59:34 2021

@author: Mansurjon Kamolov
"""

n = int(input('n='))
a = int(input('A='))
b = int(input('B='))
if a<b:
    qadam = (b-a)/n
    for i in range(n-1):
        a+=qadam
        print(a)
else:
    print('A soni B dan kichik bo\'lishi shart')