a=int(input())
for i in range(a):
    x=input().split()
    break
x.reverse()
for i in range(0,a):
    if(i==a-1):
        print(int(x[i]),end='')
    else:
        print(int(x[i]),end='->')
