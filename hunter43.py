a=input()
y=[]
z=[]
x=([a[i:i+1] for i in range(0, len(a), 1)]) 
for i in range(len(x)):
    if(x[i].isalpha()==True):
        y.append(x[i])
    else:
        z.append(x[i])
q=len(y)-1
if(len(y)==len(z)):
    z=[int(i) for i in z]
    for i in range(len(y)):
        print(y[i]*z[i],end='')
else:
    for i in range(len(y)):
        if(len(y)<len(z)):
            z[i+1]=(z[q]+z[q+1])
            z=[int(i) for i in z]
            print(y[i]*z[i],end='')
