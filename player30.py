a,b,c=input().split()
c=int(c)
co=0
s=0
for i in range(len(a)):
    for j in range(len(b)):
        if(i==j):
            if(a[i]!=b[j]):
                co=co+1
            else:
                s=s+1
if(c==co):
    print('yes')
else:
    print('no')
                
