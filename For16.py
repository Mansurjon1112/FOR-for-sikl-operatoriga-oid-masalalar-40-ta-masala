# -*- coding: utf-8 -*-
"""
For16. n butun soni va a haqiqiy soni berilgan (n > 0). Bir sikldan foydalanib a ning 1 dan n gacha
bo’lgan barcha darajalarini chiqaruvchi programma tuzilsin.

Created on Thu Jun 24 19:37:20 2021

@author: Mansurjon Kamolov
"""

a = float(input('a = '))
n = int(input('n = '))
kup = 1
if n>0 :       
    for i in range(1,n+1):
        kup*=a
        print(a,'ning',i,'- darajasi',kup)
else:
    print('n>0 bo\'lishi kerak')