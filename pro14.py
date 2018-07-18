a,b=input().split()
a=int(a)
b=int(b)
q=[]
w=[]
for i in range(a):
    x=input().split()
    break
for j in range(0,b):
    u,v=input().split()
    u=int(u)
    v=int(v)
    q.append(u)
    w.append(v)
for k in range(0,b):
    t=q[k]
    g=w[k]
    f=0
    for l in range(t,g+1):
        f=f^int(x[l-1])
    print(f)
