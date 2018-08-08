a=int(input())
count=0
count1=0
w=0
e=0
for i in range(a):
    x=input().split()
    break
if(a>=2 and a<100000):
    if(a%2==0):
        q=a//2
        for j in range(q):
            w=w+int(x[j])
            count+=1
        for k in range(q,a):
            e=e+int(x[k])
            count1+=1
    else:
        t=a//2+1
        for j in range(t):
            w=w+int(x[j])
            count+=1
        for k in range(t,a):
            e=e+int(x[k])
            count1+=1
    if(w//count==e//count1):
        print('yes')
    else:
        print('no')
else:
    print('no')
        

        
