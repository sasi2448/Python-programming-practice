a=int(input())
q=[]
for i in range(a):
    x=input().split()
    break
for j in range(a):
    y=input().split()
    break
for i in range(a):
    l=x[0:i]
    ls=x[i:]
    q.append(ls+l)
    for w in range(len(q)):
        if(y==q[w]):
            ad=w
            break
print(ad)
