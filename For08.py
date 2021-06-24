a=int(input('a='))
b=int(input('b='))
kup=1
if a<b:
    for i in range(a,b+1):
        kup *= i
    print('Ko\'paytmasi',kup)
else:
    print('A<B shartni qanoatlantirmaydi')
