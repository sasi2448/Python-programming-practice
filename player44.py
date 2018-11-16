a,b=input().split()
b=int(b)
r = a[0 : len(a)-b] 
rs = a[len(a)-b : ]
print (rs+r)
    
    
