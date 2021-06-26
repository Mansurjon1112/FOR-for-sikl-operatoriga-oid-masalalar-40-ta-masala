# -*- coding: utf-8 -*-
"""
For40. A va B butun soni berilgan (A < B). A va B sonlari orasidagi barcha butun sonlarni
chiqaruvchi programma tuzilsin. Bunda A soni 1 marta, (A + 1) soni 2 marta chiqariladi va xakazo.

Created on Sat Jun 26 10:13:53 2021

@author: Mansurjon Kamolov
"""


a = int(input('A='))
b = int(input('B='))
sanoq = 0
if a<b :
    for i in range(a,b+1):
        sanoq +=1
        for j in range(1,sanoq+1):
            print(i)
            
else:
    print('A<B shart qanoatlantiradigan son kiriting!')