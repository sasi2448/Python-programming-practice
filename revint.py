a=int(input())
re=0
while(a!=0):
    s=a%10
    re=(re*10)+s
    a=a/10
print re
