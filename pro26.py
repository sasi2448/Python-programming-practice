a=input()
b=input()
if(len(a)==len(b)):
    for i in range(len(a)):
        x=ord(a[i])
        y=ord(b[i])
        x=x-97
        y=y-97
        w=(x)+(y)
        if(w>=26):
            w=w-26
            print(chr(w+98),end='')
        else:
            print(chr(w+98),end='')
            
        
