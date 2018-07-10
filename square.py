a=int(input())
sum=0
for i in range(10000):
    d=a%10
    sum=sum + (d**2)
    a=a//10
print sum
