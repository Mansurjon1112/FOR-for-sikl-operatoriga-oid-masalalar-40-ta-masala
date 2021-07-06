# -*- coding: utf-8 -*-
"""
For24. n butun soni va x haqiqiy soni berilgan (n > 0). Quyidagi yig’indini hisoblovchi programma
tuzilsin. (Olingan natija taxminan cos(x) ga yaqinlashadi)
1 – x2 / (2!) + x4 / (4!) - … +(-1)n x2n /( (2*n)! )

Created on Thu Jun 24 21:25:46 2021

@author: Mansurjon Kamolov
"""

n = int(input('n = '))
x = float(input('x = '))
fac=1
sum=1
ishora = -1
if n>0 : 
    for i in range(1,2*n+1):
        fac*=i      
        if i%2 == 0:
            surat = ishora * x**i
            sum+=surat/fac
            ishora*=-1
    print('Yig\'indi:',sum)
else:
    print('n>0 bo\'lishi kerak')
