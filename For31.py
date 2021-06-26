# -*- coding: utf-8 -*-
"""
For31. n butun soni berilgan (n > 0). Quyidagi ketma – ketlikning dastlabki n ta hadini chiqaruvchi
programma tuzilsin.
A
0 = 2; AK = 2 + 1 / AK-1; K = 1, 2, …

Created on Fri Jun 25 18:32:21 2021

@author: Mansurjon Kamolov
"""
n = int(input('n='))
a=2
for i in range(1,n+1):
    a=2+1/a
    print('a'+str(i),'=',a)
