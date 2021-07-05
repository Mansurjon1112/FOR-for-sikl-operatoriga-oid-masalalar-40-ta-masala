""" 
For3. a va b butun sonlari berilgan (a < b). a va b sonlari orasidagi barcha butun sonlarni (a va b
dan tashqari) kamayish tartibida chiqaruvchi va chiqarilgan sonlar sonini chiqaruvchi progma
tuzilsin.
"""

a=int(input('a='))
b=int(input('b='))
for i in range (b-1,a,-1):
    print(i)
print('Oradagi sonlar soni: ',b-a-1)
