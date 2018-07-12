a=int(input())
l=0
for i in range(2,a//2+1):
    if a%i==0:
        l=l+1
            
if l<=0:
    print "yes"

else:
    print "no"
