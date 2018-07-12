a=int(input())
p=0
sum=0
r=a
if(a<=100000):
    while a>0:
        sum=a%10
        p=p*10+sum
        a=a/10
    if p==r:
        print "yes"
    else:
        print  "no"
else:
    print "invalid"
