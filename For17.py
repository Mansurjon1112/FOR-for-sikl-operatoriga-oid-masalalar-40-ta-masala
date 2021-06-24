# -*- coding: utf-8 -*-
"""
For17. n butun soni va a haqiqiy soni berilgan (n > 0). Bir sikldan foydalanib quyidagi a ning 1 dan n
gacha bo’lgan barcha darajalarini chiqaruvchi va yig'indini hisoblovchi programma tuzilsin.
1 + a + a2 + a3 + … an

Created on Thu Jun 24 19:40:05 2021

@author: Mansurjon Kamolov
"""

a = float(input('a = '))
n = int(input('n = '))
kup = 1
sum = 0
if n>0 :       
    for i in range(1,n+1):
        kup*=a
        print(a,'ning',i,'- darajasi',kup)
        sum+=kup
    print('Yig\'indisi:',sum)
else:
    print('n>0 bo\'lishi kerak')