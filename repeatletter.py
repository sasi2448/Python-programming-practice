a=str(input())
a=list(a)
max=1
for i in range(len(a)):
    count=0
    for j in range(len(a)):
        if a[i]==a[j]:
            count=count+1
        if(count>max):
            max=count
            c=a[i]
			
print(c)
