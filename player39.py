a=int(input())
c=0
for i in range(1,20):
    if(2**i==a):
        c=c+1
        break
    else:
        pass
if(c==1):
    print('yes')
else:
    print('no')
