# -*- coding: utf-8 -*-
"""
For38. N butun soni berilgan. Quyidagi yig’indini chiqaruvchi programma tuzilsin.
1N + 2N-1 + … + N1

Created on Sat Jun 26 06:39:29 2021

@author: Mansurjon Kamolov
"""

n=int(input('n='))
sum=0
for i in range(1,n+1):
    p=1
    for j in range(n,i-1,-1):
        p *=i
    sum += p
print(sum)


