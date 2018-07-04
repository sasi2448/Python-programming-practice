print"enter the one alphabet"
a=raw_input()
list={'a','e','i','o','u','A','E','I','O','U'}
if len(a)==1:
    if a in list:
        print "vowel"
    elif( a >=chr(65) and a<=chr(122)):
        print"consonant"
    else :
            print"invalid"
else:
    print"invalid"
