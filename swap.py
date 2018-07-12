a=str(raw_input())
a=list(a)
a[::2], a[1::2] = a[1::2], a[::2]
c=''.join(a)
print c
