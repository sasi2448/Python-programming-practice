a,b=input().split()
b=int(b)
x=[]
y=[]
for i in range(0,len(a)):
    for j in range(1,len(a)-i+1):
        x.append(a[i:i+j])
for i in range(len(x)):
    if(len(x[i])==b):
        y.append(x[i])
print(*y)
