# -*- coding: utf-8 -*-
"""
For19. n butun soni berilgan (n > 0). Birdan n gacha bo’lgan sonlar ko’paytmasini chiqaruvchi
programma tuzilsin. n! = 1 * 2 * … n
Birdan n gacha bo’lgan sonlar ko’paytmasi n faktorial deyiladi.

Created on Thu Jun 24 19:58:10 2021

@author: Mansurjon Kamolov
"""

n = int(input('n = '))
fac=1
if n>0 : 
    for i in range(2,n+1):
        fac*=i      
    print(str(n)+'! =',fac)
else:
    print('n>0 bo\'lishi kerak')
