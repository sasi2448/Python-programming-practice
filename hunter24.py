a,b=input().split()
a,b=[int(a),int(b)]
for i in range(a):
    x=input().split()
    break
y=0
q=0
for i in range(0,a):
    for j in range(0,a):
        if(i!=j):
            if(int(x[i])+int(x[j])==b):
                y=y+1
            else:
                q=q+1
            
if(y>=1):
    print('YES')
else:
    print('NO')
