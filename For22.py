# -*- coding: utf-8 -*-
"""
For22. n butun soni va x haqiqiy soni berilgan (n > 0). Quyidagi yig’indini hisoblovchi programma
tuzilsin. (Olingan natija taxminan ex ga yaqinlashadi)
1 + x + x2 / (2!) + x3 / (3!) + … +xn /(n!)Created on Thu Jun 24 21:09:30 2021

@author: Mansurjon Kamolov
"""

n = int(input('n = '))
x = float(input('X = '))
fac=1
sum=1
surat = 1
if n>0 : 
    for i in range(1,n+1):
        fac*=i      
        surat*=x
        sum+=surat/fac
    print('Yig\'indi:',sum)
else:
    print('n>0 bo\'lishi kerak')
