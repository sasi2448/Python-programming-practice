q=input()
n=''
for a in q:
    if(a.islower()==True):
        n=n+(a.upper())
    elif(a.isupper()==True):
        n=n+(a.lower())
    else:
        n=n+a
print(n)
