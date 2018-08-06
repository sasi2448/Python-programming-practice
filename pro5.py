a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
sum=0
p=0
for i in range(0,a):
    if(a%2==0):
        sum=sum+b+c
        if(a==sum):
            p=sum
            break
if(p==a):
    print("YES")
else:
    print("NO")
