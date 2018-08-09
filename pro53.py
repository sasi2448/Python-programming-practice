a=input()
a=a.lower()
b=set(a)
if (len(b) == 27 and " " in b) or (len(b) == 26 and " " not in b):
    print('yes')
else:
    print('no')
