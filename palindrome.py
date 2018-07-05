a=int(input())
p=0
sum=0
r=a
if(a<=1000):
    while a>0:
        sum=a%10
        p=p*10+sum
        a=a/10
    if p==r:
        print "palindrome"
    else:
        print  "not a palindrome"
else:
    print "invalid"
