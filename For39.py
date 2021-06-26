# -*- coding: utf-8 -*-
"""
For39. A va B butun soni berilgan (A < B). A va B sonlari orasidagi barcha butun sonlarni
chiqaruvchi programma tuzilsin. Bunda har bir son o’zining qiymaticha chiqarilsin. Ya’ni 3 soni 3
marta chiqariladi

Created on Sat Jun 26 09:36:30 2021

@author: Mansurjon Kamolov
"""

a = int(input('A='))
b = int(input('B='))
if a<b :
    for i in range(a,b+1):
        for j in range(1,i+1):
            print(i)
            
else:
    print('A<B shart qanoatlantiradigan son kiriting!')