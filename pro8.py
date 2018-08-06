def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x
a,b=input().split()
a=int(a)
b=int(b)
q=[]
w=[]
for i in range(a):
    n=input().split()
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
    c=int(n[t-1])
    d=int(n[g-1])
    result= gcd(c,d)
    print(result)
