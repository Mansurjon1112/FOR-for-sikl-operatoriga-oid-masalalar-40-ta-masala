# -*- coding: utf-8 -*-
"""
For27. n butun soni va x haqiqiy soni berilgan (n > 0, |x| < 1). Quyidagi yig’indini hisoblovchi
programma tuzilsin.
x + 1 * x3 / (2 * 3) + 1*3*x5 / (2*4*5) + … +
+ 1*3* …*(2*n-1)*x2n+1 /(2*4*..*(2*n)*(2*n+1))

Created on Thu Jun 24 21:35:20 2021

@author: Mansurjon Kamolov
"""

n = int(input('n = '))
x = float(input('x = '))
sum=1
ishora = 1
surat = 1
maxraj = 1 
sum = 0
if n>0 and abs(x)<1 : 
    for i in range(1,2*n+1,2):
        surat *= i   
        maxraj *= (i+1)
        sum = surat * x**(i+2) / maxraj * (i + 2)
        
    print('Yig\'indi:',sum)
else:
    print('x yoki n masala shartini qanoatlantirmaydi. ')

