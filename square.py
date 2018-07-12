a=int(input())
sums=0
for i in range(10000):
    d=a%10
    sums=sums + (d**2)
    a=a//10
print sums
