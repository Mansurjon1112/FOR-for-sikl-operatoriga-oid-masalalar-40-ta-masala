# -*- coding: utf-8 -*-
"""
For13. n butun soni berilgan (n > 0). Quyidagi yig’indini hisoblovchi programma tuzilsin.
S = 1.1 - 1.2 + 1.3 - …
(n ta qo’shiluvchi, ishoralar almashib keladi. Shart operatoridan foydalanmang)

Created on Thu Jun 24 19:03:27 2021

@author: Mansurjon Kamolov
"""

n = int(input('N= '))
sum= 0
for i in range(11,11+n):
    sum+=i/10*(-1)**(i-1)
print(sum)
