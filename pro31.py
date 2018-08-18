q=[]
w=[]
height=0
breath=0
u1,v1=input().split()
u1=int(u1)
v1=int(v1)
q.append(u1)
w.append(v1)
while(u1!=0):
    if(u1<=4 and v1<=4):
        x=4
        break
    if(u1<=8 and v1<=8):
        x=8
        break
    if(u1<=12 and v1<=12):
        x=12
        break
else:
    x=16
for i in range(x-1):
    u,v=input().split()
    u=int(u)
    v=int(v)
    q.append(u)
    w.append(v)
for k in range(0,x):
    for l in range(0,x):
        if(q[k]==q[l] and k!=l):
            y=l
            m=k
            break
for k in range(0,x):
    if(q[y]==q[m]):
        height=abs(int(w[m])-int(w[y]))

for k in range(0,x):
    for l in range(0,x):
        if(w[k]==w[l] and k!=l):
            t=l
            r=k
            break
if(x>1):
    breath=max(q)-min(q)
print(2*(height+breath))
