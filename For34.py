# -*- coding: utf-8 -*-
"""
For34. n butun soni berilgan (n > 1). Quyidagi ketma – ketlikning dastlabki n ta hadini chiqaruvchi
programma tuzilsin.
A1 = 1; A2 = 2; AK = (AK-2 + 2*AK-1) / 3; K = 3, 4, …

Created on Sat Jun 26 06:04:07 2021

@author: Mansurjon Kamolov
"""

n=int(input('n='))
a=1
b=2
print(a)
if n>1:   
    print(b)
    for i in range(n-2):
        c=(a+2*b)/3
        a,b=b,c
        print(c)
else: 
    print('n>1 shartni qanoatlantirmaydi')

    