a=int(input('a='))
b=int(input('b='))
sum=0
if a<b:
    for i in range(a,b+1):
        sum += i
    print('Yig\'indisi',sum)
else:
    print('A<B shartni qanoatlantirmaydi')
