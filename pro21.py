a=int(input())
w=[]
e=[]
for i in range(a):
    x=input().split()
    break
if(a>=2 and a<100000):
    if(a%2==0):
        q=a//2
        for j in range(q):
            w.append(x[j])
        for k in range(q,a):
            e.append(x[k])
    else:
        t=a//2+1
        for j in range(t):
            w.append(x[j])
        for k in range(t,a):
            e.append(x[k])
    print('yes')
else:
    print('no')
        
