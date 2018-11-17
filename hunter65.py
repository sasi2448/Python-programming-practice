a,b=input().split()
a,b=[int(a),int(b)]
x=[int(i) for i in input().split()]
for j in range(0,a-1):
    if(x[j]==b):
        x.remove(x[j])
for j in range(0,a-2):
    if(x[j]==b):
        x.remove(x[j])
print(*x)

    
        


