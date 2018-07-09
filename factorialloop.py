a=int(input())
fact=1
if a<=20:
    for i in range(1,a+1):
        fact=fact*i
    print fact
else:
    print "invalid"
