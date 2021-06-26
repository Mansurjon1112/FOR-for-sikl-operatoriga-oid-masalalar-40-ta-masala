# -*- coding: utf-8 -*-
"""
For32. n butun soni berilgan (n > 0). Quyidagi ketma – ketlikning dastlabki n ta hadini chiqaruvchi
programma tuzilsin.
A
0 = 1; AK = (AK-1 + 1) / K; K = 1, 2, …

Created on Fri Jun 25 18:33:00 2021

@author: Mansurjon Kamolov
"""

n = int(input('n='))
a=1
for i in range(1,n+1):
    a=(a+1)/i
    print('a'+str(i),'=',a)
