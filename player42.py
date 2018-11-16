a=int(input())
y=[]
c=0
for i in range(a):
    x=input().split()
    break
y=sorted(x)
for i in range(a):
    if(x[i]==y[i]):
        c=c+1
    else:
        pass
if(c==a):
    print('yes')
else:
    print('no')
