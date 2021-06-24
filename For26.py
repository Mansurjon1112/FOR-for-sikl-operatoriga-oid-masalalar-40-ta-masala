# -*- coding: utf-8 -*-
"""
For26. n butun soni va x haqiqiy soni berilgan (n > 0, |x| < 1). Quyidagi yig’indini hisoblovchi
programma tuzilsin.
x – x3 / 3 + x5 / 5 - … +(-1)n x2n+1 / (2n + 1)

Created on Thu Jun 24 21:33:00 2021

@author: Mansurjon Kamolov
"""

n = int(input('n = '))
x = float(input('x = '))
sum=1
ishora = 1
if n>0 and abs(x)<1 : 
    for i in range(1,2*n+2,2):
        surat = ishora * x**i
        sum+=surat/i
        ishora*=-1
    print('Yig\'indi:',sum)
else:
    print('x yoki n masala shartini qanoatlantirmaydi. ')
