# -*- coding: utf-8 -*-
"""
For25. n butun soni va x haqiqiy soni berilgan (n > 0, |x| < 1). Quyidagi yig’indini hisoblovchi
programma tuzilsin.
x – x2 / 2 + x3 / 3 - … +(-1)n – 1 xn / n

Created on Thu Jun 24 21:27:23 2021

@author: Mansurjon Kamolov
"""

n = int(input('n = '))
x = float(input('x = '))
sum=1
ishora = 1
if n>0 and abs(x)<1 : 
    for i in range(1,n+1):
        surat = ishora * x**i
        sum+=surat/i
        ishora*=-1
    print('Yig\'indi:',sum)
else:
    print('x yoki n masala shartini qanoatlantirmaydi. ')
