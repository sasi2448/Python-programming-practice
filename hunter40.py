a=input()
s=0
q=[]
for i in range(len(a)):
    s=s+int(a[i])
q.append(s)
r=0
while(s>0):
    d=s%10
    r=r*10+d
    s=s//10
if(r==q[0]):
    print('YES')
else:
    print('NO')



