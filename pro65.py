a,b=input().split()
a=int(a)
b=int(b)
sum=0
for i in range(a):
    x=input().split()
    break
s=int(input())
for j in range(a):
    sum=sum+int(x[j])
if(s==sum//2):
    e=int(x[b])
    sum=sum-e
    o=s-(sum//2)
    print(o)
else:
    print('Bon Appetit')
