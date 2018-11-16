a,b=input().split()
a,b=[int(a),int(b)]
c=0
for i in range(1,20):
    if(b**i==a):
        c=c+1
        break
    else:
        pass
if(c==1):
    print('yes')
else:
    print('no')
