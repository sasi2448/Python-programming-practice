n = int(input())
sum = 0
temp = n
if(n<=100000):
    while temp > 0:
       digit = temp % 10
       sum =sum+digit ** 3
       temp=temp//10
    if n == sum:
       print("yes")
    else:
       print("no")
else:
    print"invalid"
