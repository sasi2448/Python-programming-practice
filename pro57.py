a,b=input().split()
count=0
a=set(a)
b=set(b)
for i in a:
    if i in b:
        count=count+1
if(count>=2):
    print('yes')
elif(count<2):
    print('no')
