a,b=input().split()
a,b=[int(a),int(b)]
for i in range(a):
    x=input().split()
    break
l =x[0 : b] 
ls= x[b :]
d=' '.join(ls+l)
print(d)
