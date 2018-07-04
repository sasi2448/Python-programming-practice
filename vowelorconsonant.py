a=raw_input()
list={'a','e','i','o','u','A','E','I','O','U'}
if len(a)==1:
    if a in list:
        print "vowel"
    elif a:
        print"consonant"
else:
    print"invalid"
            
