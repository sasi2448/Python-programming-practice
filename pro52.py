a,b=input().split()
c,d=input().split()
e,f=input().split()
g,h=input().split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
e=int(e)
f=int(f)
g=int(g)
h=int(h)
if(a==c and d==b+b):
    if(d==f and e==c+c):
        if(e==g and h==f-a):
            if(h==b and a==g-a):
                if(e==a*2 and f==b*2):
                    if(g==c+c and h==d-h):
                        print('yes')
                    else:
                        print('no')
                else:
                    print('no')
            else:
                print('no')
        else:
            print('no')
    else:
        print('no')
else:
    print('no')
