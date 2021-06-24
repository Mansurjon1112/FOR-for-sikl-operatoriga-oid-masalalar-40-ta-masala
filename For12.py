# -*- coding: utf-8 -*-
"""
For12. n butun soni berilgan (n > 0). Quyidagi ko’paytmani hisoblovchi programma tuzilsin.
S = 1.1 * 1.2 * 1.3 * … (n ta ko’payuvchi)

Created on Thu Jun 24 18:57:29 2021

@author: Mansurjon Kamolov
"""

n = int(input('N= '))
kup=1
for i in range(10,10*n+1):
    kup*=i/10
    print(i, kup)
print(sum, 10*n+1)