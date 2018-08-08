a=int(input())
w=[]
r=[]
for i in range(a):
    x=input().split()
    break
for j in range(a):
    q=bin(int(x[j]))
    w.append(q)
    w.sort(reverse=True)
for o in range(a):
    d=int(w[o],2)
    r.append(d)
    r[o]=int(r[o])
    print(r[o])
