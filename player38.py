a=int(input())
x=[]
for i in range(1,a+1):
    if(a%i==0):
        if(i%2==0):
            x.append(i)
print(*x)
