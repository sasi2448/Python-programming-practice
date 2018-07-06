a,b=raw_input("enter the size").split()
a=int(a)
b=int(b)
c=0
list=[]
for i in range(a):
    list.append(i+1)
print list
for j in range(b):
    c=list[j]+c
    
print c
    
