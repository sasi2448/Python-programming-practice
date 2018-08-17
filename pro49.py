a=input()
b=input()
c=list(set(a))
q=("".join(c))
count1=0
count=0
if(len(a)==len(c)):
    count1+=1

while(len(q)<len(b)):
    for i in range(len(b)//len(q)):
        if q in b:
            count=count+1
    count1=count1+1        
    q=q+q

    if(len(q)==len(b) and len(q)==len(a)):
        for i in range(len(b)//len(q)):
            if q in b:
                count=count+1
        count1=count1+1        
print(count1)
