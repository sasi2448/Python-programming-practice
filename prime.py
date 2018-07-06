a=int(input())
l=0
for j in range(2,a//2+1):
    if a%j==0:
        l=l+1
            
if l<=0:
    print "yes"

else:
    print "no"
