# -*- coding: utf-8 -*-
"""
For15. n butun soni va a haqiqiy soni berilgan (n > 0). a ning n – darajasini aniqlovchi programma
tuzilsin. an=a*a*a…a;

Created on Thu Jun 24 19:32:24 2021

@author: Mansurjon Kamolov
"""

a=float(input('a = '))
n = int(input('n = '))
kup = 1
if n>0 :
    for i in range(1,n+1):
        kup*=a
    print(a,'ning',n,'- darajasi',kup)
else:
    print('Musbat daraja kirishingiz kerak edi! n>0')