# -*- coding: utf-8 -*-
"""
For36. N va K butun sonlari berilgan. Quyidagi yig’indini chiqaruvchi programma tuzilsin.
1K + 2K + … + NK

Created on Sat Jun 26 06:30:56 2021

@author: Mansurjon Kamolov
"""

n=int(input('n='))
k=int(input('k='))
sum=0
for i in range(1,n+1):
    p=1
    for j in range(1,k+1):
        p *=i
    sum += p
print(sum)



