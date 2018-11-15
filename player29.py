import math as m
a,b=input().split()
a,b=[int(a),int(b)]
count=0
for i in range(a,b+1):
    n=(m.sqrt(i))
    q=(n*n)
    if(i==q):
        count+=1
print(count)
