# -*- coding: utf-8 -*-
"""
For23. n butun soni va x haqiqiy soni berilgan (n > 0). Quyidagi yig’indini hisoblovchi programma
tuzilsin. (Olingan natija taxminan sin(x) ga yaqinlashadi)
x – x3 / (3!) + x5 / (5!) - … +(-1)n x2n+1 /( (2*n+1)! )

Created on Thu Jun 24 21:17:18 2021

@author: Mansurjon Kamolov
"""

n = int(input('n = '))
x = float(input('X = '))
fac=1
sum=0
ishora = 1
if n>0 : 
    for i in range(1,2*n+2):
        fac*=i      
        if i%2 == 1:
            surat = ishora * x**i
            sum+=surat/fac
            ishora*=-1
    print('Yig\'indi:',sum)
else:
    print('n>0 bo\'lishi kerak')
