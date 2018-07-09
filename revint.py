a=int(input())
rev=0
while(a!=0):
    s=a%10
    rev=(rev*10)+s
    a=a/10
print rev
