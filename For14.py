# -*- coding: utf-8 -*-
"""
For14. n butun soni berilgan (n > 0). Shu sonning kvadratini quyidagi formula asosida hisoblovchi
programma tuzilsin.
n2= 1 + 3 + 5 + … + (2*n - 1)
har bir qo’shiluvchidan keyin natijani ekranga chiqarib boring. Natijda ekranda 1 dan n gacha
bo’lgan sonlar kvadrati chiqariladi.

Created on Thu Jun 24 19:23:32 2021

@author: Mansurjon Kamolov
"""

n = int(input('N= '))
sum = 0
p = 0
for i in range (1,2*n,2):
    sum+=i
    p+=1
    print(p,'sonining kvadrati = ',sum)