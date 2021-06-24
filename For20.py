# -*- coding: utf-8 -*-
"""
For20. n butun soni berilgan (n > 0). Bir sikldan foydalangan holda quyidagi yig’indini hisoblovchi
programma tuzilsin.
1! + 2! + 3! + … +n!

Created on Thu Jun 24 20:01:11 2021

@author: Mansurjon Kamolov
"""

n = int(input('n = '))
fac=1
sum=0
if n>0 : 
    for i in range(1,n+1):
        fac*=i      
        sum+=fac
    print('Yig\'indi:',sum)
else:
    print('n>0 bo\'lishi kerak')
