n,k=input().split()
n=int(n)
k=int(k)
for i in range(n):
    x=input().split()
    break
x.sort(reverse=True)
y=x.pop(k-1)
y=int(y)
print(y)

