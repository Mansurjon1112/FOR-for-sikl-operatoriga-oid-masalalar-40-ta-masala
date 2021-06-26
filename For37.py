# -*- coding: utf-8 -*-
"""
For37. N butun soni berilgan. Quyidagi yig’indini chiqaruvchi programma tuzilsin.
11 + 22 + … + N

Created on Sat Jun 26 06:37:14 2021

@author: Mansurjon Kamolov
"""
n=int(input('n='))
sum=0
for i in range(1,n+1):
    p=1
    for j in range(1,i+1):
        p *=i
    sum += p
print(sum)



