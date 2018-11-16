a,b=input().split()
a,b=[int(a),int(b)]
q=a//2
c=0
for i in range(q):
    for j in range(q):
        if(i+j==q and i*j==b):
            c=c+1
if(c>=1):
    print('yes')
else:
    print('no')

