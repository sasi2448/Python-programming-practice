n=int(input())
a=[]
p=[]
for i in range(1,1000):
        x=2**i
        if(n==x):
                t=n-x
                break
        if(n>x):
                a.append(x)
                a.sort(reverse=True)
                p.append(n-a[0])
                p.sort()
                continue
                
q=int(p[0])
if(n==x):
        print(t)
else:
        print(q)
                
                
        
