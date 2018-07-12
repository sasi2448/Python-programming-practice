b=int(input())
fact=1
if b<=20:
    for i in range(1,b+1):
        fact=fact*i
    print fact
else:
    print "invalid"
