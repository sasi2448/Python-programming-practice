import sys
q=sys.maxsize
a=input()
a.split()
a1=''.join(a.replace(',',''))
if(int(a1)<=q):
    print('INT')
else:
    print('LONG LONG')
