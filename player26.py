a=input()
c=a.split(' ')
print(c)
s=c.count('')
if(s>=1):
    d=a.split()
    b=' '.join(d)
else:
    b=''.join(c)
print(b)

