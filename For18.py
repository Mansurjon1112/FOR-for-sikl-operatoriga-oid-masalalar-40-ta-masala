# -*- coding: utf-8 -*-
"""
For18. n butun soni va a haqiqiy soni berilgan (n > 0). Bir sikldan foydalanib quyidagi a ning 1 dan n
gacha bo’lgan barcha darajalarini  yig’indini hisochiqaruvchi vablovchi programma tuzilsin.
1 - a + a2 - a3 + … (-1)n an
Shart operatoridan foydalanilmasin.

Created on Thu Jun 24 19:48:17 2021

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
        sum+=kup*(-1)**(i+1)
    print('Yig\'indisi:',sum)
else:
    print('n>0 bo\'lishi kerak')
