# -*- coding: utf-8 -*-
"""
For33. n butun soni berilgan (n > 1). Fibonachchi ketma – ketlikning dastlabki n ta hadini
chiqaruvchi programma tuzilsin.

F1 = 1; F2 = 1; FK = FK-2 + FK-1; K = 3, 4, ...

Created on Fri Jun 25 18:36:34 2021

@author: Mansurjon Kamolov
"""
n = int(input('n='))
f0=f1=1
if n>1 :
    print(f0,end='  ')
    print(f1,end='  ')
    for i  in range(2,n):
        f=f0+f1
        print(f, end='  ')
        f0=f1
        f1=f
else:
    print('n>1 shartni qanoatlantiradigan son kiriting!')