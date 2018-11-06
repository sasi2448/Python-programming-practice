a=input()
s=[]
for i in range(len(a)):
    if(a[i] not in s):
       s.append(a[i])
s.sort()
s=''.join(s)
print(s)

