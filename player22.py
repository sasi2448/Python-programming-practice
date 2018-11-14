a,b=input().split()
a,b=[int(a),int(b)]
x=[]
for i in range(1,11):
    if(a%i==0 and b%i==0):
        x.append(i)
x.reverse()
print(x[0])
