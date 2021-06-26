# -*- coding: utf-8 -*-
"""
For35. n butun soni berilgan (n > 2). Quyidagi ketma – ketlikning dastlabki n ta hadini chiqaruvchi
programma tuzilsin.
A1 = 1; A2 = 2; A3 = 3; AK = AK-1 + AK-2 - 2*AK-3; K = 4, 5, …

Created on Sat Jun 26 06:22:38 2021

@author: Mansurjon Kamolov
"""

n=int(input('n='))
a=1
b=2
c=3
print(a)
print(b)
if n>2:   
    print(c)
    for i in range(n-3):
        d=c+b-2*a
        a,b,c=b,c,d
        print(d)
else: 
    print('n>2 shartni qanoatlantirmaydi')    