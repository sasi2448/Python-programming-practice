n,m=input().split()
n=int(n)
m=int(m)
count=0
for i in range(n):
    a=input().split()
    break
for j in range(m):
    b=input().split()
    break
for k in range(len(a)):
    for l in range(len(b)):
        if(b[l] in a[k]):
            count=count+1
if(count==len(b)):
    print("YES")
else:
    print("NO")

