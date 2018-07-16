n,k=input().split()
n=int(n)
k=int(k)
for i in range(n):
    x=input().split()
    x.sort(key =int)
    y=x[::-1]
    break
z=y.pop(k-1)
z=int(z)
print(z)



