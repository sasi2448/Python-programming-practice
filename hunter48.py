a=input()
b=input()
x=[]
for i in range(len(a)):
    for j in range(len(b)):
        if(b[j] in a[i]):
            x.append(i)
print(x[0])
