a=input()
b=list(a)
d=[]
q=[]
count=0
for i in range(len(b)):
    c=ord(b[i])
    d.append(c)

m=min(d)
for j in range(len(b)):
        q.append(m)
        m=m+1

d=list(d)
q=list(q)


for i in range(0,len(q)):
        if(q[i]==d[i]):
            count+=1
        else:
            break
print(count)
