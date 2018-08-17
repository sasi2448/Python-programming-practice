a=input()
b=list(a)
n=len(a)
count=0
for i in range(len(a)):
        j = 0
        while(j < n):
            if (i != j and b[i] == b[j]):
                break
            j += 1
        if (j == n):
            count+=1
print(count)
