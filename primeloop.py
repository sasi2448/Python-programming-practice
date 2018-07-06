a=int(input())
b= int(input())
for i in range(a,b):
    l=0
    for j in range(2,i//2+1):
        if i%j==0:
            l=l+1
            #print l
    if l<=0:
        print i
            
        
    
