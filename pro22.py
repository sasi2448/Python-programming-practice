a=int(input())
x=[int(i) for i in input().split()]
s=0
s1=0
s2=0
w=[]
r=0
t=0
for i in range(a):
    if(i%2==0):
        s=s+x[i]
    if(i%2!=0):
        s1=s1+x[i]
q=(a//3)+1
for i in range(q):
    for j in range(i,a,3):
        w.append(x[j])
r=r+sum(w[:2])
t=t+sum(w[2:4])
for i in range(a):
    if(x[i]==10):
        print(max(s,s1,r,t))
        break
        
    else:
        print(s)
        break
        
        
    
