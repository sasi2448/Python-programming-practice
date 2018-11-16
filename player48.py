a=int(input())
x=[]
for i in range(1,a):
    if(i%2!=0 or i==2):
        if(a%i==0):
            x.append(i)
if(len(x)==1):
    x.append(a)
    print(*x)
else:
    print(*x)
