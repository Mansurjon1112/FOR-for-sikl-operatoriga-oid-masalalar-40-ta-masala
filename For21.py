# -*- coding: utf-8 -*-
"""
For21. n butun soni berilgan (n > 0). Bir sikldan foydalangan holda quyidagi yig’indini hisoblovchi
programma tuzilsin. (Olingan natija taxminan e = exp(1) ga yaqinlashadi)
1 + 1/(1!) + 1/(2!) + 1/(3!) + … +1/(n!)

Created on Thu Jun 24 21:07:11 2021

@author: Mansurjon Kamolov
"""

n = int(input('n = '))
fac=1
sum=1
if n>0 : 
    for i in range(1,n+1):
        fac*=i      
        sum+=1/fac
    print('Yig\'indi:',sum)
else:
    print('n>0 bo\'lishi kerak')
