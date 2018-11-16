a,b,c=input().split()
a,b,c=[int(a),int(b),int(c)]
if(a!=0 and b!=0 and c!=0):
    if(a+b+c==180):
        print('yes')
    else:
        print('no')
else:
    print('no')
